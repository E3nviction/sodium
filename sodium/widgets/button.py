"""
Button widget module
"""
import pygame
from .. import constants, common
from .label import Label

class Button:
    """
    A button widget that displays text and is clickable with a mouse button, aswell as being able to be disabled and enabled.
    """
    def __init__(
        self,
        surface,
        text,
        rect=(0, 0, 0, 0),
        color="theme",
        background="theme",
        hover_color="theme",
        hover_background="theme",
        active_color="theme",
        active_background="theme",
        disabled_color="theme",
        disabled_background="theme",
        font=None,
        font_family=None,
        font_size=20,
        label_horizontal="center",
        label_vertical="center",
        disabled=False,
        on_click_func=None,
        on_click_args=None,
        mouse_button=0
        ):
        """
        Initializes the button

        :param surface: Surface
        :param text: str
        :param rect: tuple
        :param color: Color
        :param background: Color
        :param hover_color: Color
        :param hover_background: Color
        :param active_color: Color
        :param active_background: Color
        :param disabled_color: Color
        :param disabled_background: Color
        :param font: Font
        :param font_family: str
        :param font_size: int
        :param label_horizontal: str [left, center, right]
        :param label_vertical: str [top, center, bottom]
        :param disabled: bool
        :param on_click_func: function
        :param on_click_args: list
        :param mouse_button: int
        """
        super().__init__()
        self.surface = surface
        self.text = text
        self.rect = constants.Rect(rect)
        self.color = common.set_color(color, "ACCENT_FOREGROUND")
        self.background = common.set_color(background, "ACCENT")
        self.hover_color = common.set_color(hover_color, "FOREGROUND")
        self.hover_background = common.set_color(hover_background, "ACCENT_HOVER")
        self.active_color = common.set_color(active_color, "FOREGROUND")
        self.active_background = common.set_color(active_background, "ACCENT_ACTIVE")
        self.disabled_color = common.set_color(disabled_color, "ACCENT_FOREGROUND_DISABLED")
        self.disabled_background = common.set_color(disabled_background, "ACCENT_DISABLED")
        self.font = font
        self.font_family = font_family
        self.font_size = font_size
        self.label_horizontal = label_horizontal
        self.label_vertical = label_vertical
        self.disabled = disabled
        self.on_click_func = on_click_func
        self.on_click_args = on_click_args
        self.locked = False
        self.mouse_button = mouse_button

        if font is None:
            self.font = common.set_font(font_family, font_size)

    def is_touching_mouse(self):
        """
        Checks if the mouse is touching the button

        :return: bool
        """
        return self.rect.collidepoint(pygame.mouse.get_pos()) and not self.disabled

    def is_active(self):
        """
        Checks if the button is active

        :return: bool
        """
        return self.is_touching_mouse() and pygame.mouse.get_pressed()[self.mouse_button] and not self.disabled

    def is_locked(self):
        """
        Checks if the button is locked

        :return: bool
        """
        return self.locked

    def is_disabled(self):
        """
        Checks if the button is disabled

        :return: bool
        """
        return self.disabled

    def set_on_click_func(self, func):
        """
        Sets the button's on click function

        :param func: function
        """
        self.on_click_func = func

    def set_text(self, text):
        """
        Sets the button's text

        :param text: str
        """
        self.text = text

    def get_text(self):
        """
        Gets the button's text

        :return: str
        """
        return self.text
    
    def set_on_click_args(self, args):
        """
        Sets the button's on click arguments

        :param args: list
        """
        self.on_click_args = args

    def get_on_click_args(self):
        """
        Gets the button's on click arguments

        :return: list
        """
        return self.on_click_args

    def get_rect(self):
        """
        Gets the button's rect

        :return: Rect
        """
        return self.rect

    def get_size(self):
        """
        Gets the button's size

        :return: tuple
        """
        return self.font_family.size(self.text)

    def get_width(self):
        """
        Gets the button's width

        :return: int
        """
        return self.get_size()[0]

    def get_height(self):
        """
        Gets the button's height

        :return: int
        """
        return self.get_size()[1]

    def set_rect(self, rect):
        """
        Sets the button's rect

        :param rect: Rect
        """
        self.rect = constants.Rect(rect)

    def set_color(self, color):
        """
        Sets the button's color

        :param color: Color
        """
        self.color = common.set_color(color, "FOREGROUND")

    def set_background(self, color):
        """
        Sets the button's background

        :param color: Color
        """
        self.background = common.set_color(color, "ACCENT")

    def set_disabled(self, disabled):
        """
        Sets the button's disabled

        :param disabled: bool
        """
        self.disabled = disabled

    def set_disabled_color(self, color):
        """
        Sets the button's disabled color

        :param color: Color
        """
        self.disabled_color = common.set_color(color, "FOREGROUND_DISABLED")

    def set_disabled_background(self, color):
        """
        Sets the button's disabled background

        :param color: Color
        """
        self.disabled_background = common.set_color(color, "ACCENT_DISABLED")

    def set_hover_color(self, color):
        """
        Sets the button's hover color

        :param color: Color
        """
        self.hover_color = common.set_color(color, "FOREGROUND")

    def set_hover_background(self, color):
        """
        Sets the button's hover background

        :param color: Color
        """
        self.hover_background = common.set_color(color, "ACCENT_HOVER")

    def set_active_color(self, color):
        """
        Sets the button's active color

        :param color: Color
        """
        self.active_color = common.set_color(color, "FOREGROUND")

    def set_active_background(self, color):
        """
        Sets the button's active background

        :param color: Color
        """
        self.active_background = common.set_color(color, "ACCENT_ACTIVE")

    def set_font(self, font_family, font_size):
        """
        Sets the button's font

        :param font: str
        :param font_size: int
        """
        self.font = common.set_font(font_family, font_size)

    def on_click(self):
        """
        Calls the button's on click function
        """
        if self.is_active() and not self.is_locked():
            self.locked = True
            if self.on_click_func:
                if self.on_click_args:
                    self.on_click_func(*self.on_click_args)
                else:
                    self.on_click_func()
        if not self.is_active():
            self.locked = False

    def set_label_horizontal(self, horizontal):
        """
        Sets the button's label horizontal

        :param horizontal: str
        """
        self.label_horizontal = horizontal

    def set_label_vertical(self, vertical):
        """
        Sets the button's label vertical

        :param vertical: str
        """
        self.label_vertical = vertical
    
    def set_locked(self, locked):
        """
        Sets the button's locked

        :param locked: bool
        """
        self.locked = locked

    def get_label_horizontal(self):
        """
        Gets the button's label horizontal

        :return: str
        """
        return self.label_horizontal

    def get_label_vertical(self):
        """
        Gets the button's label vertical

        :return: str
        """
        return self.label_vertical

    def get_font(self):
        """
        Gets the button's font

        :return: str
        """
        return self.font
    
    def enable(self):
        """
        Enables the button
        """
        self.disabled = False

    def disable(self):
        """
        Disables the button
        """
        self.disabled = True
    
    def toggle_disabled(self):
        """
        Toggles the button's disabled
        """
        self.disabled = not self.disabled
    
    def get_mouse_button(self):
        """
        Gets the button's mouse button

        :return: int
        """
        return self.mouse_button

    def set_mouse_button(self, mouse_button):
        """
        Sets the button's mouse button

        :param mouse_button: int
        """
        self.mouse_button = mouse_button

    def draw(self):
        """
        Draws the button
        """
        disabled_color = self.disabled_color
        surface = self.surface
        label_horizontal = self.label_horizontal
        label_vertical = self.label_vertical
        text = self.text
        rect = self.rect
        font = self.font
        if self.is_active() and not self.is_disabled():
            pygame.draw.rect(surface, self.active_background, self.rect)
            Label(surface, text, rect, self.active_color, font, align_horizontal=label_horizontal, align_vertical=label_vertical).draw()
        elif self.is_touching_mouse():
            pygame.draw.rect(surface, self.hover_background, self.rect)
            Label(surface, text, rect, self.hover_color, font, align_horizontal=label_horizontal, align_vertical=label_vertical).draw()
        elif self.disabled:
            pygame.draw.rect(surface, self.disabled_background, self.rect)
            Label(surface, text, rect, disabled_color, font, align_horizontal=label_horizontal, align_vertical=label_vertical).draw()
        else:
            pygame.draw.rect(surface, self.background, self.rect)
            Label(surface, text, rect, self.color, font, align_horizontal=label_horizontal, align_vertical=label_vertical).draw()

    def update(self):
        """
        Updates the button
        """
        self.on_click()
        self.draw()
