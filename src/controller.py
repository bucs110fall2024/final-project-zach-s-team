import pygame
from src.card import Card
from src.gamedata import GameData

class Controller:

    def __init__(self):
            pass

    def mainloop(self):
        while True:
            # 1. handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # 2. detect collisions and update models

            # 3. redraw next frame

            # 4. display next frame
            pygame.display.flip()