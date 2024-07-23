"""
Label widget module
"""
from .. import constants, common

class FreeLabel:
    """
    A label widget that displays text on a surface without any rendering constraints.
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
        align_horizontal="center",
        align_vertical="center",
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
        :param align_horizontal: bool
        :param align_vertical: bool
        """
        super().__init__()
        self.surface = surface
        self.text = text
        self.rect = constants.Rect(rect)
        self.color = common.set_color(color, "FOREGROUND")
        self.font = font
        self.font_family = font_family
        self.font_size = font_size
        self.align_horizontal = align_horizontal
        self.align_vertical = align_vertical

        if font is None:
            self.font = common.set_font(font_family, font_size)

    def draw(self):
        """
        Draws the label
        """
        if self.font is None:
            self.font = common.set_font(self.font_family, self.font_size)

        new_rect = [0, 0, 0, 0]

        if self.align_horizontal == "center":
            new_rect[0] = self.rect.w / 2 + self.rect.x - self.font.size(self.text)[0] / 2
        elif self.align_horizontal == "right":
            new_rect[0] = self.rect.w + self.rect.x - self.font.size(self.text)[0]
        elif self.align_horizontal == "left":
            new_rect[0] = self.rect.x
        else:
            raise ValueError(f"align_x must be 'left', 'right', or 'center' and not '{self.align_horizontal}'")
        if self.align_vertical == "center":
            new_rect[1] = self.rect.h / 2 + self.rect.y - self.font.get_height() / 2
        elif self.align_vertical == "bottom":
            new_rect[1] = self.rect.h + self.rect.y - self.font.get_height()
        elif self.align_vertical == "top":
            new_rect[1] = self.rect.y
        else:
            raise ValueError(f"align_y must be 'top', 'bottom', or 'center' and not '{self.align_vertical}'")

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

    def set_rect(self, rect):
        """
        Sets the label's rect

        :param rect: Rect
        """
        self.rect = constants.Rect(rect)

    def get_rect(self):
        """
        Gets the label's rect

        :return: Rect
        """
        return self.rect

    def get_text_size(self):
        """
        Gets the label's size

        :return: tuple
        """
        return self.font.size(self.text)

    def get_text_width(self):
        """
        Gets the label's width

        :return: int
        """
        return self.get_text_size()[0]

    def get_text_height(self):
        """
        Gets the label's height

        :return: int
        """
        return self.get_text_size()[1]

    def get_x(self):
        """
        Gets the label's x

        :return: int
        """
        return self.rect.x

    def get_y(self):
        """
        Gets the label's y

        :return: int
        """
        return self.rect.y

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

    def get_width(self):
        """
        Gets the label's width

        :return: int
        """
        return self.rect.w

    def get_height(self):
        """
        Gets the label's height

        :return: int
        """
        return self.rect.h

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

    def get_color(self):
        """
        Gets the label's color

        :return: Color
        """
        return self.color

    def set_color(self, color):
        """
        Sets the label's color

        :param color: Color
        """
        self.color = common.set_color(color, "FOREGROUND")

    def get_font(self):
        """
        Gets the label's font

        :return: str
        """
        return self.font

    def set_font(self, font_family, font_size):
        """
        Sets the label's font

        :param font: str
        """
        self.font = common.set_font(font_family, font_size)

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

    def set_font_family(self, font_family):
        """
        Sets the label's font family

        :param font_family: str
        """
        self.font_family = font_family

    def set_font_size(self, font_size):
        """
        Sets the label's font size

        :param font_size: int
        """
        self.font_size = font_size


    def get_align_horizontal(self):
        """
        Gets the label's horizontal alignment

        :return: str
        """
        return self.align_horizontal

    def get_align_vertical(self):
        """
        Gets the label's vertical alignment

        :return: str
        """
        return self.align_vertical

    def get_align(self):
        """
        Gets the label's alignment

        :return: tuple
        """
        return self.get_align_horizontal(), self.get_align_vertical()

    def set_align_horizontal(self, align_horizontal):
        """
        Sets the label's horizontal alignment

        :param align_horizontal: str
        """
        self.align_horizontal = align_horizontal

    def set_align_vertical(self, align_vertical):
        """
        Sets the label's vertical alignment

        :param align_vertical: str
        """
        self.align_vertical = align_vertical

    def set_align(self, align_horizontal, align_vertical):
        """
        Sets the label's alignment

        :param align_horizontal: str
        :param align_vertical: str
        """
        self.set_align_horizontal(align_horizontal)
        self.set_align_vertical(align_vertical)

    def update(self):
        """
        Updates the label
        """
        self.draw()
