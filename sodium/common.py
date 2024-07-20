"""
common module
"""
import pygame
from .constants import Color
from .theme import theme_colors

def set_color(color, default):
    """
    Sets the color

    :param color: Color
    :param default: str
    :return: Color
    """
    color = Color(theme_colors[default]) if color == "theme" else Color(color)
    return color

def set_font(font, font_size):
    """
    Sets the font

    :param font: str
    :param font_size: int
    :return: str
    """
    default_font = pygame.font.Font(theme_colors["FONT"], theme_colors["FONT_SIZE"])
    font = default_font if font is None or font == "theme" else pygame.font.Font(font, font_size)
    return font
