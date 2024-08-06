"""
FreeLabel widget module
"""
from .. import constants, common
from .. import cache


# pylint: disable=missing-docstring
class FreeLabel:
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

        self.id = common.widget_get_id()
        self.widget_id = 3
        self.name = ""

        cache.widgets.append(self.id)

        if font is None:
            self.font = common.set_font(font_family, font_size)

    def get_text(self):
        return self.text
    def set_text(self, text):
        self.text = text

    def get_rect(self):
        return self.rect
    def set_rect(self, rect):
        self.rect = constants.Rect(rect)

    def get_text_size(self):
        return self.font.size(self.text)
    def get_text_width(self):
        return self.get_text_size()[0]
    def get_text_height(self):
        return self.get_text_size()[1]

    def get_x(self):
        return self.rect.x
    def set_x(self, x):
        self.rect.x = x

    def get_y(self):
        return self.rect.y
    def set_y(self, y):
        self.rect.y = y

    def get_width(self):
        return self.rect.w
    def set_width(self, width):
        self.rect.w = width

    def get_height(self):
        return self.rect.h
    def set_height(self, height):
        self.rect.h = height

    def get_color(self):
        return self.color
    def set_color(self, color):
        self.color = common.set_color(color, "FOREGROUND")

    def get_font(self):
        return self.font
    def set_font(self, font_family, font_size):
        self.font = common.set_font(font_family, font_size)

    def get_font_family(self) -> str:
        return self.font_family
    def set_font_family(self, font_family) -> None:
        self.font_family = font_family

    def get_font_size(self) -> int:
        return self.font_size
    def set_font_size(self, font_size) -> None:
        self.font_size = font_size

    def get_align_horizontal(self) -> str:
        return self.align_horizontal
    def set_align_horizontal(self, align_horizontal) -> None:
        self.align_horizontal = align_horizontal

    def get_align_vertical(self) -> str:
        return self.align_vertical
    def set_align_vertical(self, align_vertical) -> None:
        self.align_vertical = align_vertical

    def get_align(self) -> tuple:
        return self.get_align_horizontal(), self.get_align_vertical()
    def set_align(self, align_horizontal, align_vertical) -> None:
        self.set_align_horizontal(align_horizontal)
        self.set_align_vertical(align_vertical)

    def get_id(self) -> int:
        return self.id
    def set_id(self, _id) -> None:
        self.id = _id

    def get_name(self) -> str:
        return self.name
    def set_name(self, name) -> None:
        self.name = name

    def draw(self) -> None:
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
        
        self.surface.blit(self.font.render(self.text, True, self.color), new_rect)
    def update(self) -> None:
        self.draw()
