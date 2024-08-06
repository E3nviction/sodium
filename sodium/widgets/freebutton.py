"""
FreeButton widget module
"""
import pygame
from .. import constants, common
from .label import Label
from .. import signal as signal_module
from .. import cache

# pylint: disable=missing-docstring
class FreeButton:
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
        super().__init__()
        self.surface = surface
        self.text = text
        self.rect = constants.Rect(rect)
        self.color = common.set_color(color, "ACCENT_FOREGROUND")
        self.background = common.set_color(background, "ACCENT")
        self.hover_color = common.set_color(hover_color, "ACCENT_FOREGROUND")
        self.hover_background = common.set_color(hover_background, "ACCENT_HOVER")
        self.active_color = common.set_color(active_color, "ACCENT_FOREGROUND")
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
        self.mouse_button = mouse_button

        self.id = common.widget_get_id()
        self.widget_id = 0
        self.name = ""
        self.locked = False
        self.button_state = None

        cache.widgets.append(self.id)

        if font is None:
            self.font = common.set_font(font_family, font_size)

    def is_touching_mouse(self) -> bool:
        return self.rect.collidepoint(pygame.mouse.get_pos()) and not self.disabled
    def is_active(self) -> bool:
        return self.is_touching_mouse() and pygame.mouse.get_pressed()[self.mouse_button] and not self.disabled
    def is_locked(self) -> bool:
        return self.locked
    def is_disabled(self) -> bool:
        return self.disabled

    def get_on_click_func(self) -> tuple:
        return self.on_click_func
    def set_on_click_func(self, func) -> None:
        self.on_click_func = func

    def get_text(self) -> str:
        return self.text
    def set_text(self, text) -> None:
        self.text = text

    def get_on_click_args(self) -> tuple:
        return self.on_click_args
    def set_on_click_args(self, args) -> None:
        self.on_click_args = args

    def get_width(self) -> int:
        return self.rect.width
    def set_width(self, width) -> None:
        self.rect.width = width

    def get_height(self) -> int:
        return self.rect.height
    def set_height(self, height) -> None:
        self.rect.height = height

    def get_rect(self) -> tuple:
        return self.rect
    def set_rect(self, rect) -> None:
        self.rect = constants.Rect(rect)

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

    def get_hover_color(self) -> str:
        return self.hover_color
    def set_hover_color(self, color) -> None:
        self.hover_color = common.set_color(color, "FOREGROUND")

    def get_hover_background(self) -> str:
        return self.hover_background
    def set_hover_background(self, color) -> None:
        self.hover_background = common.set_color(color, "ACCENT_HOVER")

    def get_active_color(self) -> str:
        return self.active_color
    def set_active_color(self, color) -> None:
        self.active_color = common.set_color(color, "FOREGROUND")

    def get_active_background(self) -> str:
        return self.active_background
    def set_active_background(self, color) -> None:
        self.active_background = common.set_color(color, "ACCENT_ACTIVE")

    def get_locked(self) -> bool:
        return self.locked
    def set_locked(self, locked) -> None:
        self.locked = locked

    def get_label_horizontal(self) -> str:
        return self.label_horizontal
    def set_label_horizontal(self, horizontal) -> None:
        self.label_horizontal = horizontal
    def get_label_vertical(self) -> str:
        return self.label_vertical
    def set_label_vertical(self, vertical) -> None:
        self.label_vertical = vertical

    def get_font(self) -> str:
        return self.font
    def set_font(self, font_family, font_size) -> None:
        self.font = common.set_font(font_family, font_size)

    def enable(self) -> None:
        self.disabled = False
    def disable(self) -> None:
        self.disabled = True

    def toggle_disabled(self) -> None:
        self.disabled = not self.disabled

    def get_mouse_button(self) -> int:
        return self.mouse_button
    def set_mouse_button(self, mouse_button) -> None:
        self.mouse_button = mouse_button

    def get_id(self) -> int:
        return self.id
    def set_id(self, _id) -> None:
        self.id = _id
    
    def get_name(self) -> str:
        return self.name
    def set_name(self, name) -> None:
        self.name = name

    def get_state(self) -> str:
        if self.button_state is None:
            return "normal"
        if self.button_state:
            return "pressed"
        else:
            return "released"
    def set_state(self, state) -> None:
        if state == "normal":
            self.button_state = None
        elif state == "pressed":
            self.button_state = True
        elif state == "released":
            self.button_state = False
    def check_click(self) -> bool:
        if self.is_active() and not self.is_locked():
            self.locked = True
            self.button_state = True
            signal_module.widget_pressed.set_value(self.id)
            return True
        if not pygame.mouse.get_pressed()[self.mouse_button] and self.is_locked():
            if self.is_touching_mouse() and signal_module.widget_pressed.get_value() == self.id:
                if self.on_click_func:
                    if self.on_click_args:
                        self.on_click_func(*self.on_click_args)
                    else:
                        self.on_click_func()
                signal_module.widget_pressed.set_value(0)
            self.locked = False
            self.button_state = False
            return False
        if not self.is_active():
            self.button_state = None
            return None
    def draw(self) -> None:
        if pygame.mouse.get_pressed()[self.mouse_button] and self.is_locked() and not self.is_disabled():
            pygame.draw.rect(self.surface, self.active_background, self.rect)
            Label(self.surface, self.text, self.rect, self.active_color, self.font, align_horizontal=self.label_horizontal, align_vertical=self.label_vertical).draw()
        elif self.is_touching_mouse() and not self.is_disabled():
            pygame.draw.rect(self.surface, self.hover_background, self.rect)
            Label(self.surface, self.text, self.rect, self.hover_color, self.font, align_horizontal=self.label_horizontal, align_vertical=self.label_vertical).draw()
        elif self.is_disabled():
            pygame.draw.rect(self.surface, self.disabled_background, self.rect)
            Label(self.surface, self.text, self.rect, self.disabled_color, self.font, align_horizontal=self.label_horizontal, align_vertical=self.label_vertical).draw()
        else:
            pygame.draw.rect(self.surface, self.background, self.rect)
            Label(self.surface, self.text, self.rect, self.color, self.font, align_horizontal=self.label_horizontal, align_vertical=self.label_vertical).draw()
    def update(self) -> None:
        self.check_click()
        self.draw()
    def reload_theme(self) -> None:
        self.color = common.set_color("theme", "ACCENT_FOREGROUND")
        self.background = common.set_color("theme", "ACCENT")
        self.hover_color = common.set_color("theme", "ACCENT_FOREGROUND")
        self.hover_background = common.set_color("theme", "ACCENT_HOVER")
        self.active_color = common.set_color("theme", "ACCENT_FOREGROUND")
        self.active_background = common.set_color("theme", "ACCENT_ACTIVE")
        self.disabled_color = common.set_color("theme", "ACCENT_FOREGROUND_DISABLED")
        self.disabled_background = common.set_color("theme", "ACCENT_DISABLED")
