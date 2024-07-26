"""
Frame widget module
"""
import pygame
from .. import constants, common
from .label import Label

class Frame:
    """
    A Frame widget.
    """
    def __init__(
        self,
        surface,
        text,
        rect=(0, 0, 0, 0),
        color="theme",
        background="theme",
        disabled_color="theme",
        disabled_background="theme",
        font=None,
        font_family=None,
        font_size=20,
        label_horizontal="center",
        label_vertical="center",
        disabled=False,
        ):
        """
        Initializes the Frame

        :param surface: Surface
        :param text: str
        :param rect: tuple
        :param color: Color
        :param background: Color
        :param disabled_color: Color
        :param disabled_background: Color
        :param font: Font
        :param font_family: str
        :param font_size: int
        :param label_horizontal: str [left, center, right]
        :param label_vertical: str [top, center, bottom]
        :param disabled: bool
        """
        super().__init__()
        self.surface = surface
        self.text = text
        self.rect = constants.Rect(rect)
        self.color = common.set_color(color, "FOREGROUND")
        self.background = common.set_color(background, "BACKGROUND_SECONDARY")
        self.disabled_color = common.set_color(disabled_color, "FOREGROUND_DISABLED")
        self.disabled_background = common.set_color(disabled_background, "BACKGROUND_SECONDARY_DISABLED")
        self.font = font
        self.font_family = font_family
        self.font_size = font_size
        self.label_horizontal = label_horizontal
        self.label_vertical = label_vertical
        self.disabled = disabled

        if font is None:
            self.font = common.set_font(font_family, font_size)

    def is_disabled(self):
        """
        Checks if the Frame is disabled

        :return: bool
        """
        return self.disabled

    def set_text(self, text):
        """
        Sets the Frame's text

        :param text: str
        """
        self.text = text

    def get_text(self):
        """
        Gets the Frame's text

        :return: str
        """
        return self.text

    def get_rect(self):
        """
        Gets the Frame's rect

        :return: Rect
        """
        return self.rect

    def get_size(self):
        """
        Gets the Frame's size

        :return: tuple
        """
        return self.font_family.size(self.text)

    def get_width(self):
        """
        Gets the Frame's width

        :return: int
        """
        return self.get_size()[0]

    def get_height(self):
        """
        Gets the Frame's height

        :return: int
        """
        return self.get_size()[1]

    def set_rect(self, rect):
        """
        Sets the Frame's rect

        :param rect: Rect
        """
        self.rect = constants.Rect(rect)

    def set_color(self, color):
        """
        Sets the Frame's color

        :param color: Color
        """
        self.color = common.set_color(color, "FOREGROUND")

    def set_background(self, color):
        """
        Sets the Frame's background

        :param color: Color
        """
        self.background = common.set_color(color, "ACCENT")

    def set_disabled(self, disabled):
        """
        Sets the Frame's disabled

        :param disabled: bool
        """
        self.disabled = disabled
    
    def get_disabled(self):
        """
        Gets the Frame's disabled status

        :return: bool
        """
        return self.disabled

    def set_disabled_color(self, color):
        """
        Sets the Frame's disabled color

        :param color: Color
        """
        self.disabled_color = common.set_color(color, "FOREGROUND_DISABLED")

    def set_disabled_background(self, color):
        """
        Sets the Frame's disabled background

        :param color: Color
        """
        self.disabled_background = common.set_color(color, "ACCENT_DISABLED")

    def set_font(self, font_family, font_size):
        """
        Sets the Frame's font

        :param font: str
        :param font_size: int
        """
        self.font = common.set_font(font_family, font_size)

    def set_label_horizontal(self, horizontal):
        """
        Sets the Frame's label horizontal

        :param horizontal: str
        """
        self.label_horizontal = horizontal

    def set_label_vertical(self, vertical):
        """
        Sets the Frame's label vertical

        :param vertical: str
        """
        self.label_vertical = vertical

    def get_label_horizontal(self):
        """
        Gets the Frame's label horizontal

        :return: str
        """
        return self.label_horizontal

    def get_label_vertical(self):
        """
        Gets the Frame's label vertical

        :return: str
        """
        return self.label_vertical

    def get_font(self):
        """
        Gets the Frame's font

        :return: str
        """
        return self.font
    
    def enable(self):
        """
        Enables the Frame
        """
        self.disabled = False

    def disable(self):
        """
        Disables the Frame
        """
        self.disabled = True

    def toggle_disabled(self):
        """
        Toggles the Frame's disabled
        """
        self.disabled = not self.disabled

    def draw(self):
        """
        Draws the Frame
        """
        surface = self.surface
        label_horizontal = self.label_horizontal
        label_vertical = self.label_vertical
        text = self.text
        font = self.font
        if self.disabled:
            pygame.draw.rect(surface, self.disabled_background, self.rect)
            Label(surface, text, self.rect, self.disabled_color, font, align_horizontal=label_horizontal, align_vertical=label_vertical).draw()
        else:
            pygame.draw.rect(surface, self.background, self.rect)
            Label(surface, text, self.rect, self.color, font, align_horizontal=label_horizontal, align_vertical=label_vertical).draw()

    def update(self):
        """
        Updates the Frame
        """
        self.draw()
