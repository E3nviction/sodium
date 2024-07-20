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
from sodium import Window # import the window class

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
from sodium import Window # import the window class

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
from sodium.widgets import Button # import the button widget
from sodium import Window # import the window class

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
for this, we can use the `Button` class's `on_click` method. (note that this is not the only way to do this)
```python
import sodium
from sodium.widgets import Button # import the button widget
from sodium import Window # import the window class

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

Note that `on_click_func` is a function that takes no parameters and returns nothing.
Anyway, let's say we wanted the button to change the text of the label to "Goodbye, World!" but without on_click_func.
Do you still remember what I said? That `on_click_func` is not the only way to do this?

well...
```python
import sodium
from sodium.widgets import Button # import the button widget
from sodium import Window # import the window class

sodium.init()
window = Window(640, 480)
win = window.get_screen()

# this is the function that will be called when the button is pressed
def on_button_press():
    button.set_text("Goodbye, World!") # change the button's text to "Goodbye, World!"

# create the button and set the on_click_func to the on_button_press function
button = Button(win, "Hello, World!", (50, 50, 150, 50))

def main():
    if button.is_active() and not button.is_locked(): # if the button is active
        button.set_locked(True) # lock the button
        on_button_press() # call the on_button_press function
    if not button.is_active(): # if the button is not active
        button.set_locked(False) # unlock the button
    button.draw() # draw the button, because with the update function it would check for button clicks twice

sodium.start(win, main)

```
As you can see, we can do this without using `on_click_func`.
We are utilizing the `is_active` and `is_locked` methods of the `Button` class.
so when pressing the button it locks the button and calls the `on_button_press` function.
when locked the button will not be able to be pressed again.

And when releasing the button, the button will be unlocked.

And to be honest, That's still not the only ways to do this.
but we will be looking at more ways to do this in the future.

For now, let's go to the next section!

#### Disabling and Enabling Buttons
A button can be disabled and enabled.
When disabled, the button will not be able to be pressed and will change the color.

Let's create an application with 2 buttons. One button will toggle the disabled state of the other button.
```python
import sodium
from sodium.widgets import Button # import the button widget
from sodium import Window # import the window class

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
button = Button(win, "Toggle, it!", (50, 50, 150, 50), on_click_func=toggle_button_2)

button_2 = Button(win, "Toggle, me!", (50, 150, 150, 50), disabled=True) # create the second button
button_2.set_on_click_func(lambda: print("I'm Alive!!!")) # set the on_click_func to print "I'm Alive!!!"

def main():
    button.update() # update the button
    button_2.update() # update the second button
sodium.start(win, main)
```

Look at that code! You can see that the second button is disabled by default.
And we even used a new method to set the function that will be called when the button is pressed.
`set_on_click_func(func)`.

You now have learned the basics of buttons. Let's leave the tutorial.
## Advanced
### Widgets
#### Labels
A Label is a widget that displays text on the screen.
it's properties include:
surface
text
rect
color
font
font_family
font_size
align_x
align_y

The surface is the surface that the label will be drawn on,
Text is the text that will be displayed,
Rect is the rectangle that the label will be drawn on,
Color is the color of the label,
Font requires a Font object that will be used to display the text,
Font_family is the font family that will be used to display the text,
Font_size is the font size that will be used to display the text,
align_x is the alignment of the label on the x axis, left, center, or right,
align_y is the alignment of the label on the y axis, top, center, or bottom.
... more docs will be added in the future.