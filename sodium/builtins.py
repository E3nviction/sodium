from pygame.base import init as _init, quit as _quit  # pylint: disable=no-name-in-module

def quit_window():
    _quit()

def init():
    _init()

    with open("cache.sdc", "w", encoding="utf-8") as file:
        file.seek(0)
        file.truncate()
        file.write("")
    file.close()

    return True
