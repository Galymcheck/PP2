import pygame
import sys
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint App")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)

current_color = BLACK

tool = "PENCIL"
drawing = False
start_pos = (0, 0)

points = []

brush_size = 5
eraser_size = 20

btn_plus = pygame.Rect(10, 5, 30, 25)
btn_minus = pygame.Rect(50, 5, 30, 25)
btn_pencil = pygame.Rect(100, 5, 70, 25)
btn_rect   = pygame.Rect(180, 5, 80, 25)
btn_circle = pygame.Rect(270, 5, 80, 25)
btn_eraser = pygame.Rect(360, 5, 80, 25)

font = pygame.font.SysFont("Arial", 16)

screen.fill(WHITE)

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos  # get mouse position

            if btn_plus.collidepoint(pos):
                brush_size += 1
                eraser_size += 2

            elif btn_minus.collidepoint(pos):
                brush_size = max(1, brush_size - 1)
                eraser_size = max(5, eraser_size - 2)

            elif btn_pencil.collidepoint(pos):
                tool = "PENCIL"

            elif btn_rect.collidepoint(pos):
                tool = "RECT"

            elif btn_circle.collidepoint(pos):
                tool = "CIRCLE"

            elif btn_eraser.collidepoint(pos):
                tool = "ERASER"

            else:
                drawing = True
                start_pos = pos
                points = [pos]

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos  # final mouse position

            if tool == "RECT":
                pygame.draw.rect(
                    screen,
                    current_color,
                    pygame.Rect(
                        start_pos[0],
                        start_pos[1],
                        end_pos[0] - start_pos[0],
                        end_pos[1] - start_pos[1]
                    ),
                    2
                )

            elif tool == "CIRCLE":
                radius = int(math.hypot(
                    end_pos[0] - start_pos[0],
                    end_pos[1] - start_pos[1]
                ))
                pygame.draw.circle(screen, current_color, start_pos, radius, 2)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                 current_color = (255, 0, 0)      # Red

            elif event.key == pygame.K_g:
                current_color = (0, 255, 0)      # Green

            elif event.key == pygame.K_b:
                current_color = (0, 0, 255)      # Blue

            elif event.key == pygame.K_v:
                current_color = (0, 0, 0)        # Black

            
    if drawing:
        if tool == "PENCIL":
            pos = pygame.mouse.get_pos()  # current mouse position
            points.append(pos)            # store position

            if len(points) > 1:
                 pygame.draw.circle(screen, current_color, pos, brush_size)

        elif tool == "ERASER":
            pygame.draw.circle(screen, WHITE, pygame.mouse.get_pos(), eraser_size)

    pygame.draw.rect(screen, (200, 200, 200), (0, 0, WIDTH, 35))
    pygame.draw.rect(screen, (150, 150, 150), btn_plus)
    pygame.draw.rect(screen, (150, 150, 150), btn_minus)
    pygame.draw.rect(screen, (180, 180, 180), btn_pencil)
    pygame.draw.rect(screen, (180, 180, 180), btn_rect)
    pygame.draw.rect(screen, (180, 180, 180), btn_circle)
    pygame.draw.rect(screen, (180, 180, 180), btn_eraser)

    screen.blit(font.render("+", True, BLACK), (18, 5))
    screen.blit(font.render("-", True, BLACK), (58, 5))
    screen.blit(font.render("Pen", True, BLACK), (110, 7))
    screen.blit(font.render("Rect", True, BLACK), (195, 7))
    screen.blit(font.render("Circle", True, BLACK), (280, 7))
    screen.blit(font.render("Eraser", True, BLACK), (370, 7))

    info = font.render(
        f"Tool: {tool} | Brush: {brush_size} | Eraser: {eraser_size}",
        True,
        BLACK
    )
    screen.blit(info, (460, 7))

    pygame.display.update()
    clock.tick(60)