import sodium
from sodium.widgets import Button # import the button widget
from sodium import Window # import the window class

sodium.require("0.0.3")
sodium.init()
window = Window(640, 480)
win = window.get_screen()

def toggle_button_2():
    if button_2.is_disabled(): # if the second button is disabled
        button_2.enable() # enable the second button
    else: # if the second button is not disabled
        button_2.disable() # disable the second button
# or...
def toggle_button_2_v2():
    button_2.set_disabled(not button_2.is_disabled())
# or...
def toggle_button_2_v3():
    button_2.toggle_disabled()

# create the button with the on_click_func to toggle the second button
button = Button(win, "Toggle, it! wow this is so long", (50, 50, 150, 50), on_click_func=toggle_button_2)

button_2 = Button(win, "Toggle, me!", (50, 150, 150, 50), disabled=True) # create the second button
button_2.set_on_click_func(lambda: print("I'm Alive!!!")) # set the on_click_func to print "I'm Alive!!!"

def main():
    button.update() # update the button
    button_2.update() # update the second button
sodium.start(win, main)