"""
The  View  file for the Model-View-Controller architecture for our game.
Its   draw_everything   method is called repeatedly by the main game loop.
At each call, it displays a view of the game,
typically by asking the various objects of the Game to draw themselves.

Team members:
Anh Ngo
J.J. Moe
Quang Dao
"""
# DONE: Put the names of your entire team in the above doc-string.

import pygame

from Game import Game
from winning_screen import Scoreboard


class View:
    def __init__(self, screen: pygame.Surface, game: Game):
        self.screen = screen
        self.game = game
        self.image = pygame.image.load(
            "../media/Background_1.jpg")
        self.image_1 = pygame.transform.scale(self.image, (1430, 730))



    def draw_everything(self):
        self.screen.blit(self.image_1, (0, 0))


        self.game.draw_game()
        pygame.display.update()
