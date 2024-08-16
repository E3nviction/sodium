from .. import cache

class Screen:
    def __init__(self, surface) -> None:
        self.surface = surface
    
    def set(self) -> None:
        cache.screen = self.surface

    def get_surface(self) -> object:
        return self.surface