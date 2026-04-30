import pygame
import sys
from game import Game
from config import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
clock = pygame.time.Clock()

game = Game()

running = True

while running:
    clock.tick(game.speed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.snake.direction = UP
            elif event.key == pygame.K_DOWN:
                game.snake.direction = DOWN
            elif event.key == pygame.K_LEFT:
                game.snake.direction = LEFT
            elif event.key == pygame.K_RIGHT:
                game.snake.direction = RIGHT

    game.update()
    game.draw(screen)

    pygame.display.update()

    if game.game_over:
        running = False



pygame.quit()
sys.exit()