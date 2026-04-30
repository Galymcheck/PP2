import pygame
import sys
import json
from game import Game
from config import *
from db import save_score, get_top10

pygame.init()

screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
clock = pygame.time.Clock()

font = pygame.font.SysFont("Verdana", 20)

# ================= SETTINGS =================
def load_settings():
    with open("C:/Users/Galam/OneDrive/Документы/VScodes/repositories/PP2/TSIS4/settings.json", "r") as f:
        return json.load(f)

def save_settings(data):
    with open("C:/Users/Galam/OneDrive/Документы/VScodes/repositories/PP2/TSIS4/settings.json", "w") as f:
        json.dump(data, f, indent=4)

settings = load_settings()

# ================= STATES =================
MENU = "menu"
NAME = "name"
GAME = "game"
SETTINGS = "settings"
LEADER = "leader"

state = MENU

username = ""
game = None

# ================= BUTTONS =================
play_btn = pygame.Rect(130, 120, 140, 50)
set_btn = pygame.Rect(130, 190, 140, 50)
quit_btn = pygame.Rect(130, 260, 140, 50)

# settings buttons
color_btn = pygame.Rect(120, 100, 160, 40)
sound_btn = pygame.Rect(120, 160, 160, 40)
grid_btn = pygame.Rect(120, 220, 160, 40)
back_btn = pygame.Rect(120, 300, 160, 40)

def btn(rect, text):
    pygame.draw.rect(screen, (60, 60, 60), rect)
    screen.blit(font.render(text, True, (255,255,255)), (rect.x+10, rect.y+8))

# ================= LOOP =================
running = True

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # ===== MENU =====
        if state == MENU:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_btn.collidepoint(event.pos):
                    state = NAME

                elif set_btn.collidepoint(event.pos):
                    state = SETTINGS

                elif quit_btn.collidepoint(event.pos):
                    running = False

        # ===== NAME INPUT =====
        elif state == NAME:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game = Game(username, settings)
                    state = GAME
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    username += event.unicode

        # ===== SETTINGS =====
        elif state == SETTINGS:
            if event.type == pygame.MOUSEBUTTONDOWN:

                # color toggle
                if color_btn.collidepoint(event.pos):
                    colors = [
                        [255,255,255],
                        [0,255,0],
                        [255,0,0],
                        [0,0,255]
                    ]
                    idx = colors.index(settings["snake_color"]) if settings["snake_color"] in colors else 0
                    settings["snake_color"] = colors[(idx+1)%len(colors)]

                # sound toggle
                if sound_btn.collidepoint(event.pos):
                    settings["sound"] = not settings["sound"]

                # grid toggle
                if grid_btn.collidepoint(event.pos):
                    settings["grid"] = not settings["grid"]

                if back_btn.collidepoint(event.pos):
                    save_settings(settings)
                    state = MENU

        # ===== GAME =====
        elif state == GAME:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and game.snake.direction != DOWN:
                    game.snake.direction = UP
                elif event.key == pygame.K_DOWN and game.snake.direction != UP:
                    game.snake.direction = DOWN
                elif event.key == pygame.K_LEFT and game.snake.direction != RIGHT:
                    game.snake.direction = LEFT
                elif event.key == pygame.K_RIGHT and game.snake.direction != LEFT:
                    game.snake.direction = RIGHT

    # ================= MENU =================
    if state == MENU:
        screen.blit(font.render("SNAKE GAME", True, (255,255,255)), (130, 50))
        btn(play_btn, "PLAY")
        btn(set_btn, "SETTINGS")
        btn(quit_btn, "QUIT")

    # ================= NAME =================
    elif state == NAME:
        screen.blit(font.render("ENTER NAME:", True, (255,255,255)), (120, 100))
        screen.blit(font.render(username, True, (255,255,255)), (120, 140))

    # ================= SETTINGS =================
    elif state == SETTINGS:
        screen.blit(font.render("SETTINGS", True, (255,255,255)), (150, 40))

        btn(color_btn, f"Color: {settings['snake_color']}")
        btn(sound_btn, f"Sound: {settings['sound']}")
        btn(grid_btn, f"Grid: {settings['grid']}")
        btn(back_btn, "BACK")

    # ================= GAME =================
    elif state == GAME:
        clock.tick(game.speed)

        game.update()
        game.draw(screen)

        screen.blit(font.render(f"Score: {game.score}", True, (255,255,255)), (10, 10))
        screen.blit(font.render(f"Level: {game.level}", True, (255,255,255)), (10, 30))
        screen.blit(font.render(f"Apple: {game.apple.time_left()}", True, (255,255,255)), (250, 10))

        if game.game_over:
            save_score(game.username, game.score, game.level)
            state = LEADER

    # ================= LEADERBOARD =================
    elif state == LEADER:
        screen.blit(font.render("LEADERBOARD", True, (255,255,255)), (120, 20))

        data = get_top10()

        y = 60
        for i, d in enumerate(data):
            text = f"{i+1}. {d['username']} - {d['score']} ({d['time']})"
            screen.blit(font.render(text, True, (255,255,255)), (40, y))
            y += 25

        screen.blit(font.render("ESC -> MENU", True, (255,255,255)), (130, 360))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            state = MENU
            username = ""

    pygame.display.update()

pygame.quit()
sys.exit()