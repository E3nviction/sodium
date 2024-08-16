import sodium
from . import theme
from . import Window
from . import cache

def mainloop(win="wiscreen", main=None, auto=False):
    if win == "wiscreen":
        win = cache.screen
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
            Window.flip(win)
            Window.update(win)

    sodium.quit_window()

def start(win="wiscreen", main=None):
    if win == "wiscreen":
        win = cache.screen
    mainloop(win, main, True)

def bg_fill(win="wiscreen", color=None):
    if win == "wiscreen":
        win = cache.screen
    if color is None:
        win.fill(theme.theme_colors["BACKGROUND"])
    else:
        win.fill(color)
