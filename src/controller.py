import pygame
import pygame_menu
import random
from src.flag import Flag
from src.quiz import Quiz
from src.nametocc import NameToCC

class Controller:

    def __init__(self):
            self.state = "INACTIVE"
            pygame.init()
            self.screen = pygame.display.set_mode((1000, 750))
            self.background = pygame.Surface(pygame.display.get_window_size())
            self.background.fill((255, 255, 255))
    
    def mainloop(self):
        while True:
            if self.state == "INACTIVE":
                self.inactiveloop()
            if self.state == "ACTIVE":
                self.activeloop()

    def inactiveloop(self):
        while self.state == "INACTIVE":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.state = "ACTIVE"

            highscore = open("etc/highscore.txt").read()

            menu = pygame_menu.Menu("Start", 1000, 750)
            menu.add.label("Click to start the quiz!")
            menu.add.label(f"Highscore: {highscore}")

            menu.draw(self.screen)
            pygame.display.flip()

    def activeloop(self):
        quiz = Quiz()
        def checkAnswer(text):
            if text == quiz.currentCountry:
                quiz.newCountry()
        print(quiz.currentCountry)
        while self.state == "ACTIVE":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            menu = pygame_menu.Menu("Quiz", 1000, 750)
            menu.add.text_input("", default="Type here: ", onchange=checkAnswer, input_type="input-text", input_underline="_")

            self.background.fill((255, 255, 255))
            menu.draw(self.screen)
            pygame.display.flip()

