"""
sodium is a UI libary designed for creating UI's.
It is written on top of the pygame library. This allows you to create fully featured UI's.
The package is highly portable, running on Linux, macOS, OS X, BeOS, FreeBSD, IRIX, and Windows.
"""
  # pylint: disable=wrong-import-order, wrong-import-position

import os
import sys
import warnings

sys.stdout = open(os.devnull, 'w', encoding='utf-8')
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
warnings.filterwarnings("ignore", category=RuntimeWarning, message=".*avx2.*")
import pygame
sys.stdout = sys.__stdout__

__version__ = "0.0.9"
VERSION_0_0_7 = "0.0.7"
VERSION_0_0_8 = "0.0.8"
VERSION_0_0_9 = "0.0.9"
VERSION_LATEST = "latest"

from .settings import *
from .window import *
from .common import *
from .constants import *
from .builtins import *
from .event import *
from .theme import *
from .mainloop import *
from .require import *
from .signal import *

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
    "require",
    "load_theme",
    "get_theme",
    "Signal",
]

if not hide_friendly_messages:
    print("Sodium v" + __version__)
