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

# Docs (OUT OF DATE)
## Getting Started
### Create a window
To create a window, use the `Window` class.
```python
import sodium # import sodium
from sodium import Window # import the window class

sodium.require(sodium.__version__)
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
Also let's make the 2nd button disabled by default. And clickable using the right mouse button.
```python
import sodium
from sodium.widgets import Button # import the button widget
from sodium import Window # import the window class
sodium.require("0.0.4")

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
button_2.set_mouse_button(2) # set the mouse button to the right mouse button

def main():
    button.update() # update the button
    button_2.update() # update the second button
sodium.start(win, main)
```

Look at that code! You can see that the second button is disabled by default.
And we even used a new method to set the function that will be called when the button is pressed.
`set_on_click_func(func)`.

If you looked closely at the code, you will notice that I added a `sodium.require("0.0.4")` to the top of the file.
This is because I am using the `sodium` library version 0.0.4. So if you are using a different version of the library, you will get an error.
This line is not mandatory. It is just a way to make sure that you are using the correct version of the library. But that might change in the future.

You now have learned the basics of buttons. Let's go to the advanced section.
## Advanced
### Widgets
#### Labels
The `Label` widget is used to display text on the screen.
It has a sibling called the `FreeLabel` which is used to display text on the screen without any bounds.
Because when using the Label widget, the text will be cut off when not inside its rectangle.

The `Label` has a lot of parameters that can be set.
To create a Label simply import the `Label` class from the `sodium.widgets` module.
And then create the Label using the `Label` constructor.
```python
label = Label(surface, text, rect, color, font, font_family, font_size, align_x, align_y)
```
When creating a Label, you wont actually need all of those parameters.
Because most of them have a default value. So a simple Label will look like this:
```python
label = Label(surface, text, rect)
```
Because the Color, font, and alignment parameters are already set by the [theme], we can skip them.

If you want to take a closer look at the parameters I've listed them here:
`surface`          : The surface on which the label will be drawn
`text`             : The text that will be displayed
`rect`             : The rectangle that the label will be drawn in
`color`            : The color of the text
`font`             : The sodium.Font of the text
`font_family`      : The font family of the text
`font_size`        : The font size of the text
`align_horizontal` : The horizontal alignment of the text ("left", "center", "right")
`align_vertical`   : The vertical alignment of the text ("top", "center", "bottom")

Now let's take a look at the methods of the Label widget.

Let's first create a Label:
```python
label = Label(win, "Hello, World!", (0,0,150,50))
```
now let's render it where the first 2 methods come into play:
`draw()` and `update()`
So if we wanted the label to be rendered we could do it like this:
```python
label.update()
```
or
```python
label.draw()
```
Because the `update()` method is the same as the `draw()` method, we can use either one.

But okay, let's take a look at another method:
What if we wanted to change the text of the label?
or get the label's text?

```python
label.set_text("Goodbye, World!")
```
For this we would use the `set_text()` method.
And for getting the text we would use the `get_text()` method.
```python
text = label.get_text()
```

Alright, let's go to the next method:
`set_rect(rect)`
This method can be used to set the rectangle that the label will be drawn in.
```python
label.set_rect((50, 50, 150, 50))
```
There's also a `get_rect()` method that can be used to get the rectangle that the label will be drawn in.
```python
rect = label.get_rect()
```

Now, the next 3 methods are for getting the size of the label:
`get_text_size()`
`get_text_width()`
and `get_text_height()`

```python
size = label.get_text_size()
width = label.get_text_width()
height = label.get_text_height()
```
These methods are for getting the size of the label. Not the size of the rectangle.

Now, let's go to the next method:
`get_x()`, `get_y()` and `set_x()`, `set_y()`

Using these methods we can get and set the x and y position of the label.

The next method is `get_width()`, `get_height()` and `set_width()`, `set_height()`

Again, they are self-explanatory. We can use them to set and get the width and height of the label.

Then there's also the `get_color()` and `set_color()`

```python
color = label.get_color()
label.set_color((0, 0, 0))
```

These methods are for getting and setting the color of the label.

next up is the `get_font()` and `set_font()`, aswell as the `get_font_family()`, `get_font_size()`, `set_font_family()` and `set_font_size()`

when setting the font you need to either give it a pre installed font like "Arial" or give it a filename like "path/to/font.ttf"

And finally there's the `get_align_horizontal()`, `get_align_vertical()`, `get_align()` and the opposite methods `set_align_horizontal()`, `set_align_vertical()`, `set_align()`

With these methods we can get and set the horizontal and vertical alignment of the label.

Available alignments are "left", "center", "right" and for align_vertical "top", "middle", "bottom"



And thats it. (For now)
The `FreeLabel` is the same as the `Label` but with no bounds when drawing.

#### Buttons
The `Button` widget is used to create buttons.
It is able to be pressed and released, disabled and enabled.

The `Button` has a lot of parameters those being
surface                     : The surface on which the button will be drawn
text                        : The text that will be displayed
rect=(0, 0, 0, 0)           : The rectangle that the button will be drawn in
color="theme"               : The color of the button
background="theme"          : The background color of the button
hover_color="theme"         : The color of the button when hovered
hover_background="theme"    : The background color of the button when hovered
active_color="theme"        : The color of the button when pressed
active_background="theme"   : The background color of the button when pressed
disabled_color="theme"      : The color of the button when disabled
disabled_background="theme" : The background color of the button when disabled
font=None                   : The sodium.Font of the button
font_family=None            : The font family of the button
font_size=20                : The font size of the button
label_horizontal="center"   : The horizontal alignment of the button's text ("left", "center", "right")
label_vertical="center"     : The vertical alignment of the button's text ("top", "center", "bottom")
disabled=False              : Whether the button is disabled or not
on_click_func=None          : The function that will be called when the button is pressed
on_click_args=None          : The arguments that will be passed to the `on_click_func` function
mouse_button=0              : The mouse button that will be used when the button is pressed (left=0, middle=1, right=2)

It also has the following methods:
is_touching_mouse(self)
is_active(self)
is_locked(self)
is_disabled(self)
set_on_click_func(self, func)
set_text(self, text)
get_text(self)
set_on_click_args(self, args)
get_on_click_args(self)
get_rect(self)
get_size(self)
get_width(self)
get_height(self)
set_rect(self, rect)
set_color(self, color)
set_background(self, color)
set_disabled(self, disabled)
set_disabled_color(self, color)
set_disabled_background(self, color)
set_hover_color(self, color)
set_hover_background(self, color)
set_active_color(self, color)
set_active_background(self, color)
set_font(self, font_family, font_size)
on_click(self)
set_label_horizontal(self, horizontal)
set_label_vertical(self, vertical)
set_locked(self, locked)
get_label_horizontal(self)
get_label_vertical(self)
get_font(self)
enable(self)
disable(self)
toggle_disabled(self)
get_mouse_button(self)
set_mouse_button(self, mouse_button)
draw(self)
update(self)

And again, they are self-explanatory.
#### Frame
### themes
In sodium you can leave the parameters for colors empty which will it load default colors from a theme. The default theme is "dark blue"
but if you want a custom theme you can use 
```python
load_theme(location)
```
to load a json file.
And if you wanted to get the current theme, you can use:
```python
get_theme()
```
To get the json data of the current theme.
to make a custom theme you can create a .json file and then import the them from get_theme() into it.
But you can also load one of the pre made ones, those including "dark", "light" and "dark blue", aswell as "light blue"
these will either load the "dark_blue.json" file or the "light_blue.json" file.
