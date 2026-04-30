import pygame
import math

def draw_rect(screen, color, start, end, thickness):
    x1, y1 = start
    x2, y2 = end
    pygame.draw.rect(
        screen,
        color,
        pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1)),
        thickness
    )

def draw_circle(screen, color, start, end, thickness):
    radius = int(math.hypot(end[0] - start[0], end[1] - start[1]))
    pygame.draw.circle(screen, color, start, radius, thickness)

def draw_square(screen, color, start, end, thickness):
    x1, y1 = start
    x2, y2 = end
    size = max(abs(x2 - x1), abs(y2 - y1))
    pygame.draw.rect(screen, color, pygame.Rect(x1, y1, size, size), thickness)

def draw_right_triangle(screen, color, start, end, thickness):
    x1, y1 = start
    x2, y2 = end
    pygame.draw.polygon(screen, color, [(x1, y1), (x1, y2), (x2, y2)], thickness)

def draw_equilateral_triangle(screen, color, start, end, thickness):
    x1, y1 = start
    x2, y2 = end

    side = abs(x2 - x1)
    height = int(side * math.sqrt(3) / 2)

    base_y = max(y1, y2)
    center_x = x1 + side // 2

    pygame.draw.polygon(screen, color, [
        (x1, base_y),
        (x1 + side, base_y),
        (center_x, base_y - height)
    ], thickness)

def draw_rhombus(screen, color, start, end, thickness):
    x1, y1 = start
    x2, y2 = end

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    pygame.draw.polygon(screen, color, [
        (x1, y1 - dy),
        (x1 + dx, y1),
        (x1, y1 + dy),
        (x1 - dx, y1)
    ], thickness)