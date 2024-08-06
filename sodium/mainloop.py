"""
mainloop module
"""
import sodium
from . import theme
from . import Window

def mainloop(win, main, auto=False):
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

def start(win, main):
    mainloop(win, main, True)
