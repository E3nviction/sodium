import json

theme_colors = {}

def __init__():
    global theme_colors  # pylint: disable=global-statement
    with open("sodium/themes/dark_blue.json", encoding="utf-8") as file:
        theme_colors = json.load(file)

def load_theme(theme):
    global theme_colors  # pylint: disable=global-statement
    with open(theme, encoding="utf-8") as file:
        theme_colors = json.load(file)

    return theme_colors

def load_preset(theme):
    global theme_colors  # pylint: disable=global-statement
    if theme == "dark blue":
        theme = "sodium/themes/dark_blue.json"
    elif theme == "light blue":
        theme = "sodium/themes/light_blue.json"
    elif theme == "light":
        theme = "sodium/themes/light_blue.json"
    elif theme == "dark":
        theme = "sodium/themes/dark_blue.json"
    elif theme == "dark oled":
        theme = "sodium/themes/dark_oled.json"
    elif theme == "default":
        theme = "sodium/themes/dark_blue.json"
    else:
        theme = "sodium/themes/dark_blue.json"
    with open(theme, encoding="utf-8") as file:
        theme_colors = json.load(file)

def get_theme():
    return theme_colors


__init__()
