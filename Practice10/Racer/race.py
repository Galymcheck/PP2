import pygame
import random
from pygame.locals import *

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("C:/Users/Galam/OneDrive/Документы/VScodes/repositories/PP2/Practice10/Racer/sources/Enemy.png")
        self.rect = self.image.get_rect()  #reate a rectangle of the same size as the image
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
      def move(self, speed):
        self.rect.move_ip(0, speed)   # Move enemy downward by SPEED pixels
        if (self.rect.top > 600):    # If enemy leaves screen from bottom
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            return True
        return False

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Load coin image
        self.image = pygame.image.load(
            "C:/Users/Galam/OneDrive/Документы/VScodes/repositories/PP2/Practice10/Racer/sources/Game-Coins-Gold-Coin-Sprite-524.png"
        )
        self.image = pygame.transform.scale(self.image, (45, 45))
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        # Random new position for coin
        self.rect.center = (
            random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self, speed):
        # Move coin downward
        self.rect.move_ip(0, speed)

        # If coin leaves screen → respawn
        if self.rect.top > SCREEN_HEIGHT:
            self.reset()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("C:/Users/Galam/OneDrive/Документы/VScodes/repositories/PP2/Practice10/Racer/sources/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:  #ensure that the player isn’t able to move off screen.
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)