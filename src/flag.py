import pygame
from src.nametocc import NameToCC

class Flag(pygame.sprite.Sprite):

    def __init__(self, country, x, y):
        """
        creates a Flag object
        args:
            - country (str): the country whose flag is to be displayed
            - x (int): the flag's x pos
            - y (int): the flag's y pos
        """
        super().__init__()
        self.imageScaleFactor = 5
        self.image = pygame.transform.scale(pygame.image.load(f"assets/flags/{NameToCC().get(country)}.png"), (2560 / self.imageScaleFactor, 1792 / self.imageScaleFactor))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
