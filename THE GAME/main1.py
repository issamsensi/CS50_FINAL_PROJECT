import pygame
import random
import sys

# init
pygame.init()

# إعدادات الشاشة
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CS50 Shooter Game")
map_background = pygame.image.load("THE GAME/assets/map.jpg")
map_background = pygame.transform.scale(map_background, (WIDTH, HEIGHT))
store_background = pygame.image.load("THE GAME/assets/store.jpg")
store_background = pygame.transform.scale(store_background, (WIDTH, HEIGHT))

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
YELLOW= (255, 255, 0)
BLUE  = (0, 0, 255)


# the player
player_size = 40
player_speed = 5
class Player:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH//2, HEIGHT//2, player_size, player_size)
        self.speed = 5
        self.hp = 500
        self.kills = 0
        self.last_kills = 10

# bullet
class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 10)
        self.speed = 7
        self.bullets = []

# enemies
enemy_size = 40
class Enemy:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, enemy_size, enemy_size)
        self.enemies = []
        self.spawn_time = 2000  # every 2 seconds

last_spawn = pygame.time.get_ticks()

# coins and crystals
class Money:
    def __init__(self):
        self.coins = []
        self.crystals = []
        self.gold = 0
        self.crystale = 0
        self.gold_image = pygame.image.load("THE GAME/assets/coin.png").convert_alpha()
        self.gold_image = pygame.transform.scale(self.gold_image, (32, 32))

# the door to the shop
door = pygame.Rect(391, 70, 25, 30)

# game state : map or shop
game_state = "map"

# shop
shop_keeper = pygame.Rect(WIDTH//2 - 20, HEIGHT//2 - 50, 40, 80)

def spawn_enemy():
    x = random.choice([0, WIDTH-enemy_size])
    y = random.randint(0, HEIGHT-enemy_size)
    Enemy.enemies.append(pygame.Rect(x, y, enemy_size, enemy_size))

def draw_map():
    screen.blit(map_background, (0, 0))  

    pygame.draw.rect(screen, GREEN, Player)  # the player

    font = pygame.font.SysFont(None, 25)
    text = font.render(f"Kills: {Player.kills}  Gold: {Money.gold}  Crystal: {Money.crystale}  HP: {Player.hp:.0f}", True, WHITE)
    screen.blit(text, (300, 10))

    for bullet in Bullet.bullets:
        pygame.draw.rect(screen, YELLOW, bullet)

    for enemy in Enemy.enemies:
        pygame.draw.rect(screen, RED, enemy)

    # coins as PNG
    for coin in Money.coins:
        screen.blit(Money.gold_image, coin.topleft)

    # draw crystals as blue points
    for crystal in Money.crystals:
        pygame.draw.rect(screen, BLUE, crystal)

def draw_shop():
    screen.blit(store_background, (0, 0))  # shop background
    pygame.draw.rect(screen, GREEN, Player)
    font = pygame.font.SysFont(None, 30)
    text = font.render("Welcome to the Shop! (Press B to go back)", True, WHITE)
    screen.blit(text, (150, 50))

# Main Loop
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if game_state == "map":
                if event.key == pygame.K_SPACE:
                    # a bullet
                    Bullet.bullets.append(pygame.Rect(Player.centerx-5, Player.centery-5, 10, 10))
            elif game_state == "shop":
                if event.key == pygame.K_b:  # back to the map
                    game_state = "map"

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  Player.x -= player_speed
    if keys[pygame.K_RIGHT]: Player.x += player_speed
    if keys[pygame.K_UP]:    Player.y -= player_speed
    if keys[pygame.K_DOWN]:  Player.y += player_speed

    if game_state == "map":
        # spawn enemies
        now = pygame.time.get_ticks()
        if now - last_spawn > Enemy.spawn_time:
            spawn_enemy()
            last_spawn = now

        # bullet animation
        for bullet in Bullet.bullets[:]:
            bullet.y -= Bullet.speed
            if bullet.y < 0:
                Bullet.bullets.remove(bullet)

        # enemies animation
        for enemy in Enemy.enemies[:]:
            if enemy.x < Player.x: enemy.x += 1
            if enemy.x > Player.x: enemy.x -= 1
            if enemy.y < Player.y: enemy.y += 1
            if enemy.y > Player.y: enemy.y -= 1
            if enemy.colliderect(Player):
                Player.hp -= 0.0002

            # boom with bullet
            for bullet in Bullet.bullets[:]:
                if enemy.colliderect(bullet):
                    Enemy.enemies.remove(enemy)
                    Bullet.bullets.remove(bullet)
                    Player.kills += 1
                    Player.hp += 1
                    # احتمال ظهور كوين
                    if random.random() < 0.5:
                        coin_rect = pygame.Rect(enemy.x+10, enemy.y+10, 16, 16)
                        Money.coins.append(coin_rect)
                    # احتمال ظهور كريستال 5%
                    if random.random() < 0.05:
                        crystal_rect = pygame.Rect(enemy.x+10, enemy.y+10, 16, 16)
                        Money.crystals.append(crystal_rect)
                    if(Player.kills == Player.last_kills):
                        Player.last_kills += 10
                        if(Player.speed < 12):
                            Player.speed += 1
                        if(Bullet.speed < 20):
                            Bullet.speed += 1
                        if(Enemy.spawn_time > 100):
                            Enemy.spawn_time -= 100

                    break

        # التقاط الكوينز
        for coin in Money.coins[:]:
            if Player.colliderect(coin):
                Money.coins.remove(coin)
                gold += 1

        # التقاط الكريستالات
        for crystal in Money.crystals[:]:
            if Player.colliderect(crystal):
                Money.crystals.remove(crystal)
                crystale += 1

        # الدخول للبيت
        if Player.colliderect(door):
            game_state = "shop"

        # رسم الخريطة
        draw_map()

    elif game_state == "shop":
        draw_shop()

    pygame.display.flip()