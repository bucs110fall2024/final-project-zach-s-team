import pygame
from src.nametocc import NameToCC

class Flag(pygame.sprite.Sprite):

    def __init__(self, country, x, y, scale):
        """
        creates a Flag object
        args:
            - country (str): the country whose flag is to be displayed
            - x (int): the flag's x pos
            - y (int): the flag's y pos
            - scale (float): the scale of reduction of image size
        """
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(f"assets/flags/{NameToCC().get(country)}.png"), (640 / scale, 448 / scale))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
