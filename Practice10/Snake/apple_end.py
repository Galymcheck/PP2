import pygame
import random


class Apple:
    def __init__(self):
        # apple image
        self.apple = pygame.Surface((10, 10))
        self.apple.fill((255, 0, 0))

        self.position = (0, 0)

    def set_random_position(self, screen_size, snake_body):
        while True:
            # random position aligned to grid
            x = random.randrange(0, screen_size, 10)
            y = random.randrange(0, screen_size, 10)

            # check if apple is NOT on snake
            if (x, y) not in snake_body:
                self.position = (x, y)
                break