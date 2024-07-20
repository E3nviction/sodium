"""
Module for creating windows
"""
import pygame
import sodium

from . import constants



class Window:
    """
    Window class for controlling the window
    """
    def __init__(self,
                 width: int = 640,
                 height: int = 480,
                 caption: str = "SodiumUI | window",
                 flags: int = constants.RESIZABLE,
                 vsync: int = 1
                ):
        """
        creates the window

        :param width: int
        :param height: int
        :param caption: str
        :param flags: int
        :param vsync: int
        """
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height), flags=flags, vsync=vsync)
        self.set_caption(caption)
        self.rect = self.screen.get_rect()

    def get_screen(self):
        """
        Gets the window's screen

        :return: Surface
        """
        return self.screen

    def update(self):
        """
        Updates the window
        """
        pygame.display.update()

    def fill(self, color):
        """
        Fills the window

        :param color: Color
        """
        color = sodium.Color(*color)
        self.screen.fill(color)

    def set_caption(self, caption):
        """
        Sets the window's caption

        :param caption: str
        """
        pygame.display.set_caption(caption)

    def get_caption(self):
        """
        Gets the window's caption

        :return: str
        """
        return pygame.display.get_caption()

    def get_rect(self):
        """
        Gets the window's rect

        :return: Rect
        """
        return self.rect

    def get_size(self):
        """
        Gets the window's size

        :return: tuple
        """
        return self.screen.get_size()

    def get_width(self):
        """
        Gets the window's width

        :return: int
        """
        return self.screen.get_width()

    def get_height(self):
        """
        Gets the window's height

        :return: int
        """
        return self.screen.get_height()

    def get_flags(self):
        """
        Gets the window's flags

        :return: int
        """
        return self.screen.get_flags()
