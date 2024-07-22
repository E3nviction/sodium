"""
Label widget module
"""
from .. import constants, common

class Label:
    """
    A label widget that displays text on a Pygame surface with rendering constraints.
    The text is clipped to a defined rectangular area.

    methods:
        __init__(self,
            surface,
            text,
            rect=(0, 0, 0, 0),
            color="theme",
            font=None,
            font_family=None,
            font_size=20,
            align_x="center",
            align_y="center"
            )
        draw(self)
        set_text(self, text)
        get_text(self)
        set_rect(self, rect)
        get_rect(self)
        set_color(self, color)
        get_color(self)
        set_font(self, font)
        get_font(self)
        set_font_family(self, font_family)
        get_font_family(self)
        set_font_size(self, font_size)
        get_font_size(self)
        set_align_x(self, align_x)
        get_align_x(self)
        set_align_y(self, align_y)
        get_align_y(self)
        update(self)
    """
    def __init__(
        self,
        surface,
        text,
        rect=(0, 0, 0, 0),
        color="theme",
        font=None,
        font_family=None,
        font_size=20,
        align_x="center",
        align_y="center",
        ):
        """
        Initializes the label

        :param surface: Surface
        :param text: str
        :param rect: tuple
        :param color: Color
        :param font: Font
        :param font_family: str
        :param font_size: int
        :param align_x: bool
        :param align_y: bool
        """
        super().__init__()
        self.surface = surface
        self.text = text
        self.rect = constants.Rect(rect)
        self.color = common.set_color(color, "FOREGROUND")
        self.font = font
        self.font_family = font_family
        self.font_size = font_size
        self.align_x = align_x
        self.align_y = align_y

        if font is None:
            self.font = common.set_font(font_family, font_size)

    def draw(self):
        """
        Draws the label
        """
        if self.font is None:
            self.font = common.set_font(self.font_family, self.font_size)

        new_rect = [0, 0, 0, 0]

        if self.align_x == "center":
            new_rect[0] = self.rect.w / 2 + self.rect.x - self.font.size(self.text)[0] / 2
        elif self.align_x == "right":
            new_rect[0] = self.rect.w + self.rect.x - self.font.size(self.text)[0]
        elif self.align_x == "left":
            new_rect[0] = self.rect.x
        else:
            raise ValueError(f"align_x must be 'left', 'right', or 'center' and not '{self.align_x}'")
        if self.align_y == "center":
            new_rect[1] = self.rect.h / 2 + self.rect.y - self.font.get_height() / 2
        elif self.align_y == "bottom":
            new_rect[1] = self.rect.h + self.rect.y - self.font.get_height()
        elif self.align_y == "top":
            new_rect[1] = self.rect.y
        else:
            raise ValueError(f"align_y must be 'top', 'bottom', or 'center' and not '{self.align_y}'")

        # Save the current clipping area
        old_clip = self.surface.get_clip()

        # Define the clipping area
        self.surface.set_clip(self.rect)

        # Blit the text surface within the rectangle
        self.surface.blit(self.font.render(self.text, True, self.color), new_rect)

        # Restore the old clipping area
        self.surface.set_clip(old_clip)

    def set_text(self, text):
        """
        Sets the label's text

        :param text: str
        """
        self.text = text

    def get_text(self):
        """
        Gets the label's text

        :return: str
        """
        return self.text

    def get_rect(self):
        """
        Gets the label's rect

        :return: Rect
        """
        return self.rect

    def get_size(self):
        """
        Gets the label's size

        :return: tuple
        """
        return self.font.size(self.text)

    def get_width(self):
        """
        Gets the label's width

        :return: int
        """
        return self.get_size()[0]

    def get_height(self):
        """
        Gets the label's height

        :return: int
        """
        return self.get_size()[1]

    def set_rect(self, rect):
        """
        Sets the label's rect

        :param rect: Rect
        """
        self.rect = constants.Rect(rect)

    def set_x(self, x):
        """
        Sets the label's x

        :param x: int
        """
        self.rect.x = x

    def set_y(self, y):
        """
        Sets the label's y

        :param y: int
        """
        self.rect.y = y

    def set_width(self, width):
        """
        Sets the label's width

        :param width: int
        """
        self.rect.w = width

    def set_height(self, height):
        """
        Sets the label's height

        :param height: int
        """
        self.rect.h = height

    def set_color(self, color):
        """
        Sets the label's color

        :param color: Color
        """
        self.color = common.set_color(color, "FOREGROUND")

    def set_font(self, font_family, font_size):
        """
        Sets the label's font

        :param font: str
        """
        self.font = common.set_font(font_family, font_size)

    def get_font(self):
        """
        Gets the label's font

        :return: str
        """
        return self.font

    def get_font_family(self):
        """
        Gets the label's font family

        :return: str
        """
        return self.font_family

    def get_font_size(self):
        """
        Gets the label's font size

        :return: int
        """
        return self.font_size

    def get_align_x(self):
        """
        Gets the label's align x

        :return: bool
        """
        return self.align_x

    def get_align_y(self):
        """
        Gets the label's align y

        :return: bool
        """
        return self.align_y

    def set_align_x(self, align_x):
        """
        Sets the label's align x

        :param align_x: bool
        """
        self.align_x = align_x

    def set_align_y(self, align_y):
        """
        Sets the label's pos y

        :param align_y: bool
        """
        self.align_y = align_y

    def set_align(self, align_x, align_y):
        """
        Sets the label's pos

        :param pos_x: bool
        :param pos_y: bool
        """
        self.set_align_x(align_x)
        self.set_align_y(align_y)

    def update(self):
        """
        Updates the label
        """
        self.draw()
