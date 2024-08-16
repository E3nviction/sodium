import pygame
from .. import constants, common
from .label import Label
from .. import cache


# pylint: disable=missing-docstring
class Frame:
    def __init__(
        self,
        surface="wiscreen",
        label="",
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
        children=None,
        ):
        super().__init__()
        self.surface = surface
        if surface == "wiscreen":
            self.surface = cache.screen
        self.label = label
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

        self.id = common.widget_get_id()
        self.widget_id = 1
        self.name = ""

        self.children = children

        cache.widgets.append(self.id)

        if font is None:
            self.font = common.set_font(font_family, font_size)

    def is_disabled(self) -> bool:
        return self.disabled

    def get_label(self) -> str:
        return self.label
    def set_label(self, label) -> None:
        self.label = label

    def get_rect(self) -> tuple:
        return self.rect
    def set_rect(self, rect) -> None:
        self.rect = constants.Rect(rect)

    def get_width(self) -> int:
        return self.rect.width
    def set_width(self, width) -> None:
        self.rect.width = width

    def get_height(self) -> int:
        return self.rect.height
    def set_height(self, height) -> None:
        self.rect.height = height

    def get_size(self) -> tuple:
        return self.rect.size
    def set_size(self, size) -> None:
        self.rect.size = size

    def get_x(self) -> int:
        return self.rect.x
    def set_x(self, x) -> None:
        self.rect.x = x

    def get_y(self) -> int:
        return self.rect.y
    def set_y(self, y) -> None:
        self.rect.y = y

    def get_position(self) -> tuple:
        return self.rect.topleft
    def set_position(self, position) -> None:
        self.rect.topleft = position

    def get_color(self) -> str:
        return self.color
    def set_color(self, color) -> None:
        self.color = common.set_color(color, "FOREGROUND")

    def get_background(self) -> str:
        return self.background
    def set_background(self, color) -> None:
        self.background = common.set_color(color, "ACCENT")

    def get_disabled(self) -> bool:
        return self.disabled
    def set_disabled(self, disabled) -> None:
        self.disabled = disabled

    def get_disabled_color(self) -> str:
        return self.disabled_color
    def set_disabled_color(self, color) -> None:
        self.disabled_color = common.set_color(color, "FOREGROUND_DISABLED")

    def get_disabled_background(self) -> str:
        return self.disabled_background
    def set_disabled_background(self, color) -> None:
        self.disabled_background = common.set_color(color, "ACCENT_DISABLED")

    def get_font_family(self) -> str:
        return self.font_family
    def set_font_family(self, font_family) -> None:
        self.font_family = font_family

    def set_label_horizontal(self, horizontal) -> None:
        self.label_horizontal = horizontal
    def get_label_horizontal(self) -> str:
        return self.label_horizontal

    def set_label_vertical(self, vertical) -> None:
        self.label_vertical = vertical
    def get_label_vertical(self) -> str:
        return self.label_vertical

    def get_font(self):
        return self.font
    def set_font(self, font_family, font_size) -> None:
        self.font = common.set_font(font_family, font_size)

    def enable(self):
        self.disabled = False
    def disable(self):
        self.disabled = True

    def toggle_disabled(self):
        self.disabled = not self.disabled

    def add_child(self, child):
        self.children.append(child)
    def remove_child(self, child):
        self.children.remove(child)
    def get_childs(self):
        return self.children
    def set_childs(self, childs):
        self.children = childs
    def clear_childs(self):
        self.children = []
    
    def get_id(self) -> int:
        return self.id
    def set_id(self, _id) -> None:
        self.id = _id
    
    def get_name(self) -> str:
        return self.name
    def set_name(self, name) -> None:
        self.name = name
    
    def update_childs_bounding_box(self):
        for child in self.children:
            if hasattr(child, "set_bounding_box"):
                child.set_bounding_box(self.rect)
    def update_childs(self):
        for child in self.children:
            child.update()
    def draw(self):
        if self.disabled:
            pygame.draw.rect(self.surface, self.disabled_background, self.rect)
            Label(self.surface, self.label, self.rect, self.disabled_color, self.font, align_horizontal=self.label_horizontal, align_vertical=self.label_vertical).draw()
        else:
            pygame.draw.rect(self.surface, self.background, self.rect)
            Label(self.surface, self.label, self.rect, self.color, self.font, align_horizontal=self.label_horizontal, align_vertical=self.label_vertical).draw()
    def update(self):
        self.draw()
        self.update_childs_bounding_box()
        self.update_childs()
    def reload_theme(self):
        self.color = common.set_color("theme", "FOREGROUND")
        self.background = common.set_color("theme", "BACKGROUND_SECONDARY")
        self.disabled_color = common.set_color("theme", "FOREGROUND_DISABLED")
        self.disabled_background = common.set_color("theme", "BACKGROUND_SECONDARY_DISABLED")
