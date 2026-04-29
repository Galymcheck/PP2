import pygame
from pygame.locals import *
import sys
from snake_end import Snake
from apple_end import Apple

pygame.init()

SCREEN_SIZE = 400
FPS_BASE = 7

screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
clock = pygame.time.Clock()  # clock object to control game speed

snake = Snake()
apple = Apple()
apple.set_random_position(SCREEN_SIZE, snake.snake) # place apple at random position not on snake

SCORE = 0
LEVEL = 1
SPEED = FPS_BASE

font = pygame.font.SysFont("Verdana", 20)

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

GAME_ON = True

while GAME_ON:
    clock.tick(SPEED)
    snake.crawl()
    for event in pygame.event.get():
        if event.type == QUIT:
            GAME_ON = False

        if event.type == KEYDOWN:
            if event.key == K_UP and snake.direction != DOWN:  #prevent reverse
                snake.direction = UP
            elif event.key == K_DOWN and snake.direction != UP:
                snake.direction = DOWN
            elif event.key == K_LEFT and snake.direction != RIGHT:
                snake.direction = LEFT
            elif event.key == K_RIGHT and snake.direction != LEFT:
                snake.direction = RIGHT


    # wall collision
    if snake.wall_collision(SCREEN_SIZE) or snake.self_collision():
        GAME_ON = False

    # apple collision
    if snake.snake_eat_apple(apple.position):
        snake.snake_bigger()
        SCORE += apple.value

        # spawn new apple NOT on snake
        apple.set_random_position(SCREEN_SIZE, snake.snake)

        LEVEL = SCORE // 5 + 1
        SPEED = FPS_BASE + (LEVEL - 1) * 2.5
    
    screen.fill((0, 0, 0))
    
    food_time = apple.get_time_left()
    # if timer ends → respawn apple
    if food_time == 0:
        apple.set_random_position(SCREEN_SIZE, snake.snake)
    if apple.get_time_left() == 0:
        apple.set_random_position(SCREEN_SIZE, snake.snake)
    
    # draw snake body (all parts except head)
    for pos in snake.snake[:-1]:
        screen.blit(snake.skin, pos)
    # draw snake head
    screen.blit(snake.head, snake.snake[-1])

    # draw apple
    screen.blit(apple.apple, apple.position)

    # score + level UI
    food_time = apple.get_time_left()
    timer_text = font.render(f"Apple: {food_time}", True, (255, 255, 255))
    score_text = font.render(f"Score: {SCORE}", True, (255, 255, 255))
    level_text = font.render(f"Level: {LEVEL}", True, (255, 255, 255))

    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 30))
    screen.blit(timer_text, (300, 10))

    pygame.display.update()

pygame.quit()
sys.exit()