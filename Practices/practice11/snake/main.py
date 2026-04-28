import pygame
import time
import random

# ---------------- SETTINGS ----------------
snake_speed = 15

window_x = 720
window_y = 480

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

pygame.init()

pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((window_x, window_y))

fps = pygame.time.Clock()

# ---------------- SNAKE ----------------
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

direction = 'RIGHT'
change_to = direction

# ---------------- SCORE ----------------
score = 0

# ---------------- FOOD ----------------
food_position = [0, 0]
food_weight = 1
food_spawn_time = 0
FOOD_LIFETIME = 10000  # 10 seconds

def generate_food():
    return [
        random.randrange(1, (window_x // 10)) * 10,
        random.randrange(1, (window_y // 10)) * 10
    ]

def generate_food_weight():
    return random.randint(1, 3)

def get_food_color(weight):
    if weight == 1:
        return green
    elif weight == 2:
        return white
    else:
        return red

# first food spawn
food_position = generate_food()
food_weight = generate_food_weight()
food_spawn_time = pygame.time.get_ticks()

# ---------------- SCORE TEXT ----------------
def show_score():
    font = pygame.font.SysFont('times new roman', 20)
    text = font.render(f"Score: {score}", True, white)
    game_window.blit(text, (10, 10))

# ---------------- GAME OVER ----------------
def game_over():
    font = pygame.font.SysFont('times new roman', 50)
    text = font.render("Game Over", True, red)
    rect = text.get_rect(center=(window_x / 2, window_y / 2))

    game_window.blit(text, rect)
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    quit()

# ---------------- MAIN LOOP ----------------
while True:

    # controls
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # direction rules
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # move snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    snake_body.insert(0, list(snake_position))

    # ---------------- EAT FOOD ----------------
    if snake_position == food_position:
        score += food_weight * 10
        food_position = generate_food()
        food_weight = generate_food_weight()
        food_spawn_time = pygame.time.get_ticks()
    else:
        snake_body.pop()

    # ---------------- FOOD TIMER ----------------
    current_time = pygame.time.get_ticks()

    if current_time - food_spawn_time > FOOD_LIFETIME:
        food_position = generate_food()
        food_weight = generate_food_weight()
        food_spawn_time = current_time

    # ---------------- DRAW ----------------
    game_window.fill(black)

    # snake
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

    # food (same size always)
    food_color = get_food_color(food_weight)

    pygame.draw.rect(
        game_window,
        food_color,
        pygame.Rect(food_position[0], food_position[1], 10, 10)
    )

    # ---------------- COLLISION ----------------
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()

    for block in snake_body[1:]:
        if snake_position == block:
            game_over()

    # ---------------- UI ----------------
    show_score()

    pygame.display.update()
    fps.tick(snake_speed)