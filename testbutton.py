import sodium
from sodium import Window

sodium.init()
window = Window(640, 480)
win = window.get_screen()

label = sodium.Label(win, "Hello, World!")

def main():
    width = window.get_width()
    height = window.get_height()
    label.set_rect((50, 50, window.get_width() - 100, window.get_height() - 100))
    label.update()
sodium.start(win, main)
