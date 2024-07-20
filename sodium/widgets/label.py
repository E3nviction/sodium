"""
Label widget module
"""
from .. import constants, common

class Label:
    """
    A label widget
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
        pos_x="center",
        pos_y="center",
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
        :param pos_x: bool
        :param pos_y: bool
        """
        super().__init__()
        self.surface = surface
        self.text = text
        self.rect = constants.Rect(rect)
        self.color = common.set_color(color, "FOREGROUND")
        self.font = font
        self.font_family = font_family
        self.font_size = font_size
        self.pos_x = pos_x
        self.pos_y = pos_y

        if font is None:
            self.font = common.set_font(font_family, font_size)

    def draw(self):
        """
        Draws the label
        """
        if self.font is None:
            self.font = common.set_font(self.font_family, self.font_size)

        new_rect = [0, 0, 0, 0]

        if self.pos_x == "center":
            new_rect[0] = self.rect.w / 2 + self.rect.x - self.font.size(self.text)[0] / 2
        elif self.pos_x == "right":
            new_rect[0] = self.rect.w + self.rect.x - self.font.size(self.text)[0]
        elif self.pos_x == "left":
            pass
        else:
            raise ValueError(f"pos_x must be 'left', 'right', or 'center' and not '{self.pos_x}'")
        if self.pos_y == "center":
            new_rect[1] = self.rect.h / 2 + self.rect.y - self.font.get_height() / 2
        elif self.pos_y == "bottom":
            new_rect[1] = self.rect.h + self.rect.y - self.font.get_height()
        elif self.pos_y == "top":
            pass
        else:
            raise ValueError(f"pos_y must be 'top', 'bottom', or 'center' and not '{self.pos_y}'")
        self.surface.blit(self.font.render(self.text, True, self.color), new_rect)

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

    def get_pos_x(self):
        """
        Gets the label's pos x

        :return: bool
        """
        return self.pos_x

    def get_pos_y(self):
        """
        Gets the label's pos y

        :return: bool
        """
        return self.pos_y

    def set_pos_x(self, pos_x):
        """
        Sets the label's pos x

        :param pos_x: bool
        """
        self.pos_x = pos_x

    def set_pos_y(self, pos_y):
        """
        Sets the label's pos y

        :param pos_y: bool
        """
        self.pos_y = pos_y

    def set_pos(self, pos_x, pos_y):
        """
        Sets the label's pos

        :param pos_x: bool
        :param pos_y: bool
        """
        self.set_pos_x(pos_x)
        self.set_pos_y(pos_y)

    def update(self):
        """
        Updates the label
        """
        self.draw()
