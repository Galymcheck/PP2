import pygame
from clock import MickeyClock

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()   #Creates a clock object to control how fast the program runs


mickey_clock = MickeyClock(screen, (600 // 2, 600 // 2))

while True:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    mickey_clock.update()    #Updates and draws the clock

    pygame.display.flip()    #Updates the screen
    clock.tick(1)            #Limits the loop to 1 time per second