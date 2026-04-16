import pygame
import datetime

class MickeyClock:
    def __init__(self, screen, center):  #store the screen and center so we can use them later.
        self.screen = screen
        self.center = center
        self.hand_image = pygame.image.load("C:/Users/Galam/OneDrive/Документы/VScodes/repositories/PP2/Practice9/mickeys_clock/images/f641q88402u59sd16lso2ka5o3-92eb8eed57f277b6df8b8c3efea63ed1.png").convert_alpha()
        self.bg = pygame.image.load("C:/Users/Galam/OneDrive/Документы/VScodes/repositories/PP2/Practice9/mickeys_clock/images/mickeyclock.jpeg").convert_alpha()
        self.bg = pygame.transform.scale(self.bg, (800, 600))  

    def draw_hand(self, angle):
        rotated = pygame.transform.rotate(self.hand_image, -angle) #negative = clockwise

        rect = rotated.get_rect(center=self.center)   #Creates a rectangle around the image to keep rotating around the correct point
        self.screen.blit(rotated, rect)               #Draws the image on the screen

    def update(self):
        now = datetime.datetime.now()

        seconds = now.second
        minutes = now.minute
        #extract and convert into angles
        sec_angle = seconds * 6
        min_angle = minutes * 6
        
        rect = self.bg.get_rect(center=self.center)
        self.screen.blit(self.bg, rect)

        self.draw_hand(sec_angle)   #draw the clock hands in the correct positions
        self.draw_hand(min_angle)   