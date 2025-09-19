import pygame
import random
import sys

# init
pygame.init()

# إعدادات الشاشة
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CS50 Shooter Game")
map_background = pygame.image.load("GAME/assets/map.jpg")
map_background = pygame.transform.scale(map_background, (WIDTH, HEIGHT))
store_background = pygame.image.load("GAME/assets/store.jpg")
store_background = pygame.transform.scale(store_background, (WIDTH, HEIGHT))

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
YELLOW= (255, 255, 0)
BLUE  = (0, 0, 255)

#important variables
kills = 0
last_kills = 10
hp = 500

# the player
player_size = 40
player = pygame.Rect(WIDTH//2, HEIGHT//2, player_size, player_size)
player_speed = 5

# bullet
bullets = []
bullet_speed = 7

# enemies
enemies = []
enemy_size = 40
enemy_spawn_time = 2000  # every 2 seconds
last_spawn = pygame.time.get_ticks()

# coins and crystals
coins = []
crystals = []
gold = 0
crystale = 0
gold_image = pygame.image.load("GAME/assets/coin.png").convert_alpha()
gold_image = pygame.transform.scale(gold_image, (32, 32))

# the door to the shop
door = pygame.Rect(391, 70, 25, 30)

# game state : map or shop
game_state = "map"

# shop
shop_keeper = pygame.Rect(WIDTH//2 - 20, HEIGHT//2 - 50, 40, 80)

def spawn_enemy():
    x = random.choice([0, WIDTH-enemy_size])
    y = random.randint(0, HEIGHT-enemy_size)
    enemies.append(pygame.Rect(x, y, enemy_size, enemy_size))

def draw_map():
    screen.blit(map_background, (0, 0))  

    pygame.draw.rect(screen, GREEN, player)  # the player

    font = pygame.font.SysFont(None, 25)
    text = font.render(f"Kills: {kills}  Gold: {gold}  Crystal: {crystale}  HP: {hp:.0f}", True, WHITE)
    screen.blit(text, (300, 10))

    for bullet in bullets:
        pygame.draw.rect(screen, YELLOW, bullet)

    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    # coins as PNG
    for coin in coins:
        screen.blit(gold_image, coin.topleft)

    # draw crystals as blue points
    for crystal in crystals:
        pygame.draw.rect(screen, BLUE, crystal)

def draw_shop():
    screen.blit(store_background, (0, 0))  # shop background
    pygame.draw.rect(screen, GREEN, player)
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
                    bullets.append(pygame.Rect(player.centerx-5, player.centery-5, 10, 10))
            elif game_state == "shop":
                if event.key == pygame.K_b:  # back to the map
                    game_state = "map"

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  player.x -= player_speed
    if keys[pygame.K_RIGHT]: player.x += player_speed
    if keys[pygame.K_UP]:    player.y -= player_speed
    if keys[pygame.K_DOWN]:  player.y += player_speed

    if game_state == "map":
        # spawn enemies
        now = pygame.time.get_ticks()
        if now - last_spawn > enemy_spawn_time:
            spawn_enemy()
            last_spawn = now

        # bullet animation
        for bullet in bullets[:]:
            bullet.y -= bullet_speed
            if bullet.y < 0:
                bullets.remove(bullet)

        # enemies animation
        for enemy in enemies[:]:
            if enemy.x < player.x: enemy.x += 1
            if enemy.x > player.x: enemy.x -= 1
            if enemy.y < player.y: enemy.y += 1
            if enemy.y > player.y: enemy.y -= 1
            if enemy.colliderect(player):
                hp -= 0.0002

            # boom with bullet
            for bullet in bullets[:]:
                if enemy.colliderect(bullet):
                    enemies.remove(enemy)
                    bullets.remove(bullet)
                    kills += 1
                    hp += 1
                    # احتمال ظهور كوين
                    if random.random() < 0.5:
                        coin_rect = pygame.Rect(enemy.x+10, enemy.y+10, 16, 16)
                        coins.append(coin_rect)
                    # احتمال ظهور كريستال 5%
                    if random.random() < 0.05:
                        crystal_rect = pygame.Rect(enemy.x+10, enemy.y+10, 16, 16)
                        crystals.append(crystal_rect)
                    if(kills == last_kills):
                        last_kills += 10
                        if(player_speed < 15):
                            player_speed += 1
                        if(bullet_speed < 20):
                            bullet_speed += 1
                        if(enemy_spawn_time > 100):
                            enemy_spawn_time -= 100

                    break

        # التقاط الكوينز
        for coin in coins[:]:
            if player.colliderect(coin):
                coins.remove(coin)
                gold += 1

        # التقاط الكريستالات
        for crystal in crystals[:]:
            if player.colliderect(crystal):
                crystals.remove(crystal)
                crystale += 1

        # الدخول للبيت
        if player.colliderect(door):
            game_state = "shop"

        # رسم الخريطة
        draw_map()

    elif game_state == "shop":
        draw_shop()

    pygame.display.flip()