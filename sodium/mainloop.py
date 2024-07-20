"""
mainloop module
"""
import sodium
from . import theme
from . import Window

def mainloop(win, main, auto=False):
    """
    Starts the mainloop

    :param win: window object
    :param main: main function
    :param auto: auto update
    """
    if not auto:
        running = True
        while running:
            for event in sodium.event.get():
                if event.type == sodium.QUIT:
                    running = False
            win.fill(theme.theme_colors["BACKGROUND"])
            main()
    else:
        running = True
        while running:
            for event in sodium.event.get():
                if event.type == sodium.QUIT:
                    running = False
            win.fill(theme.theme_colors["BACKGROUND"])
            main()
            Window.update(win)

    sodium.quit_window()

def start(win, main):
    """
    Starts the mainloop

    :param win: window object
    :param main: main function
    """
    mainloop(win, main, True)
