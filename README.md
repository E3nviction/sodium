# sodium
UI Libary written in Python using pygame


## About

Sodium is a UI library written in Python using Pygame. 
It aims to provide a simple and easy to use interface for creating graphical user interfaces and other graphical applications.

## Installation 
(WIP)
dependencies:
 - pygame-ce

To install Sodium, move the sodium folder into your project folder and import it in your project:
```python
import sodium
```

## License
This project is licensed under the MIT license.
which means that you can use this project in any way you want.
Fork it, modify it, or redistribute it as you wish.
For more information, visit [https://github.com/E3nviction/sodium/blob/main/LICENSE](https://github.com/E3nviction/sodium/blob/main/LICENSE)


# Docs
## Getting Started
### Create a window
To create a window, use the `Window` class.
```python
import sodium # import sodium
from sodium import Window # import the Window class

sodium.init() # initialize sodium
window = Window(640, 480) # create a window with width 640 and height 480
win = window.get_screen() # get the screen of the window to draw on

def main(): # define the main function
    # do nothing
    pass 
sodium.start(win, main) # start sodium mainloop
```
this will create a window with width 640 and height 480.
### Hello World
To get started with Sodium, create a new file named `main.py` and copy the code below into it.
```python
import sodium # import sodium
from sodium import Window # import the Window class

sodium.init() # initialize sodium
window = Window(640, 480) # create a window with width 640 and height 480
win = window.get_screen() # get the screen of the window to draw on

label = sodium.Label(win, "Hello, World!") # create a label with text "Hello, World!"

def main(): # define the main function
    label.set_rect((50, 50, window.get_width() - 100, window.get_height() - 100)) # set the position of the label to the center of the window
    label.update() # update the label
sodium.start(win, main) # start sodium mainloop
```
this will create a window with a label "Hello, World!" in the center of the screen.
resize the window and the label will update to the new position.
### Button
To create a button, you can use the `Button` class.
```python
import sodium # import sodium
from sodium import Button, Window # import the Button and Window classes

sodium.init()
window = Window(640, 480)
win = window.get_screen()

button = Button(win, "Hello, World!", (50, 50, 150, 50))

# and in the mainloop you can update the button
def main():
    button.update()
sodium.start(win, main)
```
in this example, the button will be created at position (50, 50) with size 150x50.
and pressing the button will do nothing.

but what if we wanted the button to do something?
let's say we wanted the button to change the text of the label to "Goodbye, World!" when the button is pressed.

#### on_click_func
for this, we can use the `Button` class's `on_click` method. (remember that this is not the only way to do this)
```python
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
```
Great! Now, when the button is pressed, the `on_button_press` function will be called.
And the button's text will change to "Goodbye, World!".

