import sodium
from sodium import Button, Window # import the Button and Window classes

sodium.init()
window = Window(640, 480)
win = window.get_screen()

# this is the function that will be called when the button is pressed
def on_button_press():
    button.set_text("Goodbye, World!") # change the button's text to "Goodbye, World!"

# create the button and set the on_click_func to the on_button_press function
button = Button(win, "Hello, World!", (50, 50, 150, 50), on_click_func=on_button_press) 

def main():
    button.update() # update the button
sodium.start(win, main)