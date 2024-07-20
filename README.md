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

## Docs
### Getting Started
#### Hello World
To get started with Sodium, create a new file named `main.py` and copy the code below into it.
```python
import sodium
from sodium import Window

sodium.init()
window = Window(640, 480)
win = window.get_screen()

label = sodium.Label(win, "Hello, World!")

def main():
    label.set_rect((50, 50, window.get_width() - 100, window.get_height() - 100))
    label.update()
sodium.start(win, main)
```


## License
This project is licensed under the MIT license.