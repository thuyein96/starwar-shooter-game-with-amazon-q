import pygame
import random
import math
import sys
import os
from pygame import mixer

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Star Wars: Rebel Defense")

# Create assets directory if it doesn't exist
assets_dir = os.path.join(os.path.dirname(__file__), "assets")
if not os.path.exists(assets_dir):
    os.makedirs(assets_dir)
    os.makedirs(os.path.join(assets_dir, "ships"))
    os.makedirs(os.path.join(assets_dir, "effects"))
    os.makedirs(os.path.join(assets_dir, "powerups"))

# Function to create ship images
def create_ship_image(color, width, height, ship_type):
    img = pygame.Surface((width, height), pygame.SRCALPHA)
    
    if ship_type == "x_wing":
        # X-Wing design
        # Main body
        pygame.draw.rect(img, color, (width//4, height//4, width//2, height//2))
        
        # Wings
        pygame.draw.polygon(img, color, [(0, height//4), (width//4, height//4), (width//4, 3*height//4), (0, 3*height//4)])
        pygame.draw.polygon(img, color, [(3*width//4, height//4), (width, height//4), (width, 3*height//4), (3*width//4, 3*height//4)])
        
        # Engines
        pygame.draw.rect(img, (200, 200, 200), (width//4, 3*height//4, width//8, height//8))
        pygame.draw.rect(img, (200, 200, 200), (5*width//8, 3*height//4, width//8, height//8))
        
        # Cockpit
        pygame.draw.circle(img, (100, 100, 255), (width//2, height//2), width//8)
        
        # Laser cannons
        pygame.draw.rect(img, (200, 0, 0), (width//8, height//8, width//16, height//8))
        pygame.draw.rect(img, (200, 0, 0), (7*width//8 - width//16, height//8, width//16, height//8))
        pygame.draw.rect(img, (200, 0, 0), (width//8, 3*height//4 - height//8, width//16, height//8))
        pygame.draw.rect(img, (200, 0, 0), (7*width//8 - width//16, 3*height//4 - height//8, width//16, height//8))
        
    elif ship_type == "tie_fighter":
        # TIE Fighter design
        # Center pod
        pygame.draw.circle(img, (80, 80, 80), (width//2, height//2), width//6)
        
        # Wing panels
        pygame.draw.polygon(img, color, [
            (0, height//6), (width//3, height//6), 
            (width//3, 5*height//6), (0, 5*height//6)
        ])
        pygame.draw.polygon(img, color, [
            (2*width//3, height//6), (width, height//6), 
            (width, 5*height//6), (2*width//3, 5*height//6)
        ])
        
        # Wing details
        for i in range(3):
            y_pos = height//4 + i * height//6
            pygame.draw.line(img, (50, 50, 50), (0, y_pos), (width//3, y_pos), 2)
            pygame.draw.line(img, (50, 50, 50), (2*width//3, y_pos), (width, y_pos), 2)
        
        # Cockpit window
        pygame.draw.circle(img, (255, 0, 0), (width//2, height//2), width//12)
        
    elif ship_type == "tie_bomber":
        # TIE Bomber design
        # Twin pods
        pygame.draw.circle(img, (80, 80, 80), (width//2, height//2 - height//8), width//6)
        pygame.draw.circle(img, (100, 100, 100), (width//2, height//2 + height//8), width//5)
        
        # Wing panels
        pygame.draw.polygon(img, color, [
            (0, height//6), (width//3, height//6), 
            (width//3, 5*height//6), (0, 5*height//6)
        ])
        pygame.draw.polygon(img, color, [
            (2*width//3, height//6), (width, height//6), 
            (width, 5*height//6), (2*width//3, 5*height//6)
        ])
        
        # Wing details
        for i in range(4):
            y_pos = height//5 + i * height//7
            pygame.draw.line(img, (50, 50, 50), (0, y_pos), (width//3, y_pos), 2)
            pygame.draw.line(img, (50, 50, 50), (2*width//3, y_pos), (width, y_pos), 2)
        
        # Cockpit window
        pygame.draw.circle(img, (255, 0, 0), (width//2, height//2 - height//8), width//12)
        
    elif ship_type == "tie_interceptor":
        # TIE Interceptor design
        # Center pod
        pygame.draw.circle(img, (80, 80, 80), (width//2, height//2), width//6)
        
        # Angled wing panels
        pygame.draw.polygon(img, color, [
            (0, height//3), (width//3, height//6), 
            (width//3, 5*height//6), (0, 2*height//3)
        ])
        pygame.draw.polygon(img, color, [
            (2*width//3, height//6), (width, height//3), 
            (width, 2*height//3), (2*width//3, 5*height//6)
        ])
        
        # Wing tips
        pygame.draw.polygon(img, (150, 150, 150), [
            (0, height//3), (width//10, height//4), 
            (width//10, 3*height//4), (0, 2*height//3)
        ])
        pygame.draw.polygon(img, (150, 150, 150), [
            (9*width//10, height//4), (width, height//3), 
            (width, 2*height//3), (9*width//10, 3*height//4)
        ])
        
        # Cockpit window
        pygame.draw.circle(img, (255, 0, 0), (width//2, height//2), width//12)
    
    return img

# Function to create power-up images
def create_powerup_image(color, width, height, powerup_type):
    img = pygame.Surface((width, height), pygame.SRCALPHA)
    
    if powerup_type == "rapid_fire":
        # Rapid fire - lightning bolt
        pygame.draw.polygon(img, color, [
            (width//2, 0), 
            (width//4, height//2), 
            (width//2, height//2), 
            (width//4, height), 
            (3*width//4, height//3),
            (width//2, height//3)
        ])
        pygame.draw.circle(img, (255, 255, 255, 180), (width//2, height//2), width//3, 2)
        
    elif powerup_type == "shield":
        # Shield - shield shape
        pygame.draw.circle(img, color, (width//2, height//2), width//2 - 2, 3)
        pygame.draw.circle(img, color, (width//2, height//2), width//3, 2)
        pygame.draw.line(img, color, (width//2, height//6), (width//2, 5*height//6), 2)
        pygame.draw.line(img, color, (width//6, height//2), (5*width//6, height//2), 2)
        
    elif powerup_type == "double_laser":
        # Double laser - two parallel lines
        pygame.draw.rect(img, color, (width//3 - 2, height//6, 4, 2*height//3))
        pygame.draw.rect(img, color, (2*width//3 - 2, height//6, 4, 2*height//3))
        pygame.draw.circle(img, (255, 255, 255, 180), (width//2, height//2), width//3, 2)
        
    return img

# Function to create explosion animation frames
def create_explosion_frames(num_frames):
    frames = []
    max_radius = 32
    
    for i in range(num_frames):
        progress = i / (num_frames - 1)
        radius = int(max_radius * progress)
        
        if progress < 0.7:
            # Expanding phase
            frame = pygame.Surface((max_radius*2, max_radius*2), pygame.SRCALPHA)
            
            # Outer circle
            pygame.draw.circle(frame, (255, 200, 0, 255 - int(255 * progress)), 
                              (max_radius, max_radius), radius)
            
            # Inner circle
            inner_radius = max(0, int(radius * 0.6))
            pygame.draw.circle(frame, (255, 100, 0, 255 - int(200 * progress)), 
                              (max_radius, max_radius), inner_radius)
            
        else:
            # Fading phase
            fade = 1.0 - ((progress - 0.7) / 0.3)
            frame = pygame.Surface((max_radius*2, max_radius*2), pygame.SRCALPHA)
            
            # Outer circle
            pygame.draw.circle(frame, (255, 200, 0, int(100 * fade)), 
                              (max_radius, max_radius), radius)
            
            # Inner circle
            inner_radius = max(0, int(radius * 0.6))
            pygame.draw.circle(frame, (255, 100, 0, int(150 * fade)), 
                              (max_radius, max_radius), inner_radius)
        
        frames.append(frame)
    
    return frames

# Create ship images
player_img = create_ship_image((100, 150, 255), 64, 64, "x_wing")
tie_fighter_img = create_ship_image((180, 180, 180), 48, 48, "tie_fighter")
tie_bomber_img = create_ship_image((150, 150, 150), 56, 56, "tie_bomber")
tie_interceptor_img = create_ship_image((200, 200, 200), 44, 44, "tie_interceptor")

# Create power-up images
rapid_fire_img = create_powerup_image((0, 255, 255), 30, 30, "rapid_fire")
shield_img = create_powerup_image((0, 100, 255), 30, 30, "shield")
double_laser_img = create_powerup_image((255, 255, 0), 30, 30, "double_laser")

# Create explosion animation
explosion_imgs = create_explosion_frames(8)

# Laser images
player_laser_img = pygame.Surface((5, 20), pygame.SRCALPHA)
pygame.draw.rect(player_laser_img, (0, 255, 0), (0, 0, 5, 20))
pygame.draw.rect(player_laser_img, (200, 255, 200), (1, 1, 3, 18))

enemy_laser_img = pygame.Surface((5, 20), pygame.SRCALPHA)
pygame.draw.rect(enemy_laser_img, (255, 0, 0), (0, 0, 5, 20))
pygame.draw.rect(enemy_laser_img, (255, 200, 200), (1, 1, 3, 18))

# Background stars for parallax effect
class Star:
    def __init__(self, layer):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        # Different layers move at different speeds
        self.layer = layer
        if layer == 1:  # Distant stars
            self.speed = 0.5
            self.size = 1
            self.color = (100, 100, 100)
        elif layer == 2:  # Mid-distance stars
            self.speed = 1
            self.size = 2
            self.color = (150, 150, 150)
        else:  # Close stars
            self.speed = 2
            self.size = 3
            self.color = (200, 200, 200)
    
    def update(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = 0
            self.x = random.randint(0, WIDTH)
    
    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)

# Create stars for parallax background
stars = []
for layer in range(1, 4):
    for _ in range(50):  # 50 stars per layer
        stars.append(Star(layer))

# Player class
class Player:
    def __init__(self):
        self.img = player_img
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.x = WIDTH // 2 - self.width // 2
        self.y = HEIGHT - self.height - 20
        self.speed = 5
        self.health = 100
        self.max_health = 100
        self.cooldown = 0
        self.cooldown_max = 15  # Frames between shots
        self.shield = 0
        self.shield_max = 100
        self.power_up = None
        self.power_up_time = 0
    
    def move(self, direction):
        if direction == "left" and self.x > 0:
            self.x -= self.speed
        if direction == "right" and self.x < WIDTH - self.width:
            self.x += self.speed
    
    def shoot(self):
        if self.cooldown <= 0:
            if self.power_up == "double_laser":
                return [Laser(self.x + 10, self.y, "player"), 
                        Laser(self.x + self.width - 15, self.y, "player")]
            else:
                return [Laser(self.x + self.width // 2 - 2, self.y, "player")]
            
            # Reset cooldown based on power-up
            if self.power_up == "rapid_fire":
                self.cooldown = self.cooldown_max // 2
            else:
                self.cooldown = self.cooldown_max
        return []
    
    def update(self):
        self.cooldown -= 1
        
        # Update power-up timer
        if self.power_up:
            self.power_up_time -= 1
            if self.power_up_time <= 0:
                self.power_up = None
    
    def draw(self):
        screen.blit(self.img, (self.x, self.y))
        
        # Draw health bar
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y + self.height + 10, self.width, 5))
        pygame.draw.rect(screen, (0, 255, 0), 
                        (self.x, self.y + self.height + 10, 
                         self.width * (self.health / self.max_health), 5))
        
        # Draw shield if active
        if self.shield > 0:
            pygame.draw.circle(screen, (0, 100, 255, 128), 
                              (self.x + self.width // 2, self.y + self.height // 2), 
                              max(self.width, self.height) // 2 + 10, 2)

# Enemy class
class Enemy:
    def __init__(self, enemy_type):
        self.type = enemy_type
        
        if enemy_type == "tie_fighter":
            self.img = tie_fighter_img
            self.health = 10
            self.speed = 2
            self.shoot_chance = 0.005  # 0.5% chance to shoot each frame
            self.score_value = 10
            self.movement_pattern = "straight"
        elif enemy_type == "tie_bomber":
            self.img = tie_bomber_img
            self.health = 20
            self.speed = 1
            self.shoot_chance = 0.01  # 1% chance to shoot each frame
            self.score_value = 20
            self.movement_pattern = "zigzag"
        elif enemy_type == "tie_interceptor":
            self.img = tie_interceptor_img
            self.health = 5
            self.speed = 3
            self.shoot_chance = 0.007  # 0.7% chance to shoot each frame
            self.score_value = 15
            self.movement_pattern = "swoop"
        
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.x = random.randint(0, WIDTH - self.width)
        self.y = -self.height
        
        # For zigzag and swoop patterns
        self.direction = 1  # 1 for right, -1 for left
        self.angle = 0  # For swoop pattern
    
    def move(self):
        if self.movement_pattern == "straight":
            self.y += self.speed
        elif self.movement_pattern == "zigzag":
            self.y += self.speed
            self.x += self.direction * self.speed
            
            # Change direction if hitting screen edge
            if self.x <= 0 or self.x >= WIDTH - self.width:
                self.direction *= -1
        elif self.movement_pattern == "swoop":
            self.y += self.speed
            self.angle += 0.05
            self.x += math.sin(self.angle) * 3
    
    def shoot(self):
        if random.random() < self.shoot_chance:
            return Laser(self.x + self.width // 2 - 2, self.y + self.height, "enemy")
        return None
    
    def draw(self):
        screen.blit(self.img, (self.x, self.y))

# Laser class
class Laser:
    def __init__(self, x, y, source):
        self.source = source
        if source == "player":
            self.img = player_laser_img
            self.speed = -10  # Negative because it moves up
        else:
            self.img = enemy_laser_img
            self.speed = 7
        
        self.x = x
        self.y = y
        self.width = self.img.get_width()
        self.height = self.img.get_height()
    
    def move(self):
        self.y += self.speed
    
    def off_screen(self):
        return self.y < 0 or self.y > HEIGHT
    
    def collision(self, obj):
        # Simple rectangle collision
        return (self.x < obj.x + obj.width and
                self.x + self.width > obj.x and
                self.y < obj.y + obj.height and
                self.y + self.height > obj.y)
    
    def draw(self):
        screen.blit(self.img, (self.x, self.y))

# Power-up class
class PowerUp:
    def __init__(self):
        self.type = random.choice(["rapid_fire", "shield", "double_laser"])
        
        if self.type == "rapid_fire":
            self.img = rapid_fire_img
        elif self.type == "shield":
            self.img = shield_img
        else:  # double_laser
            self.img = double_laser_img
        
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.x = random.randint(0, WIDTH - self.width)
        self.y = -self.height
        self.speed = 2
        self.duration = 300  # Power-up lasts for 300 frames (5 seconds at 60 FPS)
    
    def move(self):
        self.y += self.speed
    
    def off_screen(self):
        return self.y > HEIGHT
    
    def collision(self, player):
        # Simple rectangle collision
        return (self.x < player.x + player.width and
                self.x + self.width > player.x and
                self.y < player.y + player.height and
                self.y + self.height > player.y)
    
    def draw(self):
        screen.blit(self.img, (self.x, self.y))

# Explosion class
class Explosion:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.images = explosion_imgs
        self.index = 0
        self.counter = 0
        self.speed = 3  # Animation speed
    
    def update(self):
        self.counter += 1
        if self.counter >= self.speed:
            self.counter = 0
            self.index += 1
    
    def draw(self):
        if self.index < len(self.images):
            screen.blit(self.images[self.index], (self.x, self.y))
        
    def is_finished(self):
        return self.index >= len(self.images)

# Game state
def main_game():
    # Game objects
    player = Player()
    enemies = []
    lasers = []
    power_ups = []
    explosions = []
    
    # Game variables
    score = 0
    level = 1
    enemy_spawn_rate = 60  # Frames between enemy spawns
    enemy_spawn_counter = 0
    power_up_spawn_rate = 500  # Frames between power-up spawns
    power_up_spawn_counter = 0
    game_over = False
    
    # Game font
    font = pygame.font.SysFont('comicsans', 30)
    
    # Game clock
    clock = pygame.time.Clock()
    FPS = 60
    
    # Main game loop
    running = True
    while running:
        clock.tick(FPS)
        
        # Fill screen with black
        screen.fill((0, 0, 0))
        
        # Draw parallax background
        for star in stars:
            star.update()
            star.draw()
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    sys.exit()
                
                # Restart game if game over
                if game_over and event.key == pygame.K_r:
                    main_game()  # Restart game
        
        # Game over check
        if game_over:
            game_over_text = font.render("GAME OVER - Press R to Restart", True, (255, 255, 255))
            screen.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//2))
            pygame.display.update()
            continue
        
        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move("left")
        if keys[pygame.K_RIGHT]:
            player.move("right")
        
        # Player shooting
        if keys[pygame.K_SPACE]:
            new_lasers = player.shoot()
            lasers.extend(new_lasers)
        
        # Update player
        player.update()
        
        # Spawn enemies
        enemy_spawn_counter += 1
        if enemy_spawn_counter >= enemy_spawn_rate:
            enemy_spawn_counter = 0
            
            # Determine enemy type based on level and randomness
            enemy_types = ["tie_fighter"]
            if level >= 2:
                enemy_types.append("tie_interceptor")
            if level >= 3:
                enemy_types.append("tie_bomber")
            
            enemy_type = random.choice(enemy_types)
            enemies.append(Enemy(enemy_type))
        
        # Spawn power-ups
        power_up_spawn_counter += 1
        if power_up_spawn_counter >= power_up_spawn_rate:
            power_up_spawn_counter = 0
            power_ups.append(PowerUp())
        
        # Update enemies
        for enemy in enemies[:]:
            enemy.move()
            
            # Enemy shooting
            enemy_laser = enemy.shoot()
            if enemy_laser:
                lasers.append(enemy_laser)
            
            # Check if enemy is off screen
            if enemy.y > HEIGHT:
                enemies.remove(enemy)
            
            # Check collision with player
            if (enemy.x < player.x + player.width and
                enemy.x + enemy.width > player.x and
                enemy.y < player.y + player.height and
                enemy.y + enemy.height > player.y):
                
                # If player has shield, reduce shield instead of health
                if player.shield > 0:
                    player.shield -= 20
                    if player.shield < 0:
                        player.shield = 0
                    
                    # Create explosion
                    explosions.append(Explosion(enemy.x, enemy.y))
                    enemies.remove(enemy)
                else:
                    # Player takes damage
                    player.health -= 20
                    
                    # Create explosion
                    explosions.append(Explosion(enemy.x, enemy.y))
                    enemies.remove(enemy)
                    
                    # Check if player is dead
                    if player.health <= 0:
                        game_over = True
        
        # Update lasers
        for laser in lasers[:]:
            laser.move()
            
            # Check if laser is off screen
            if laser.off_screen():
                lasers.remove(laser)
                continue
            
            # Check collision with enemies (if player laser)
            if laser.source == "player":
                for enemy in enemies[:]:
                    if laser.collision(enemy):
                        enemy.health -= 10
                        
                        if enemy.health <= 0:
                            # Create explosion
                            explosions.append(Explosion(enemy.x, enemy.y))
                            
                            # Add score
                            score += enemy.score_value
                            
                            # Remove enemy
                            enemies.remove(enemy)
                        
                        # Remove laser
                        if laser in lasers:
                            lasers.remove(laser)
                        break
            
            # Check collision with player (if enemy laser)
            elif laser.source == "enemy" and laser.collision(player):
                # If player has shield, reduce shield instead of health
                if player.shield > 0:
                    player.shield -= 10
                    if player.shield < 0:
                        player.shield = 0
                else:
                    # Player takes damage
                    player.health -= 10
                    
                    # Check if player is dead
                    if player.health <= 0:
                        game_over = True
                
                # Remove laser
                lasers.remove(laser)
        
        # Update power-ups
        for power_up in power_ups[:]:
            power_up.move()
            
            # Check if power-up is off screen
            if power_up.off_screen():
                power_ups.remove(power_up)
                continue
            
            # Check collision with player
            if power_up.collision(player):
                # Apply power-up effect
                player.power_up = power_up.type
                player.power_up_time = power_up.duration
                
                # If shield power-up, add shield
                if power_up.type == "shield":
                    player.shield = player.shield_max
                
                # Remove power-up
                power_ups.remove(power_up)
        
        # Update explosions
        for explosion in explosions[:]:
            explosion.update()
            if explosion.is_finished():
                explosions.remove(explosion)
        
        # Level progression
        if score >= level * 100:
            level += 1
            enemy_spawn_rate = max(20, enemy_spawn_rate - 5)  # Increase spawn rate
        
        # Draw everything
        player.draw()
        
        for enemy in enemies:
            enemy.draw()
        
        for laser in lasers:
            laser.draw()
        
        for power_up in power_ups:
            power_up.draw()
        
        for explosion in explosions:
            explosion.draw()
        
        # Draw UI
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        level_text = font.render(f"Level: {level}", True, (255, 255, 255))
        
        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (WIDTH - level_text.get_width() - 10, 10))
        
        # Draw power-up indicator if active
        if player.power_up:
            power_up_text = font.render(f"Power-up: {player.power_up.replace('_', ' ').title()}", True, (255, 255, 0))
            screen.blit(power_up_text, (WIDTH//2 - power_up_text.get_width()//2, 10))
        
        # Update display
        pygame.display.update()

# Start menu
def main_menu():
    # Menu font
    title_font = pygame.font.SysFont('comicsans', 60)  # Reduced font size
    subtitle_font = pygame.font.SysFont('comicsans', 30)
    button_font = pygame.font.SysFont('comicsans', 40)
    
    # Main menu loop
    running = True
    while running:
        screen.fill((0, 0, 0))
        
        # Draw stars for background
        for star in stars:
            star.update()
            star.draw()
        
        # Draw title (split into two lines)
        title_text = title_font.render("STAR WARS", True, (255, 255, 0))
        subtitle_text = subtitle_font.render("REBEL DEFENSE", True, (255, 255, 0))
        
        # Position the title and subtitle
        screen.blit(title_text, (WIDTH//2 - title_text.get_width()//2, 80))
        screen.blit(subtitle_text, (WIDTH//2 - subtitle_text.get_width()//2, 150))
        
        # Draw decorative line
        pygame.draw.line(screen, (255, 255, 0), (WIDTH//4, 200), (3*WIDTH//4, 200), 2)
        
        # Draw start button
        start_button = pygame.Rect(WIDTH//2 - 100, 300, 200, 50)
        pygame.draw.rect(screen, (0, 255, 0), start_button)
        start_text = button_font.render("START", True, (0, 0, 0))
        screen.blit(start_text, (WIDTH//2 - start_text.get_width()//2, 310))
        
        # Draw quit button
        quit_button = pygame.Rect(WIDTH//2 - 100, 400, 200, 50)
        pygame.draw.rect(screen, (255, 0, 0), quit_button)
        quit_text = button_font.render("QUIT", True, (0, 0, 0))
        screen.blit(quit_text, (WIDTH//2 - quit_text.get_width()//2, 410))
        
        # Draw copyright text
        copyright_font = pygame.font.SysFont('comicsans', 16)
        copyright_text = copyright_font.render("Fan game - not affiliated with Disney/Lucasfilm", True, (150, 150, 150))
        screen.blit(copyright_text, (WIDTH//2 - copyright_text.get_width()//2, HEIGHT - 30))
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                
                # Check if start button is clicked
                if start_button.collidepoint(mouse_pos):
                    main_game()
                
                # Check if quit button is clicked
                if quit_button.collidepoint(mouse_pos):
                    running = False
                    pygame.quit()
                    sys.exit()
        
        pygame.display.update()

# Run the game
if __name__ == "__main__":
    main_menu()
