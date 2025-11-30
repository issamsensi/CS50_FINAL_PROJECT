import pygame
import random
import sys
import math

# Initialize Pygame
pygame.init()

# Screen Settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CS50 Shooter Game")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
GRAY = (128, 128, 128)
DARK_GREEN = (0, 128, 0)

# Load backgrounds
try:
    map_background = pygame.image.load("GAME/assets/map.jpg")
    map_background = pygame.transform.scale(map_background, (WIDTH, HEIGHT))
except:
    map_background = pygame.Surface((WIDTH, HEIGHT))
    map_background.fill((50, 50, 50))

try:
    store_background = pygame.image.load("GAME/assets/store.jpg")
    store_background = pygame.transform.scale(store_background, (WIDTH, HEIGHT))
except:
    store_background = pygame.Surface((WIDTH, HEIGHT))
    store_background.fill((80, 60, 40))

# Load coin image
try:
    coin_image = pygame.image.load("GAME/assets/coin.png").convert_alpha()
    coin_image = pygame.transform.scale(coin_image, (24, 24))
except:
    coin_image = pygame.Surface((24, 24))
    coin_image.fill(YELLOW)



class Particle:
    def __init__(self, x, y, color, size=5):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.vx = random.randint(-4, 4)
        self.vy = random.randint(-4, 4)
        self.lifetime = 30
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.lifetime -= 1
        self.size = max(1, self.size - 0.1)
    
    def draw(self, screen):
        if self.lifetime > 0:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.size))


# Player Class
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 40
        self.max_hp = 500
        self.hp = self.max_hp
        self.speed = 5
        self.bullet_speed = 7
        self.damage = 1
        self.fire_rate = 15  
        self.fire_cooldown = 0
        self.direction = 0  
        self.bullet_type = "normal"  
        
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def move(self, keys):
        old_x, old_y = self.x, self.y
        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed
            self.direction = 3
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.speed
            self.direction = 1
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= self.speed
            self.direction = 0
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += self.speed
            self.direction = 2
        
      
        self.x = max(0, min(WIDTH - self.width, self.x))
        self.y = max(0, min(HEIGHT - self.height, self.y))
    
    def shoot(self):
        if self.fire_cooldown <= 0:
            bullets = []
            center_x = self.x + self.width // 2
            center_y = self.y + self.height // 2
            
            if self.bullet_type == "multi":
                
                for angle_offset in [-20, 0, 20]:
                    angle = self.direction * 90 + angle_offset
                    bullets.append(Bullet(center_x, center_y, self.bullet_speed, 
                                        self.damage, angle, "normal"))
            elif self.bullet_type == "laser":
                bullets.append(Bullet(center_x, center_y, self.bullet_speed * 1.5, 
                                    self.damage * 2, self.direction * 90, "laser"))
            else:  
                bullets.append(Bullet(center_x, center_y, self.bullet_speed, 
                                    self.damage, self.direction * 90, "normal"))
            
            self.fire_cooldown = self.fire_rate
            return bullets
        return []
    
    def update(self):
        if self.fire_cooldown > 0:
            self.fire_cooldown -= 1
    
    def draw(self, screen):
        # AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        center_x = self.x + self.width // 2
        center_y = self.y + self.height // 2
        
        if self.direction == 0:  # up
            points = [(center_x, self.y), (self.x, self.y + self.height), 
                     (self.x + self.width, self.y + self.height)]
        elif self.direction == 1:  # right
            points = [(self.x + self.width, center_y), (self.x, self.y), 
                     (self.x, self.y + self.height)]
        elif self.direction == 2:  # down
            points = [(center_x, self.y + self.height), (self.x, self.y), 
                     (self.x + self.width, self.y)]
        else:  # left
            points = [(self.x, center_y), (self.x + self.width, self.y), 
                     (self.x + self.width, self.y + self.height)]
        
        pygame.draw.polygon(screen, GREEN, points)
        pygame.draw.polygon(screen, WHITE, points, 2)


# Bullet Class
class Bullet:
    def __init__(self, x, y, speed, damage, angle, bullet_type="normal"):
        self.x = x
        self.y = y
        self.speed = speed
        self.damage = damage
        self.angle = angle
        self.bullet_type = bullet_type
        self.width = 10 if bullet_type == "normal" else 15
        self.height = 10 if bullet_type == "normal" else 15
        

        rad = math.radians(angle)
        self.vx = math.sin(rad) * speed
        self.vy = -math.cos(rad) * speed
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
    
    def get_rect(self):
        return pygame.Rect(self.x - self.width//2, self.y - self.height//2, 
                          self.width, self.height)
    
    def is_off_screen(self):
        return (self.x < -20 or self.x > WIDTH + 20 or 
                self.y < -20 or self.y > HEIGHT + 20)
    
    def draw(self, screen):
        if self.bullet_type == "laser":
            pygame.draw.circle(screen, PURPLE, (int(self.x), int(self.y)), 7)
        else:
            pygame.draw.circle(screen, YELLOW, (int(self.x), int(self.y)), 5)


# Enemy Class
class Enemy:
    def __init__(self, x, y, enemy_type="normal"):
        self.x = x
        self.y = y
        self.type = enemy_type
        
        if enemy_type == "fast":
            self.width = 30
            self.height = 30
            self.max_hp = 1
            self.hp = 1
            self.speed = 3
            self.damage = 0.5
            self.color = (255, 100, 100)
        elif enemy_type == "tank":
            self.width = 60
            self.height = 60
            self.max_hp = 5
            self.hp = 5
            self.speed = 1
            self.damage = 2
            self.color = (150, 0, 0)
        else:  
            self.width = 40
            self.height = 40
            self.max_hp = 2
            self.hp = 2
            self.speed = 2
            self.damage = 1
            self.color = RED
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def move_towards_player(self, player):
        if self.x < player.x:
            self.x += self.speed
        if self.x > player.x:
            self.x -= self.speed
        if self.y < player.y:
            self.y += self.speed
        if self.y > player.y:
            self.y -= self.speed
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.get_rect())
        pygame.draw.rect(screen, WHITE, self.get_rect(), 2)
        
        # Draw HP bar
        bar_width = self.width
        bar_height = 5
        bar_x = self.x
        bar_y = self.y - 10
        
        # Background (red)
        pygame.draw.rect(screen, RED, (bar_x, bar_y, bar_width, bar_height))
        # Health (green)
        health_width = (self.hp / self.max_hp) * bar_width
        pygame.draw.rect(screen, GREEN, (bar_x, bar_y, health_width, bar_height))


# Collectible Class
class Collectible:
    def __init__(self, x, y, item_type="coin"):
        self.x = x
        self.y = y
        self.type = item_type
        self.width = 24
        self.height = 24
        self.lifetime = 600  
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def update(self):
        self.lifetime -= 1
    
    def draw(self, screen):
        if self.type == "coin":
            screen.blit(coin_image, (self.x, self.y))
        else:  
            pygame.draw.circle(screen, BLUE, (int(self.x + 12), int(self.y + 12)), 10)
            pygame.draw.circle(screen, WHITE, (int(self.x + 12), int(self.y + 12)), 10, 2)


# Game Class
class Game:
    def __init__(self):
        self.state = "map"  
        self.player = Player(WIDTH // 2, HEIGHT // 2)
        self.bullets = []
        self.enemies = []
        self.collectibles = []
        self.particles = []
        
        self.gold = 0
        self.crystals = 0
        self.kills = 0
        self.wave = 1
        
        self.enemy_spawn_timer = 0
        self.enemy_spawn_rate = 120  
        
        self.door = pygame.Rect(391, 70, 25, 30)
        
        self.font_small = pygame.font.SysFont(None, 24)
        self.font_medium = pygame.font.SysFont(None, 32)
        self.font_large = pygame.font.SysFont(None, 48)
    
    def spawn_enemy(self):

        side = random.choice(['left', 'right', 'top', 'bottom'])
        if side == 'left':
            x, y = -40, random.randint(0, HEIGHT - 40)
        elif side == 'right':
            x, y = WIDTH, random.randint(0, HEIGHT - 40)
        elif side == 'top':
            x, y = random.randint(0, WIDTH - 40), -40
        else:  
            x, y = random.randint(0, WIDTH - 40), HEIGHT
        
        
        if self.kills < 20:
            enemy_type = "normal"
        elif self.kills < 50:
            enemy_type = random.choice(["normal", "normal", "fast"])
        else:
            enemy_type = random.choice(["normal", "fast", "tank"])
        
        self.enemies.append(Enemy(x, y, enemy_type))
    
    def create_explosion(self, x, y, color):
        for _ in range(15):
            self.particles.append(Particle(x, y, color))
    
    def update_map(self):
        keys = pygame.key.get_pressed()
        
        
        self.player.move(keys)
        self.player.update()
        
        
        if keys[pygame.K_SPACE]:
            new_bullets = self.player.shoot()
            self.bullets.extend(new_bullets)
        
        for bullet in self.bullets[:]:
            bullet.update()
            if bullet.is_off_screen():
                self.bullets.remove(bullet)
        
        
        self.enemy_spawn_timer += 1
        if self.enemy_spawn_timer >= self.enemy_spawn_rate:
            self.spawn_enemy()
            self.enemy_spawn_timer = 0
        
        
        for enemy in self.enemies[:]:
            enemy.move_towards_player(self.player)
            
            
            if enemy.get_rect().colliderect(self.player.get_rect()):
                self.player.hp -= enemy.damage * 0.1
            
            
            for bullet in self.bullets[:]:
                if enemy.get_rect().colliderect(bullet.get_rect()):
                    enemy.hp -= bullet.damage
                    if bullet in self.bullets:
                        self.bullets.remove(bullet)
                    
                    if enemy.hp <= 0:
                        self.kills += 1
                        self.create_explosion(enemy.x + enemy.width // 2, 
                                            enemy.y + enemy.height // 2, enemy.color)
                        
                        
                        if random.random() < 0.5:  
                            self.collectibles.append(Collectible(enemy.x, enemy.y, "coin"))
                        if random.random() < 0.05: 
                            self.collectibles.append(Collectible(enemy.x, enemy.y, "crystal"))
                        
                        if enemy in self.enemies:
                            self.enemies.remove(enemy)
                    break
        
        for collectible in self.collectibles[:]:
            collectible.update()
            if collectible.lifetime <= 0:
                self.collectibles.remove(collectible)
            elif collectible.get_rect().colliderect(self.player.get_rect()):
                if collectible.type == "coin":
                    self.gold += 1
                else:
                    self.crystals += 1
                self.create_explosion(collectible.x + 12, collectible.y + 12, 
                                    YELLOW if collectible.type == "coin" else BLUE)
                self.collectibles.remove(collectible)
        
        
        for particle in self.particles[:]:
            particle.update()
            if particle.lifetime <= 0:
                self.particles.remove(particle)
        
        
        if self.kills >= self.wave * 10:
            self.wave += 1
            self.enemy_spawn_rate = max(30, self.enemy_spawn_rate - 10)
        
    
        if self.player.get_rect().colliderect(self.door):
            self.state = "shop"
        
        
        if self.player.hp <= 0:
            self.state = "game_over"
    
    def draw_map(self):
        screen.blit(map_background, (0, 0))
        
        
        pygame.draw.rect(screen, (139, 69, 19), self.door)
        pygame.draw.rect(screen, BLACK, self.door, 2)
        
        
        self.player.draw(screen)
        
       
        for bullet in self.bullets:
            bullet.draw(screen)
        
       
        for enemy in self.enemies:
            enemy.draw(screen)
        
        
        for collectible in self.collectibles:
            collectible.draw(screen)
        
        for particle in self.particles:
            particle.draw(screen)
        
   
        self.draw_hud()
    
    def draw_hud(self):
        # Health bar
        bar_width = 200
        bar_height = 20
        bar_x = 10
        bar_y = 10
        
        pygame.draw.rect(screen, RED, (bar_x, bar_y, bar_width, bar_height))
        health_width = (self.player.hp / self.player.max_hp) * bar_width
        pygame.draw.rect(screen, GREEN, (bar_x, bar_y, health_width, bar_height))
        pygame.draw.rect(screen, WHITE, (bar_x, bar_y, bar_width, bar_height), 2)
        
        hp_text = self.font_small.render(f"HP: {int(self.player.hp)}/{self.player.max_hp}", 
                                         True, BLACK)
        screen.blit(hp_text, (bar_x + 5, bar_y + 2))
        
        # Stats
        stats_y = 40
        stats = [
            f"Kills: {self.kills}",
            f"Wave: {self.wave}",
            f"Gold: {self.gold}",
            f"Crystals: {self.crystals}"
        ]
        
        for i, stat in enumerate(stats):
            text = self.font_small.render(stat, True, WHITE)
            screen.blit(text, (10, stats_y + i * 25))
    
    def draw_shop(self):
        screen.blit(store_background, (0, 0))
        
        # Title
        title = self.font_large.render("SHOP", True, WHITE)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 20))
        
        # Instructions
        instruction = self.font_small.render("Press B to go back | Press number keys to buy", 
                                            True, WHITE)
        screen.blit(instruction, (WIDTH // 2 - instruction.get_width() // 2, 70))
        
        # Player stats
        stats_x = 30
        stats_y = 120
        stats = [
            f"Your Gold: {self.gold}",
            f"Your Crystals: {self.crystals}",
            f"Max HP: {self.player.max_hp}",
            f"Speed: {self.player.speed}",
            f"Damage: {self.player.damage}",
            f"Fire Rate: {20 - self.player.fire_rate}",
        ]
        
        for i, stat in enumerate(stats):
            text = self.font_small.render(stat, True, WHITE)
            screen.blit(text, (stats_x, stats_y + i * 30))
        
        # Shop items
        items_x = 400
        items_y = 120
        
        shop_items = [
            ("1. Increase Max HP (+100) - 50 Gold", 50, "gold"),
            ("2. Increase Speed (+1) - 30 Gold", 30, "gold"),
            ("3. Increase Damage (+1) - 40 Gold", 40, "gold"),
            ("4. Increase Fire Rate - 35 Gold", 35, "gold"),
            ("5. Multi-Shot - 3 Crystals", 3, "crystal"),
            ("6. Laser Bullets - 5 Crystals", 5, "crystal"),
        ]
        
        for i, (item, cost, currency) in enumerate(shop_items):
            color = WHITE
            if currency == "gold" and self.gold < cost:
                color = GREEN
            elif currency == "crystal" and self.crystals < cost:
                color = GREEN
            
            text = self.font_small.render(item, True, color)
            screen.blit(text, (items_x, items_y + i * 40))
    
    def handle_shop_purchase(self, key):
        if key == pygame.K_1 and self.gold >= 50:
            self.gold -= 50
            self.player.max_hp += 100
            self.player.hp = min(self.player.hp + 100, self.player.max_hp)
        elif key == pygame.K_2 and self.gold >= 30:
            self.gold -= 30
            self.player.speed = min(15, self.player.speed + 1)
        elif key == pygame.K_3 and self.gold >= 40:
            self.gold -= 40
            self.player.damage += 1
        elif key == pygame.K_4 and self.gold >= 35:
            self.gold -= 35
            self.player.fire_rate = max(5, self.player.fire_rate - 2)
        elif key == pygame.K_5 and self.crystals >= 3:
            self.crystals -= 3
            self.player.bullet_type = "multi"
        elif key == pygame.K_6 and self.crystals >= 5:
            self.crystals -= 5
            self.player.bullet_type = "laser"
    
    def draw_game_over(self):
        screen.fill(BLACK)
        
        title = self.font_large.render("GAME OVER", True, RED)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2 - 100))
        
        stats = [
            f"Final Kills: {self.kills}",
            f"Wave Reached: {self.wave}",
            f"Gold Collected: {self.gold}",
            f"Crystals Collected: {self.crystals}"
        ]
        
        for i, stat in enumerate(stats):
            text = self.font_medium.render(stat, True, WHITE)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 + i * 40))
        
        restart = self.font_small.render("Press R to Restart or Q to Quit", True, WHITE)
        screen.blit(restart, (WIDTH // 2 - restart.get_width() // 2, HEIGHT - 100))
    
    def run(self):
        running = True
        while running:
            clock.tick(60)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.KEYDOWN:
                    if self.state == "shop":
                        if event.key == pygame.K_b:
                            self.state = "map"
                            self.player.y = self.door.y + self.door.height + 10
                        else:
                            self.handle_shop_purchase(event.key)
                    
                    elif self.state == "game_over":
                        if event.key == pygame.K_r:
                            self.__init__()  
                        elif event.key == pygame.K_q:
                            running = False
            
            
            if self.state == "map":
                self.update_map()
                self.draw_map()
            elif self.state == "shop":
                self.draw_shop()
            elif self.state == "game_over":
                self.draw_game_over()
            
            pygame.display.flip()
        
        pygame.quit()
        sys.exit()


# Run the game
if __name__ == "__main__":
    game = Game()
    game.run()
