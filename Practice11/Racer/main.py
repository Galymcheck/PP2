import pygame, sys
from pygame.locals import *
import random, time
from race import Player, Enemy, Coin

pygame.init()
 
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()  # clock object to control game speed
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0
LEVEL_CHECK = 0 
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load("C:/Users/Galam/OneDrive/Документы/VScodes/repositories/PP2/Practice11/Racer/sources/AnimatedStreet.png")
 
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
 

# Create player and enemy objects       
P1 = Player()
E1 = Enemy()
C1 = Coin()
enemies = pygame.sprite.Group()   # Create sprite group for enemies
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
 
#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1  #+1 to ensure that it will have a unique ID
pygame.time.set_timer(INC_SPEED, 1000)  #call event object every 1000 milliseconds
 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    DISPLAYSURF.blit(background, (0,0))
    score_text = font_small.render("Score: " + str(SCORE), True, BLACK)
    DISPLAYSURF.blit(score_text, (10, 10))

    coin_text = font_small.render("Coins: " + str(COINS), True, BLACK)
    DISPLAYSURF.blit(coin_text, (280, 10))
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)  # Draw sprite

        if isinstance(entity, Enemy):  # Enemy movement
            if entity.move(SPEED):     # If enemy passed screen
                SCORE += 1             # Increase score

        elif isinstance(entity, Player):  # Player movement
            entity.move()

        elif isinstance(entity, Coin):    # Coin movement
            entity.move(SPEED)

    
    if pygame.sprite.collide_rect(P1, C1):
        COINS += C1.value
        C1.reset()  # Move coin to new random position
    # Collision with coin → collect coin
      
    
    if COINS // 10 > LEVEL_CHECK:
        LEVEL_CHECK = COINS // 10
        SPEED += 1
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('C:/Users/Galam/OneDrive/Документы/VScodes/repositories/PP2/Practice11/Racer/sources/crash.wav').play()
          time.sleep(0.5)   # Small delay after crash sound
                    
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(1.5)
          pygame.quit()
          sys.exit()        
         
    pygame.display.update()   # Refresh game screen every frame
    FramePerSec.tick(FPS)     # Keep game running at fixed FPS