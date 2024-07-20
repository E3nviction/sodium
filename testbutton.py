import sodium
from sodium import Window

sodium.init()
win = Window(640, 480, "Test").get_screen()

def button_press():
    print("Button pressed!")


button = sodium.Button(win, "Btn1", (50, 50, 150, 50))
button.set_on_click(button_press)

def main():
    button.update()
sodium.start(win, main)
