import pygame
import pygame_menu

class Controller:

    def __init__(self):
            self.state = "MENU"

    def mainloop(self):
        while True:
            if self.state == "MENU":
                self.menuloop()
            if self.state == "GAME":
                self.gameloop()

    def menuloop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def gameloop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
