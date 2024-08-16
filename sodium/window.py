import pygame
import sodium

from . import constants

class Window:
    def __init__(self,
                 width: int = 640,
                 height: int = 480,
                 caption: str = "SodiumUI | window",
                 flags: int = constants.RESIZABLE,
                 vsync: int = 1
                ):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height), flags=flags, vsync=vsync)
        self.set_caption(caption)
        self.rect = self.screen.get_rect()

    def get_screen(self):
        return self.screen

    def update(self):
        pygame.display.update()

    def flip(self):
        pygame.display.flip()

    def fill(self, color):
        color = sodium.Color(*color)
        self.screen.fill(color)

    def set_caption(self, caption):
        pygame.display.set_caption(caption)

    def get_caption(self):
        return pygame.display.get_caption()

    def get_rect(self):
        return self.rect

    def get_size(self):
        return self.screen.get_size()

    def get_width(self):
        return self.screen.get_width()

    def get_height(self):
        return self.screen.get_height()

    def get_flags(self):
        return self.screen.get_flags()
