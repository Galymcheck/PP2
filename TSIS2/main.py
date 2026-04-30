import pygame
import sys
import tools
from datetime import datetime

pygame.init()

WIDTH, HEIGHT = 1200, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint App")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

current_color = BLACK
tool = "PENCIL"

drawing = False
start_pos = (0, 0)

stroke_size = 5
eraser_size = 20

canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(WHITE)

font = pygame.font.SysFont("Arial", 16)
text_font = pygame.font.SysFont("Arial", 24)

# TEXT TOOL STATE
text_mode = False
text_pos = (0, 0)
typed_text = ""

# UI
btn_pencil = pygame.Rect(90, 5, 80, 25)
btn_line = pygame.Rect(180, 5, 80, 25)
btn_eraser = pygame.Rect(270, 5, 80, 25)
btn_circle = pygame.Rect(360, 5, 80, 25)
btn_rect = pygame.Rect(450, 5, 80, 25)
btn_square = pygame.Rect(540, 5, 80, 25)
btn_rtri = pygame.Rect(630, 5, 80, 25)
btn_eqtri = pygame.Rect(720, 5, 80, 25)
btn_rhomb = pygame.Rect(810, 5, 80, 25)
btn_text = pygame.Rect(10, 5, 70, 25)

def get_btn_color(name, tool):
    return (255, 255, 0) if name == tool else (180, 180, 180)


while True:
    screen.fill(WHITE)
    screen.blit(canvas, (0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # ---------------- TEXT TOOL INPUT ----------------
        if text_mode:

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    text_mode = False
                    typed_text = ""

                elif event.key == pygame.K_RETURN:
                    canvas.blit(text_font.render(typed_text, True, current_color), text_pos)
                    text_mode = False
                    typed_text = ""

                elif event.key == pygame.K_BACKSPACE:
                    typed_text = typed_text[:-1]

                else:
                    typed_text += event.unicode

            continue  # блокируем рисование пока вводим текст

        # ---------------- MOUSE ----------------
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos

            if btn_text.collidepoint(pos):
                tool = "TEXT"
            elif btn_pencil.collidepoint(pos):
                tool = "PENCIL"
            elif btn_line.collidepoint(pos):
                tool = "LINE"
            elif btn_eraser.collidepoint(pos):
                tool = "ERASER"
            elif btn_circle.collidepoint(pos):
                tool = "CIRCLE"
            elif btn_rect.collidepoint(pos):
                tool = "RECT"
            elif btn_square.collidepoint(pos):
                tool = "SQUARE"
            elif btn_rtri.collidepoint(pos):
                tool = "RIGHT_TRI"
            elif btn_eqtri.collidepoint(pos):
                tool = "EQUIL_TRI"
            elif btn_rhomb.collidepoint(pos):
                tool = "RHOMBUS"

            # TEXT PLACE
            if tool == "TEXT":
                text_mode = True
                text_pos = pos
                typed_text = ""
                continue

            drawing = True
            start_pos = pos

        if event.type == pygame.MOUSEBUTTONUP:
            if not drawing:
                continue

            drawing = False
            end_pos = event.pos

            if tool == "LINE":
                pygame.draw.line(canvas, current_color, start_pos, end_pos, stroke_size)

            elif tool == "RECT":
                tools.draw_rect(canvas, current_color, start_pos, end_pos, stroke_size)

            elif tool == "CIRCLE":
                tools.draw_circle(canvas, current_color, start_pos, end_pos, stroke_size)

            elif tool == "SQUARE":
                tools.draw_square(canvas, current_color, start_pos, end_pos, stroke_size)

            elif tool == "RIGHT_TRI":
                tools.draw_right_triangle(canvas, current_color, start_pos, end_pos, stroke_size)

            elif tool == "EQUIL_TRI":
                tools.draw_equilateral_triangle(canvas, current_color, start_pos, end_pos, stroke_size)

            elif tool == "RHOMBUS":
                tools.draw_rhombus(canvas, current_color, start_pos, end_pos, stroke_size)

        # COLORS
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_1:
                stroke_size = 2
            elif event.key == pygame.K_2:
                stroke_size = 5
            elif event.key == pygame.K_3:
                stroke_size = 10

            elif event.key == pygame.K_r:
                current_color = RED
            elif event.key == pygame.K_g:
                current_color = GREEN
            elif event.key == pygame.K_b:
                current_color = BLUE
            elif event.key == pygame.K_v:
                current_color = BLACK

    # ---------------- DRAW LIVE ----------------
    if drawing:
        pos = pygame.mouse.get_pos()

        if tool == "PENCIL":
            pygame.draw.circle(canvas, current_color, pos, stroke_size)

        elif tool == "ERASER":
            pygame.draw.circle(canvas, WHITE, pos, eraser_size)

        elif tool == "LINE":
            pygame.draw.line(screen, current_color, start_pos, pos, stroke_size)

    # ---------------- TEXT PREVIEW ----------------
    if text_mode:
        preview = text_font.render(typed_text, True, current_color)
        screen.blit(preview, text_pos)

    # ---------------- UI ----------------
    pygame.draw.rect(screen, (200, 200, 200), (0, 0, WIDTH, 35))

    pygame.draw.rect(screen, get_btn_color("TEXT", tool), btn_text)
    pygame.draw.rect(screen, get_btn_color("PENCIL", tool), btn_pencil)
    pygame.draw.rect(screen, get_btn_color("LINE", tool), btn_line)
    pygame.draw.rect(screen, get_btn_color("ERASER", tool), btn_eraser)
    pygame.draw.rect(screen, get_btn_color("CIRCLE", tool), btn_circle)
    pygame.draw.rect(screen, get_btn_color("RECT", tool), btn_rect)
    pygame.draw.rect(screen, get_btn_color("SQUARE", tool), btn_square)
    pygame.draw.rect(screen, get_btn_color("RIGHT_TRI", tool), btn_rtri)
    pygame.draw.rect(screen, get_btn_color("EQUIL_TRI", tool), btn_eqtri)
    pygame.draw.rect(screen, get_btn_color("RHOMBUS", tool), btn_rhomb)

    screen.blit(font.render("TEXT", True, BLACK), (15, 7))
    screen.blit(font.render("Pen", True, BLACK), (110, 7))
    screen.blit(font.render("Line", True, BLACK), (195, 7))
    screen.blit(font.render("Eraser", True, BLACK), (280, 7))
    screen.blit(font.render("Circle", True, BLACK), (370, 7))
    screen.blit(font.render("Rect", True, BLACK), (455, 7))
    screen.blit(font.render("Square", True, BLACK), (550, 7))
    screen.blit(font.render("Right-Tri", True, BLACK), (640, 7))
    screen.blit(font.render("Equil-Tri", True, BLACK), (730, 7))
    screen.blit(font.render("Rhomb", True, BLACK), (820, 7))

    info = font.render(f"Tool: {tool} | Stroke: {stroke_size}", True, BLACK)
    screen.blit(info, (900, 7))

    pygame.display.update()
    clock.tick(60)