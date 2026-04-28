import pygame, sys
from pygame.locals import *
import random, time

# -------------------- INIT --------------------
pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

# Colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Game variables
SPEED = 5
SCORE = 0
COIN_SCORE = 0

# Speed boost threshold
NEXT_SPEED_BOOST = 5  # каждые 5 монет ускоряем врагов

# Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)

game_over = font.render("Game Over", True, BLACK)

# Background
background = pygame.image.load("AnimatedStreet.png")

# Music
pygame.mixer.music.load('background.wav')
pygame.mixer.music.play(-1)

# Screen
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Race Game")

# -------------------- ENEMY --------------------
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE, SPEED
        self.rect.move_ip(0, SPEED)

        # Respawn enemy
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# -------------------- PLAYER --------------------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        keys = pygame.key.get_pressed()

        if self.rect.left > 0 and keys[K_LEFT]:
            self.rect.move_ip(-5, 0)

        if self.rect.right < SCREEN_WIDTH and keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

# -------------------- COIN --------------------
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # ----- RANDOM WEIGHT (1–3) -----
        self.weight = random.randint(1, 3)

        # Load coin image
        original = pygame.image.load("coin.png").convert_alpha()

        # Different size depending on weight
        size = 20 + self.weight * 10   # 30, 40, 50 px
        self.image = pygame.transform.scale(original, (size, size))

        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)

        # Respawn coin
        if self.rect.top > SCREEN_HEIGHT:
            self.reset()

    def reset(self):
        self.weight = random.randint(1, 3)
        size = 20 + self.weight * 10

        original = pygame.image.load("coin.png").convert_alpha()
        self.image = pygame.transform.scale(original, (size, size))

        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# -------------------- OBJECTS --------------------
P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies = pygame.sprite.Group(E1)
coins = pygame.sprite.Group(C1)

all_sprites = pygame.sprite.Group(P1, E1, C1)

# Speed increase event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# -------------------- MAIN LOOP --------------------
while True:

    for event in pygame.event.get():

        # Increase speed over time
        if event.type == INC_SPEED:
            SPEED += 0.3

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Background
    DISPLAYSURF.blit(background, (0, 0))

    # UI
    score_text = font_small.render("Enemies: " + str(SCORE), True, BLACK)
    DISPLAYSURF.blit(score_text, (10, 10))

    coin_text = font_small.render("Coins: " + str(COIN_SCORE), True, BLACK)
    DISPLAYSURF.blit(coin_text, (SCREEN_WIDTH - 120, 10))

    # -------------------- SPRITES --------------------
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # -------------------- COIN COLLISION --------------------
    if pygame.sprite.spritecollideany(P1, coins):
        COIN_SCORE += C1.weight  # вес влияет на очки
        C1.reset()

        # Increase enemy speed every N coins
        if COIN_SCORE % NEXT_SPEED_BOOST == 0:
            SPEED += 1

    # -------------------- ENEMY COLLISION --------------------
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.music.stop()
        pygame.mixer.Sound('crash.wav').play()

        time.sleep(0.5)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()

        for entity in all_sprites:
            entity.kill()

        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)