import pygame
import random
from pygame.locals import *

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("C:/Users/Galam/OneDrive/Документы/VScodes/repositories/PP2/Practice11/Racer/sources/Enemy.png")
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

        # Load normal coin image
        self.normal_image = pygame.image.load(
            "C:/Users/Galam/OneDrive/Документы/VScodes/repositories/PP2/Practice11/Racer/sources/Game-Coins-Gold-Coin-Sprite-524.png"
        )
        self.normal_image = pygame.transform.scale(self.normal_image, (45, 45))

        # Load rare red coin image
        self.red_image = pygame.image.load(
            "C:/Users/Galam/OneDrive/Документы/VScodes/repositories/PP2/Practice11/Racer/sources/Game-RedCoins-Gold-Coin-Sprite-524.png"
        )
        self.red_image = pygame.transform.scale(self.red_image, (45, 45))

        self.image = self.normal_image
        self.rect = self.image.get_rect()

        self.value = 1  # default coin value

        self.reset()

    def reset(self):
        # Random position
        self.rect.center = (
            random.randint(40, SCREEN_WIDTH - 40), 0)

        # Small chance for rare red coin
        if random.randint(1, 5) == 1:   # 20% chance
            self.image = self.red_image
            self.value = 3
        else:
            self.image = self.normal_image
            self.value = 1

    def move(self, speed):
        self.rect.move_ip(0, speed)

        if self.rect.top > SCREEN_HEIGHT:
            self.reset()

            
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("C:/Users/Galam/OneDrive/Документы/VScodes/repositories/PP2/Practice11/Racer/sources/Player.png")
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