import pygame
from src.flag import Flag
from src.quiz import Quiz
from src.highscore import Highscore

class Controller:

    def __init__(self):
            self.state = "INACTIVE"
            pygame.init()
            self.screen = pygame.display.set_mode((750, 750))
            self.background = pygame.Surface((750, 750))
            self.backgroundColor = (230, 230, 230)
            self.font = pygame.font.SysFont(None, 30)
            self.inputText = ""
            self.input = self.font.render(self.inputText, True, (0, 0, 0))
            self.highscore = Highscore()
            self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p' ,'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    
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

            textObj = self.font.render(f"Click anywhere to start the quiz! Highscore: {self.highscore.get()}/197", True, (0, 0, 0))

            self.background.fill(self.backgroundColor)
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(textObj, (150, 250))
            pygame.display.flip()

    def activeloop(self):
        self.quiz = Quiz()
        while self.state == "ACTIVE":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
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
                            self.state = "INACTIVE"
                            self.inputText = ""
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
            counter = self.font.render(f"{self.quiz.correctCountries}/197", True, (0, 0, 0))
            flag = Flag(self.quiz.currentCountry, 100, 100)
            self.input = self.font.render(self.inputText, True, (0, 0, 0))
            self.background.fill(self.backgroundColor)
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(flag.image, (125, 250))
            self.screen.blit(textObj1, (100, 100))
            self.screen.blit(textObj2, (75, 150))
            self.screen.blit(counter, (650, 700))
            self.screen.blit(self.input, (100, 650))
            pygame.display.flip()

