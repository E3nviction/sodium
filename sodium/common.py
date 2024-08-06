"""
common module
"""
import pygame
from .constants import Color
from . import theme
from . import cache

def set_color(color, default):
    theme_colors = theme.get_theme()
    color = Color(theme_colors[default]) if color == "theme" else Color(color)
    return color

def set_font(font, font_size):
    theme_colors = theme.get_theme()
    default_font = pygame.font.Font(theme_colors["FONT"], theme_colors["FONT_SIZE"])
    font = default_font if font is None or font == "theme" else pygame.font.Font(font, font_size)
    return font

def widget_get_id():
    return len(cache.widgets) + 1