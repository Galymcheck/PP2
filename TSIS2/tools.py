import pygame  # import pygame for drawing shapes
import math  # import math for geometry calculations (circle, triangle height)

def draw_rect(screen, color, start, end, thickness):  # function to draw rectangle
    x1, y1 = start  # unpack starting coordinates
    x2, y2 = end  # unpack ending coordinates
    pygame.draw.rect(  # draw rectangle on screen
        screen,  # target surface
        color,  # color of rectangle
        pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1)),  # normalized rectangle
        thickness  # border thickness
    )

def draw_circle(screen, color, start, end, thickness):  # function to draw circle
    radius = int(math.hypot(end[0] - start[0], end[1] - start[1]))  # calculate radius using distance formula
    pygame.draw.circle(screen, color, start, radius, thickness)  # draw circle from start point

def draw_square(screen, color, start, end, thickness):  # function to draw square
    x1, y1 = start  # starting point
    x2, y2 = end  # ending point
    size = max(abs(x2 - x1), abs(y2 - y1))  # ensure equal sides for square
    pygame.draw.rect(screen, color, pygame.Rect(x1, y1, size, size), thickness)  # draw square

def draw_right_triangle(screen, color, start, end, thickness):  # right triangle function
    x1, y1 = start  # start point
    x2, y2 = end  # end point
    pygame.draw.polygon(screen, color, [(x1, y1), (x1, y2), (x2, y2)], thickness)  # draw triangle

def draw_equilateral_triangle(screen, color, start, end, thickness):  # equilateral triangle function
    x1, y1 = start  # start coordinates
    x2, y2 = end  # end coordinates

    side = abs(x2 - x1)  # calculate side length
    height = int(side * math.sqrt(3) / 2)  # calculate triangle height

    base_y = max(y1, y2)  # base position (bottom)
    center_x = x1 + side // 2  # center of triangle

    pygame.draw.polygon(screen, color, [  # draw triangle shape
        (x1, base_y),
        (x1 + side, base_y),
        (center_x, base_y - height)
    ], thickness)

def draw_rhombus(screen, color, start, end, thickness):  # rhombus drawing function
    x1, y1 = start  # start point
    x2, y2 = end  # end point

    dx = abs(x2 - x1)  # horizontal distance
    dy = abs(y2 - y1)  # vertical distance

    pygame.draw.polygon(screen, color, [  # draw diamond shape
        (x1, y1 - dy),
        (x1 + dx, y1),
        (x1, y1 + dy),
        (x1 - dx, y1)
    ], thickness)