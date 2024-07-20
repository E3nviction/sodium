"""
Builtins module
"""
from pygame.base import init as _init, quit as _quit  # pylint: disable=no-name-in-module

def quit_window():
    """
    Closes the window
    """
    _quit()

def init():
    """
    Initializes the window
    """
    _init()
