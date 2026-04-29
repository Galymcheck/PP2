import pygame

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3


class Snake:
    def __init__(self):
        # list of snake body segments (each segment is (x, y))
        self.snake = [
            (200, 200),
            (210, 200),
            (220, 200),
            (230, 200)
        ]

        # body segment
        self.skin = pygame.Surface((10, 10))
        self.skin.fill((255, 255, 255))

        # head
        self.head = pygame.Surface((10, 10))
        self.head.fill((180, 180, 180))

        self.direction = RIGHT

    def crawl(self):
        head_x, head_y = self.snake[-1]  # get current head position

        # move head
        if self.direction == RIGHT:
            new_head = (head_x + 10, head_y)
        elif self.direction == LEFT:
            new_head = (head_x - 10, head_y)
        elif self.direction == UP:
            new_head = (head_x, head_y - 10)
        elif self.direction == DOWN:
            new_head = (head_x, head_y + 10)

        self.snake.append(new_head)  # add new head to snake body
        self.snake.pop(0)            # remove tail (to keep length same)


    def self_collision(self):
        return self.snake[-1] in self.snake[:-1]

    def wall_collision(self, screen_size):
        x, y = self.snake[-1]

        return x < 0 or y < 0 or x >= screen_size or y >= screen_size

    def snake_eat_apple(self, apple_pos):
        return self.snake[-1] == apple_pos

    def snake_bigger(self):
        # add segment to tail
        self.snake.insert(0, self.snake[0])