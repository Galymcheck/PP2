import pygame
import random
import time
from config import *

class Snake:
    def __init__(self, color):
        self.snake = [(200, 200), (210, 200), (220, 200)]
        self.direction = RIGHT

        self.skin = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.skin.fill(color)

        self.head = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.head.fill((180, 180, 180))

    def crawl(self, grow=False):
        x, y = self.snake[-1]

        if self.direction == RIGHT:
            new = (x + CELL_SIZE, y)
        elif self.direction == LEFT:
            new = (x - CELL_SIZE, y)
        elif self.direction == UP:
            new = (x, y - CELL_SIZE)
        else:
            new = (x, y + CELL_SIZE)

        self.snake.append(new)

        if not grow:
            self.snake.pop(0)

    def eat(self, pos):
        return self.snake[-1] == pos

    def collision(self, obstacles):
        x, y = self.snake[-1]

        # wall
        if x < 0 or y < 0 or x >= SCREEN_SIZE or y >= SCREEN_SIZE:
            return True

        # self
        if self.snake[-1] in self.snake[:-1]:
            return True

        # obstacles
        if self.snake[-1] in obstacles:
            return True

        return False


class Apple:
    def __init__(self):
        self.surface = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.pos = (0, 0)
        self.value = 1
        self.type = "normal"
        self.spawn_time = time.time()

    def spawn(self, snake_body, obstacles):
        while True:
            x = random.randrange(0, SCREEN_SIZE, CELL_SIZE)
            y = random.randrange(0, SCREEN_SIZE, CELL_SIZE)

            if (x, y) not in snake_body and (x, y) not in obstacles:
                self.pos = (x, y)
                break

        self.spawn_time = time.time()

        r = random.randint(1, 10)

        if r <= 6:
            self.surface.fill((255, 0, 0))
            self.value = 1
            self.type = "normal"
        elif r <= 9:
            self.surface.fill((0, 0, 255))
            self.value = 2
            self.type = "normal"
        else:
            self.surface.fill((80, 0, 0))
            self.value = -2
            self.type = "poison"

    def time_left(self):
        return max(0, 10 - int(time.time() - self.spawn_time))


class Game:
    def __init__(self, username, settings):
        self.snake = Snake(settings["snake_color"])
        self.apple = Apple()

        self.username = username
        self.settings = settings

        self.score = 0
        self.level = 1
        self.speed = FPS_BASE

        self.game_over = False

        self.obstacles = []

        self.apple.spawn(self.snake.snake, self.obstacles)

    # ================= OBSTACLES =================
    def generate_obstacles(self):
        self.obstacles = []

        # number grows with level
        count = 5 + self.level * 2

        safe_zone = self.snake.snake[-1]

        for _ in range(count):
            while True:
                x = random.randrange(0, SCREEN_SIZE, CELL_SIZE)
                y = random.randrange(0, SCREEN_SIZE, CELL_SIZE)

                pos = (x, y)

                # DON'T trap snake spawn area
                if pos not in self.snake.snake:
                    if abs(pos[0] - safe_zone[0]) > 40 or abs(pos[1] - safe_zone[1]) > 40:
                        self.obstacles.append(pos)
                        break

    # ================= UPDATE =================
    def update(self):
        grow = self.snake.eat(self.apple.pos)
        self.snake.crawl(grow)

        # apple
        if grow:
            if self.apple.type == "poison":
                for _ in range(2):
                    if len(self.snake.snake) > 1:
                        self.snake.snake.pop(0)
                if len(self.snake.snake) <= 1:
                    self.game_over = True
            else:
                self.score += self.apple.value

            # LEVEL SYSTEM
            self.level = self.score // 5 + 1
            self.speed = FPS_BASE + (self.level - 1) * 2

            # obstacles from level 3
            if self.level >= 3:
                self.generate_obstacles()

            self.apple.spawn(self.snake.snake, self.obstacles)

        # collisions
        if self.snake.collision(self.obstacles):
            self.game_over = True

        # apple timer
        if self.apple.time_left() == 0:
            self.apple.spawn(self.snake.snake, self.obstacles)

    # ================= DRAW =================
    def draw(self, screen):
        screen.fill((0, 0, 0))

        # grid
        if self.settings["grid"]:
            for x in range(0, SCREEN_SIZE, CELL_SIZE):
                pygame.draw.line(screen, (30, 30, 30), (x, 0), (x, SCREEN_SIZE))
            for y in range(0, SCREEN_SIZE, CELL_SIZE):
                pygame.draw.line(screen, (30, 30, 30), (0, y), (SCREEN_SIZE, y))

        # obstacles
        for o in self.obstacles:
            pygame.draw.rect(screen, (120, 120, 120), (*o, CELL_SIZE, CELL_SIZE))

        # snake
        for s in self.snake.snake[:-1]:
            screen.blit(self.snake.skin, s)

        screen.blit(self.snake.head, self.snake.snake[-1])

        # apple
        screen.blit(self.apple.surface, self.apple.pos)