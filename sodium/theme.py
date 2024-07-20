"""
Theme module
"""
import json

theme_colors = {}

def __init__():
    global theme_colors  # pylint: disable=global-statement
    with open("sodium/themes/dark_blue.json", encoding="utf-8") as file:
        theme_colors = json.load(file)

def load_theme(theme):
    """
    Loads the theme

    :param theme: str
    :return: dict
    """
    global theme_colors  # pylint: disable=global-statement
    with open(theme, encoding="utf-8") as file:
        theme_colors = json.load(file)

    return theme_colors

def get_theme():
    """
    Gets the theme

    :return: dict
    """
    return theme_colors


__init__()
