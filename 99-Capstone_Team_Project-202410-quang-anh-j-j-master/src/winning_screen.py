import pygame.image


class Scoreboard:
    def __init__(self, screen):
        self.screen = screen

        font_1 = pygame.font.SysFont("Player 1 Wins!", 100)
        self.caption1 = font_1.render("Player 1 Wins!", True, (255, 0, 255))

        font_2 = pygame.font.SysFont("PLayer 2 Wins!", 100)
        self.caption2 = font_2.render("Player 2 Wins!", True, (255, 0, 255))

    def draw_1(self):
        self.screen.blit(self.caption1, (550, 350))

    def draw_2(self):
        self.screen.blit(self.caption2, (550, 350))
