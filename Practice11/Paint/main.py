import pygame              # import pygame library
import sys                 # system exit
import math                # math for geometry (circles, triangles)

pygame.init()             # initialize pygame


WIDTH, HEIGHT = 1200, 600
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
btn_eraser   = pygame.Rect(180, 5, 80, 25)
btn_circle = pygame.Rect(270, 5, 80, 25)
btn_rect = pygame.Rect(360, 5, 80, 25)

# NEW SHAPES BUTTONS
btn_square = pygame.Rect(450, 5, 80, 25)
btn_rtri   = pygame.Rect(540, 5, 80, 25)
btn_eqtri  = pygame.Rect(630, 5, 90, 25)
btn_rhomb  = pygame.Rect(730, 5, 80, 25)

font = pygame.font.SysFont("Arial", 16)

screen.fill(WHITE)


while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            is_ui = (
                btn_plus.collidepoint(pos) or
                btn_minus.collidepoint(pos) or
                btn_pencil.collidepoint(pos) or
                btn_eraser.collidepoint(pos) or
                btn_circle.collidepoint(pos) or
                btn_rect.collidepoint(pos) or
                btn_square.collidepoint(pos) or
                btn_rtri.collidepoint(pos) or
                btn_eqtri.collidepoint(pos) or
                btn_rhomb.collidepoint(pos)
            )
            if is_ui:
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

                elif btn_square.collidepoint(pos):
                    tool = "SQUARE"

                elif btn_rtri.collidepoint(pos):
                    tool = "RIGHT_TRI"

                elif btn_eqtri.collidepoint(pos):
                    tool = "EQUIL_TRI"

                elif btn_rhomb.collidepoint(pos):
                    tool = "RHOMBUS"
                drawing = False
                continue

            drawing = True
            start_pos = pos

        if event.type == pygame.MOUSEBUTTONUP:
            

            drawing = False
            end_pos = event.pos

            if tool == "RECT":
                pygame.draw.rect(
                    screen,
                    current_color,
                    pygame.Rect(start_pos[0], start_pos[1],
                                end_pos[0]-start_pos[0],
                                end_pos[1]-start_pos[1]),
                    2
                )

            elif tool == "CIRCLE":
                radius = int(math.hypot(
                    end_pos[0]-start_pos[0],
                    end_pos[1]-start_pos[1]
                ))
                pygame.draw.circle(screen, current_color, start_pos, radius, 2)

            elif tool == "SQUARE":
                size = max(abs(end_pos[0]-start_pos[0]),
                           abs(end_pos[1]-start_pos[1]))
                pygame.draw.rect(
                    screen,
                    current_color,
                    pygame.Rect(start_pos[0], start_pos[1], size, size),
                    2
                )

            elif tool == "RIGHT_TRI":
                pygame.draw.polygon(screen, current_color, [
                    start_pos,
                    (start_pos[0], end_pos[1]),
                    end_pos
                ], 2)

            elif tool == "EQUIL_TRI":
                x1, y1 = start_pos
                x2, y2 = end_pos

                side = abs(x2 - x1)
                height = int(side * math.sqrt(3) / 2)

                base_y = max(y1, y2)
                center_x = x1 + side // 2

                pygame.draw.polygon(screen, current_color, [
                    (x1, base_y),
                    (x1 + side, base_y),
                    (center_x, base_y - height)
                ], 2)

            elif tool == "RHOMBUS":
                dx = abs(end_pos[0] - start_pos[0])
                dy = abs(end_pos[1] - start_pos[1])

                pygame.draw.polygon(screen, current_color, [
                    (start_pos[0], start_pos[1] - dy),
                    (start_pos[0] + dx, start_pos[1]),
                    (start_pos[0], start_pos[1] + dy),
                    (start_pos[0] - dx, start_pos[1])
                ], 2)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                current_color = RED
            elif event.key == pygame.K_g:
                current_color = GREEN
            elif event.key == pygame.K_b:
                current_color = BLUE
            elif event.key == pygame.K_v:
                current_color = BLACK


    if drawing:
        if tool == "PENCIL":
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(screen, current_color, pos, brush_size)

        elif tool == "ERASER":
            pygame.draw.circle(screen, WHITE, pygame.mouse.get_pos(), eraser_size)


    pygame.draw.rect(screen, (200, 200, 200), (0, 0, WIDTH, 35))

    pygame.draw.rect(screen, (150, 150, 150), btn_plus)
    pygame.draw.rect(screen, (150, 150, 150), btn_minus)

    pygame.draw.rect(screen, (180, 180, 180), btn_pencil)
    pygame.draw.rect(screen, (180, 180, 180), btn_eraser)
    pygame.draw.rect(screen, (180, 180, 180), btn_circle)
    pygame.draw.rect(screen, (180, 180, 180), btn_rect)

    pygame.draw.rect(screen, (180, 180, 180), btn_square)
    pygame.draw.rect(screen, (180, 180, 180), btn_rtri)
    pygame.draw.rect(screen, (180, 180, 180), btn_eqtri)
    pygame.draw.rect(screen, (180, 180, 180), btn_rhomb)

    # labels
    screen.blit(font.render("+", True, BLACK), (18, 5))
    screen.blit(font.render("-", True, BLACK), (58, 5))
    screen.blit(font.render("Pen", True, BLACK), (110, 7))
    screen.blit(font.render("Eraser", True, BLACK), (190, 7))
    screen.blit(font.render("Circle", True, BLACK), (280, 7))
    screen.blit(font.render("Rect", True, BLACK), (370, 7))

    screen.blit(font.render("Square", True, BLACK), (455, 7))
    screen.blit(font.render("Right-Tri", True, BLACK), (545, 7))
    screen.blit(font.render("Equil-Tri", True, BLACK), (635, 7))
    screen.blit(font.render("Rhomb", True, BLACK), (735, 7))

    # info
    info = font.render(
        f"Tool: {tool} | Brush: {brush_size} | Eraser: {eraser_size}",
        True,
        BLACK
    )
    screen.blit(info, (900, 7))

    pygame.display.update()
    clock.tick(60)