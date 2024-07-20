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
        center_x=False,
        center_y=False
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
        :param center_x: bool
        :param center_y: bool
        """
        super().__init__()
        self.surface = surface
        self.text = text
        self.rect = constants.Rect(rect)
        self.color = common.set_color(color, "FOREGROUND")
        self.font = font
        self.font_family = font_family
        self.font_size = font_size
        self.center_x = center_x
        self.center_y = center_y

        if font is None:
            self.font = common.set_font(font_family, font_size)

    def draw(self):
        """
        Draws the label
        """
        if self.font is None:
            self.font = common.set_font(self.font_family, self.font_size)

        if self.center_x:
            self.rect.centerx = self.surface.get_width() // 2
        if self.center_y:
            self.rect.centery = self.surface.get_height() // 2
        self.surface.blit(self.font.render(self.text, True, self.color), self.rect)

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
        return self.font_family.size(self.text)

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
        self.rect = rect

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

    def get_center_x(self):
        """
        Gets the label's center x

        :return: bool
        """
        return self.center_x

    def get_center_y(self):
        """
        Gets the label's center y

        :return: bool
        """
        return self.center_y

    def set_center_x(self, center_x):
        """
        Sets the label's center x

        :param center_x: bool
        """
        self.center_x = center_x

    def set_center_y(self, center_y):
        """
        Sets the label's center y

        :param center_y: bool
        """
        self.center_y = center_y

    def set_center(self, center_x, center_y):
        """
        Sets the label's center

        :param center_x: bool
        :param center_y: bool
        """
        self.set_center_x(center_x)
        self.set_center_y(center_y)

    def update(self):
        """
        Updates the label
        """
        self.draw()
