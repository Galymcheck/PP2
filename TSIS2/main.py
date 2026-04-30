import pygame  # import pygame library for graphics, input handling, and rendering
import sys  # import sys module to allow safe program exit using sys.exit()
import tools  # import custom module containing all shape drawing functions (rect, circle, etc.)
from datetime import datetime 
pygame.init()  # initialize all pygame modules (must be called before using pygame)

WIDTH, HEIGHT = 1200, 600  # set window width and height in pixels
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # create main display surface (window canvas)
pygame.display.set_caption("Paint App")  # set title of the application window

clock = pygame.time.Clock()  # create clock object to control FPS and timing

WHITE = (255, 255, 255)  # define RGB color white (used for background and eraser)
BLACK = (0, 0, 0)  # define black color for drawing
RED = (255, 0, 0)  # define red color
GREEN = (0, 255, 0)  # define green color
BLUE = (0, 0, 255)  # define blue color

current_color = BLACK  # current drawing color starts as black
tool = "PENCIL"  # default tool is pencil (free drawing mode)

drawing = False  # boolean flag indicating whether user is currently drawing
start_pos = (0, 0)  # stores starting mouse position for shapes

stroke_size = 5  # default thickness of drawing lines and shapes
eraser_size = 40  # size of eraser brush (white circle)

canvas = pygame.Surface((WIDTH, HEIGHT))  # separate surface used as permanent drawing layer
canvas.fill(WHITE)  # fill canvas with white background like blank paper
# NEW: save function
def save_canvas():
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"drawing_{now}.png"
    pygame.image.save(canvas, filename)
    print("Saved:", filename)

font = pygame.font.SysFont("Arial", 16)  # small font for UI labels and buttons
text_font = pygame.font.SysFont("Arial", 24)  # larger font used for text tool rendering

text_mode = False  # indicates whether text input mode is active
text_pos = (0, 0)  # position where typed text will be placed on canvas
typed_text = ""  # stores current text being typed by user

btn_pencil = pygame.Rect(90, 5, 80, 25)  # pencil tool button area
btn_line = pygame.Rect(180, 5, 80, 25)  # line tool button area
btn_eraser = pygame.Rect(270, 5, 80, 25)  # eraser tool button area
btn_circle = pygame.Rect(360, 5, 80, 25)  # circle tool button area
btn_rect = pygame.Rect(450, 5, 80, 25)  # rectangle tool button area
btn_square = pygame.Rect(540, 5, 80, 25)  # square tool button area
btn_rtri = pygame.Rect(630, 5, 80, 25)  # right triangle tool button area
btn_eqtri = pygame.Rect(720, 5, 80, 25)  # equilateral triangle tool button area
btn_rhomb = pygame.Rect(810, 5, 80, 25)  # rhombus tool button area
btn_text = pygame.Rect(10, 5, 70, 25)  # text tool button area

def get_btn_color(name, tool):  # function that returns button color depending on selected tool
    return (255, 255, 0) if name == tool else (180, 180, 180)  # yellow if active tool, gray otherwise

while True:  # main infinite game loop
    screen.fill(WHITE)  # clear screen every frame (reset visual display)
    screen.blit(canvas, (0, 0))  # draw permanent canvas layer onto screen

    for event in pygame.event.get():  # loop through all user input events

        if event.type == pygame.QUIT:  # check if window close button is pressed
            pygame.quit()  # shut down pygame safely
            sys.exit()  # exit Python program completely

        if text_mode:  # if text input mode is active

            if event.type == pygame.KEYDOWN:  # handle keyboard input for text tool

                if event.key == pygame.K_ESCAPE:  # cancel text input
                    text_mode = False  # exit text mode
                    typed_text = ""  # clear typed text

                elif event.key == pygame.K_RETURN:  # confirm and place text
                    canvas.blit(text_font.render(typed_text, True, current_color), text_pos)  # render text onto canvas
                    text_mode = False  # exit text mode
                    typed_text = ""  # reset text buffer

                elif event.key == pygame.K_BACKSPACE:  # remove last character
                    typed_text = typed_text[:-1]  # delete last symbol

                else:  # any other key input
                    typed_text += event.unicode  # append character to text string

            continue  # skip rest of loop while typing text

        if event.type == pygame.MOUSEBUTTONDOWN:  # detect mouse click start
            pos = event.pos  # get mouse click position

            if btn_text.collidepoint(pos):  # check if text tool selected
                tool = "TEXT"
            elif btn_pencil.collidepoint(pos):  # pencil tool selected
                tool = "PENCIL"
            elif btn_line.collidepoint(pos):  # line tool selected
                tool = "LINE"
            elif btn_eraser.collidepoint(pos):  # eraser tool selected
                tool = "ERASER"
            elif btn_circle.collidepoint(pos):  # circle tool selected
                tool = "CIRCLE"
            elif btn_rect.collidepoint(pos):  # rectangle tool selected
                tool = "RECT"
            elif btn_square.collidepoint(pos):  # square tool selected
                tool = "SQUARE"
            elif btn_rtri.collidepoint(pos):  # right triangle tool selected
                tool = "RIGHT_TRI"
            elif btn_eqtri.collidepoint(pos):  # equilateral triangle tool selected
                tool = "EQUIL_TRI"
            elif btn_rhomb.collidepoint(pos):  # rhombus tool selected
                tool = "RHOMBUS"

            if tool == "TEXT":  # if text tool activated
                text_mode = True  # enable typing mode
                text_pos = pos  # store text position
                typed_text = ""  # reset current text
                continue  # skip drawing start

            drawing = True  # start drawing state
            start_pos = pos  # store starting mouse position

        if event.type == pygame.MOUSEBUTTONUP:  # detect mouse release
            if not drawing:  # if not drawing, ignore
                continue

            drawing = False  # stop drawing state
            end_pos = event.pos  # store ending position

            if tool == "LINE":  # draw line tool
                pygame.draw.line(canvas, current_color, start_pos, end_pos, stroke_size)

            elif tool == "RECT":  # draw rectangle
                tools.draw_rect(canvas, current_color, start_pos, end_pos, stroke_size)

            elif tool == "CIRCLE":  # draw circle
                tools.draw_circle(canvas, current_color, start_pos, end_pos, stroke_size)

            elif tool == "SQUARE":  # draw square
                tools.draw_square(canvas, current_color, start_pos, end_pos, stroke_size)

            elif tool == "RIGHT_TRI":  # draw right triangle
                tools.draw_right_triangle(canvas, current_color, start_pos, end_pos, stroke_size)

            elif tool == "EQUIL_TRI":  # draw equilateral triangle
                tools.draw_equilateral_triangle(canvas, current_color, start_pos, end_pos, stroke_size)

            elif tool == "RHOMBUS":  # draw rhombus
                tools.draw_rhombus(canvas, current_color, start_pos, end_pos, stroke_size)

        if event.type == pygame.KEYDOWN:  # handle keyboard input for settings
            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                save_canvas()
            elif event.key == pygame.K_1:  # small stroke size
                stroke_size = 2
            elif event.key == pygame.K_2:  # medium stroke size
                stroke_size = 5
            elif event.key == pygame.K_3:  # large stroke size
                stroke_size = 10

            elif event.key == pygame.K_r:  # switch to red color
                current_color = RED
            elif event.key == pygame.K_g:  # switch to green color
                current_color = GREEN
            elif event.key == pygame.K_b:  # switch to blue color
                current_color = BLUE
            elif event.key == pygame.K_v:  # switch back to black
                current_color = BLACK

    if drawing:  # live drawing while mouse is held
        pos = pygame.mouse.get_pos()  # current mouse position

        if tool == "PENCIL":  # freehand drawing
            pygame.draw.circle(canvas, current_color, pos, stroke_size)

        elif tool == "ERASER":  # erase by drawing white circles
            pygame.draw.circle(canvas, WHITE, pos, eraser_size)

        elif tool == "LINE":  # preview line while dragging
            pygame.draw.line(screen, current_color, start_pos, pos, stroke_size)

    if text_mode:  # show text preview while typing
        screen.blit(text_font.render(typed_text, True, current_color), text_pos)

    pygame.draw.rect(screen, (200, 200, 200), (0, 0, WIDTH, 35))  # draw top UI bar

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

    screen.blit(font.render("TEXT", True, BLACK), (15, 7))  # text label
    screen.blit(font.render("Pen", True, BLACK), (110, 7))  # pencil label
    screen.blit(font.render("Line", True, BLACK), (195, 7))  # line label
    screen.blit(font.render("Eraser", True, BLACK), (280, 7))  # eraser label
    screen.blit(font.render("Circle", True, BLACK), (370, 7))  # circle label
    screen.blit(font.render("Rect", True, BLACK), (455, 7))  # rectangle label
    screen.blit(font.render("Square", True, BLACK), (550, 7))  # square label
    screen.blit(font.render("Right-Tri", True, BLACK), (640, 7))  # right triangle label
    screen.blit(font.render("Equil-Tri", True, BLACK), (730, 7))  # equilateral triangle label
    screen.blit(font.render("Rhomb", True, BLACK), (820, 7))  # rhombus label

    info = font.render(f"Tool: {tool} | Stroke: {stroke_size}", True, BLACK)  # info text
    screen.blit(info, (900, 7))  # draw info on screen

    pygame.display.update()  # update display every frame
    clock.tick(60)  # limit FPS to 60