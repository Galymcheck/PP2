import pygame
import random
import time

class Apple:
    def __init__(self):
        # apple image
        self.apple = pygame.Surface((10, 10))

        self.position = (0, 0)
        self.value = 1

        # Time when food was created
        self.spawn_time = time.time()

    def set_random_position(self, screen_size, snake_body):
        while True:
            # random position aligned to grid
            x = random.randrange(0, screen_size, 10)
            y = random.randrange(0, screen_size, 10)

            # check if apple is NOT on snake
            if (x, y) not in snake_body:
                self.position = (x, y)
                break


        # reset timer EVERY time apple appears
        self.spawn_time = time.time()

        # random color + value
        r = random.randint(1, 10)

        if r <= 6:
            self.apple.fill((255, 0, 0))
            self.value = 1
        elif r <= 9:
            self.apple.fill((0, 0, 255))
            self.value = 2
        else:
            self.apple.fill((255, 255, 0))
            self.value = 3

    def get_time_left(self):
        # 10 seconds lifetime
        return max(0, 10 - int(time.time() - self.spawn_time))