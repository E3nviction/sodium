"""
sodium is a UI libary designed for creating UI's.
It is written on top of the pygame library. This allows you to create fully featured UI's.
The package is highly portable, running on Linux, macOS, OS X, BeOS, FreeBSD, IRIX, and Windows.
"""
import pygame
from .settings import *
from .window import *
from .common import *
from .widgets import *
from .constants import *
from .builtins import *
from .event import *
from .theme import *
from .mainloop import *



__all__ = [
    "settings",
    "common",
    "widgets",
    "Window",
    "constants",
    "builtins",
    "event",
    "theme",
    "mainloop",
    "init",
    "quit_window",
]
__version__ = "0.0.2"

if friendly_messages:
    print("SodiumUI v" + __version__)
