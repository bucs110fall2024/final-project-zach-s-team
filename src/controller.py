import pygame
import json
import random
from src.flag import Flag
from src.quiz import Quiz
from src.highscore import Highscore

class Controller:

    def __init__(self):
            """
            initializes the controller object
            args: None
            return: None
            """
            self.state = "INACTIVE"
            pygame.init()
            pygame.display.set_caption("flags quiz")
            self.screen = pygame.display.set_mode((750, 750))
            self.background = pygame.Surface((750, 750))
            self.backgroundColor = (230, 230, 230)
            self.font = pygame.font.SysFont(None, 30)
            self.inputText = ""
            self.input = self.font.render(self.inputText, True, (0, 0, 0))
            self.highscore = Highscore()
            self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p' ,'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            self.randomFlag1 = Flag(self.randomCountry(), 0, 0, 3)
            self.randomFlag2 = Flag(self.randomCountry(), 0, 0, 3)

    
    def mainloop(self):
        """
        the mainloop of the controller
        args: None
        return: None
        """
        while True:
            if self.state == "INACTIVE":
                self.inactiveloop()
            if self.state == "ACTIVE":
                self.activeloop()

    def inactiveloop(self):
        """
        the loop that runs while the quiz is inactive
        args: None
        return: None
        """
        while self.state == "INACTIVE":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.state = "ACTIVE"

            textObj = self.font.render(f"Click anywhere to start the quiz! Highscore: {self.highscore.get()}/197", True, (0, 0, 0))
            logo = pygame.image.load("assets/logo.png")

            self.background.fill(self.backgroundColor)
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(textObj, (125, 500))
            self.screen.blit(self.randomFlag1.image, (25, 226))
            self.screen.blit(self.randomFlag2.image, (512, 226))
            self.screen.blit(logo, (265, 226))
            pygame.display.flip()

    def activeloop(self):
        """
        the loop that runs while the quiz is active
        args: None
        return: None
        """
        self.quiz = Quiz()
        while self.state == "ACTIVE":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if int(self.highscore.get()) < self.quiz.correctCountries:
                        self.highscore.set(self.quiz.correctCountries)
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.inputText += " "
                    elif event.key == pygame.K_BACKSPACE:
                        self.inputText = self.inputText[:-1]
                    elif event.key == pygame.K_RETURN:
                        if self.inputText == "skip":
                            self.inputText = ""
                            if self.quiz.unusedCountries:
                                self.quiz.newCountry()
                            else:
                                if int(self.highscore.get()) < self.quiz.correctCountries:
                                    self.highscore.set(self.quiz.correctCountries)
                                self.state = "INACTIVE"
                        elif self.inputText == "exit":
                            if int(self.highscore.get()) < self.quiz.correctCountries:
                                self.highscore.set(self.quiz.correctCountries)
                            pygame.quit()
                            exit()
                        elif self.inputText == self.quiz.currentCountry.lower():
                            self.quiz.correctCountries += 1
                            self.inputText = ""
                            if self.quiz.unusedCountries:
                                self.quiz.newCountry()
                            else:
                                if int(self.highscore.get()) < self.quiz.correctCountries:
                                    self.highscore.set(self.quiz.correctCountries)
                                self.state = "INACTIVE"
                            
                    elif pygame.key.name(event.key) in self.alphabet:
                        self.inputText += pygame.key.name(event.key)

            textObj1 = self.font.render("What country is this? Type your answer and hit enter.", True, (0, 0, 0))
            textObj2 = self.font.render("Type SKIP to skip the current question and EXIT to end the quiz.", True, (0, 0, 0))
            correctCounter = self.font.render(f"{self.quiz.correctCountries}/197", True, (0, 0, 0))
            remainingCounter = self.font.render(f"{len(self.quiz.unusedCountries) + 1} remaining", True, (0, 0, 0))
            flag = Flag(self.quiz.currentCountry, 150, 250, 1.5)
            self.input = self.font.render(self.inputText, True, (0, 0, 0))
            self.background.fill(self.backgroundColor)
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(flag.image, (150, 250))
            self.screen.blit(textObj1, (100, 100))
            self.screen.blit(textObj2, (75, 150))
            self.screen.blit(correctCounter, (650, 700))
            self.screen.blit(remainingCounter, (50, 700))

            self.screen.blit(self.input, (100, 600))
            pygame.display.flip()

    def randomCountry(self):
        """
        returns a random valid country
        args: None
        return: None
        """
        file = open("etc/countries.json")
        data = json.load(file)
        file.close()
        self.countries = []
        for i in data:
            self.countries.append(i["name"])
        return random.choice(self.countries)