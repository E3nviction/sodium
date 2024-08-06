class Signal:
    def __init__(self, value=None):
        self._value = value

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

widget_pressed = Signal(0)