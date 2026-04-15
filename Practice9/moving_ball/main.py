import pygame
from ball import Ball

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

clock = pygame.time.Clock()

ball = Ball(WIDTH // 2, HEIGHT // 2)

running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ball.move(-ball.step, 0, WIDTH, HEIGHT)   #move left by 20 pixels and no vertical movement
            elif event.key == pygame.K_RIGHT:
                ball.move(ball.step, 0, WIDTH, HEIGHT)
            elif event.key == pygame.K_UP:
                ball.move(0, -ball.step, WIDTH, HEIGHT)
            elif event.key == pygame.K_DOWN:
                ball.move(0, ball.step, WIDTH, HEIGHT)

    ball.draw(screen)    #Draw the ball at its new position

    pygame.display.flip()
    clock.tick(60)

pygame.quit()