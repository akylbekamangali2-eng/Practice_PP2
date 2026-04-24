import pygame, sys
from pygame.locals import *
import random, time

# Initialize pygame
pygame.init()

# Frames per second
FPS = 60
FramePerSec = pygame.time.Clock()

# Colors (RGB)
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen settings
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Game variables
SPEED = 5
SCORE = 0
COIN_SCORE = 0

# Fonts for UI
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)

# Game over text surface
game_over = font.render("Game Over", True, BLACK)

# Load background image
background = pygame.image.load("AnimatedStreet.png")

# Load and play background music (loop forever)
pygame.mixer.music.load('background.wav') 
pygame.mixer.music.play(-1)

# Create game window
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("race")

# Enemy class (cars that player must avoid)
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        # Spawn enemy at random horizontal position at top
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        global SCORE
        # Move enemy downward
        self.rect.move_ip(0, SPEED)
        # If enemy leaves screen, reset position and increase score
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Player class (controlled by keyboard)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        # Initial position of player
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        # Move left (stay inside screen)
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        # Move right (stay inside screen)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

# Coin class (collectible objects)
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load and scale coin image
        original_image = pygame.image.load("coin.png").convert_alpha()
        self.image = pygame.transform.scale(original_image, (35, 35))
        
        self.rect = self.image.get_rect()
        # Spawn coin at random position at top
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def update(self):
        # Move coin downward
        self.rect.y += 5
        # Remove coin if it leaves screen
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

    def move(self):
        # Move coin with same speed as enemies
        self.rect.move_ip(0, SPEED)
        # Reset position if it leaves screen
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    
    def reset(self):
        # Reset coin after collecting
        self.rect.top = 0
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Create objects
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Groups for sprites
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Custom event to increase speed over time
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Main game loop
while True:
    for event in pygame.event.get():
        # Increase speed every second
        if event.type == INC_SPEED:
              SPEED += 0.5      
        # Exit game
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Draw background
    DISPLAYSURF.blit(background, (0,0))
    
    # Display enemy score
    scores = font_small.render("Enemies: " + str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))

    # Display coin score
    coin_text = font_small.render("Coins: " + str(COIN_SCORE), True, BLACK)
    DISPLAYSURF.blit(coin_text, (SCREEN_WIDTH - 100, 10))

    # Draw and update all sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Check collision with coin
    if pygame.sprite.spritecollideany(P1, coins):
        COIN_SCORE += 1
        C1.reset()

    # Check collision with enemy (game over)
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.music.stop()  # Stop background music
          pygame.mixer.Sound('crash.wav').play()  # Play crash sound
          time.sleep(0.5)
                   
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          
          pygame.display.update()
          # Remove all sprites
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
        
    pygame.display.update()
    FramePerSec.tick(FPS)