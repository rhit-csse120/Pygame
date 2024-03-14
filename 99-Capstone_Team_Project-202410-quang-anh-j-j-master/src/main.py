"""
The  main  file for the Model-View-Controller (MVC) architecture for our game.
It:
   1. Initializes pygame, the screen and a Clock (for the frame rate).
   2. Constructs a Game (model), View and Controller.
   3. Runs the game loop, which repeatedly (per the frame rate):
      -- Asks the Controller object to get and respond to events.
      -- Asks the Game object to run one cycle.
      -- Asks the View object to draw everything.

Team members:
Anh Ngo
J.J. Moe
Quang Dao
"""
# DONE: Put the names of your entire team in the above doc-string.

import pygame

from Controller import Controller
from Game import Game
from View import View

again = True
def main():
    pygame.init()
    pygame.display.set_caption("Tanks")  # DONE: Put your own game name
    screen = pygame.display.set_mode((1500, 800))  # DONE: Choose your own size
    clock = pygame.time.Clock()
    game = Game(screen)  # the Model
    view = View(screen, game)  # the View
    controller = Controller(game)  # the Controller
    pygame.mixer.music.load("../media/bouncy-ball-55955.mp3")
    pygame.mixer.music.play()
    frame_rate = 60  # DONE: Choose your own frame rate

    while True:
        clock.tick(frame_rate)
        controller.get_and_handle_events()
        game.run_one_cycle()
        view.draw_everything()


main()
