from __future__ import annotations

from .settings import Settings
from .coordinate import RelativeCoordinate, AbsoluteCoordinate


class CoordinateSystem:
    settings: Settings

    def __init__(self: CoordinateSystem, settings: Settings):
        self.settings = settings

    def absolute(self: CoordinateSystem, coordinate: RelativeCoordinate):
        x_position = self.settings.width * (coordinate.get_x() / 100)
        y_position = self.settings.height * (coordinate.get_y() / 100)

        return AbsoluteCoordinate(x_position, y_position)

    def get_width(self: CoordinateSystem) -> int:
        return self.settings.width

    def get_height(self: CoordinateSystem) -> int:
        return self.settings.height
