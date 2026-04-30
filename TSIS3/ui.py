# ui.py
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class UI:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 24)
        self.big_font = pygame.font.SysFont("Arial", 50)

    def draw_hud(self, score, coins, distance):
        score_text = self.font.render(f"Score: {score}", True, BLACK)
        coin_text = self.font.render(f"Coins: {coins}", True, BLACK)
        dist_text = self.font.render(f"Distance: {distance}", True, BLACK)

        self.screen.blit(score_text, (10, 10))
        self.screen.blit(coin_text, (10, 40))
        self.screen.blit(dist_text, (10, 70))

    def draw_menu(self):
        title = self.big_font.render("RACER GAME", True, BLACK)
        self.screen.blit(title, (60, 200))

    def draw_game_over(self, score):
        text = self.big_font.render("GAME OVER", True, BLACK)
        self.screen.blit(text, (60, 200))