# importing libraries
import pygame
import time
import random

snake_speed = 15

# Window size
window_x = 720
window_y = 480

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('snakes')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS controller
fps = pygame.time.Clock()

# defining snake default position
snake_position = [100, 50]

# defining first 4 blocks of snake body
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]

# ---------- ADDED: LEVEL SYSTEM ----------
level = 1
foods_eaten = 0

# ---------- ADDED: LEVEL UP EFFECT ----------
level_up_flag = False
level_up_time = 0

# ---------- ADDED: SAFE FOOD GENERATION ----------
def generate_food():
    # generate food not inside snake body
    while True:
        pos = [
            random.randrange(1, (window_x//10)) * 10,
            random.randrange(1, (window_y//10)) * 10
        ]
        if pos not in snake_body:
            return pos

# fruit position
fruit_position = generate_food()
fruit_spawn = True

# ---------- ADDED: SNAKE COLOR BY LEVEL ----------
def get_snake_color(level):
    if level == 1:
        return pygame.Color(0, 255, 0)
    elif level == 2:
        return pygame.Color(0, 200, 255)
    elif level == 3:
        return pygame.Color(255, 200, 0)
    else:
        return pygame.Color(255, 0, 0)

# setting default snake direction
direction = 'RIGHT'
change_to = direction

# initial score
score = 0

# displaying Score function
def show_score(choice, color, font, size):

    # creating font object
    score_font = pygame.font.SysFont(font, size)

    # add level to text
    score_surface = score_font.render(
        'Score : ' + str(score) + '  Level : ' + str(level),
        True, color
    )

    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

# game over function
def game_over():

    my_font = pygame.font.SysFont('times new roman', 50)

    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)

    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x/2, window_y/2)

    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    time.sleep(2)

    pygame.quit()
    quit()

# Main Function
while True:

    # handling key events
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

    # direction control
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_position))

    # ---------- MODIFIED: FOOD EATING ----------
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        foods_eaten += 1   # count foods for level
        fruit_spawn = False
    else:
        snake_body.pop()

    # ---------- ADDED: LEVEL UP ----------
    if foods_eaten == 3:
        level += 1
        snake_speed += 3   # increase speed
        foods_eaten = 0

        level_up_flag = True
        level_up_time = pygame.time.get_ticks()

    # spawn food safely
    if not fruit_spawn:
        fruit_position = generate_food()
        fruit_spawn = True

    game_window.fill(black)

    # ---------- MODIFIED: USE LEVEL COLOR ----------
    snake_color = get_snake_color(level)

    for pos in snake_body:
        pygame.draw.rect(game_window, snake_color,
                         pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))

    # Game Over conditions (border collision)
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()

    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # displaying score continuously
    show_score(1, white, 'times new roman', 20)

    # ---------- ADDED: LEVEL UP TEXT ----------
    if level_up_flag:
        current_time = pygame.time.get_ticks()

        # show message for 1 second
        if current_time - level_up_time < 1000:
            font = pygame.font.SysFont('times new roman', 40)
            text = font.render('LEVEL UP!', True, red)
            rect = text.get_rect(center=(window_x/2, window_y/2))
            game_window.blit(text, rect)
        else:
            level_up_flag = False

    pygame.display.update()

    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)