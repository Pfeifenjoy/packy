from __future__ import annotations

from .settings import Settings
from .vector import Vector


class CoordinateSystem:
    settings: Settings

    def __init__(self: CoordinateSystem, settings: Settings):
        self.settings = settings

    def absolute(self: CoordinateSystem, vector: Vector) -> Vector:
        return Vector(
            self.get_x(vector.get_x()),
            self.get_y(vector.get_y())
        )

    def relative(self: CoordinateSystem, vector: Vector) -> Vector:
        return Vector(
            self.relative_x(vector.get_x()),
            self.relative_y(vector.get_y())
        )

    def get_width(self: CoordinateSystem) -> int:
        return self.settings.width

    def get_height(self: CoordinateSystem) -> int:
        return self.settings.height

    def get_x(self: CoordinateSystem, x_position: int) -> int:
        return self.translate_x(x_position)

    def get_y(self: CoordinateSystem, y_position: int) -> int:
        return self.translate_y(y_position)

    def translate_x(self: CoordinateSystem, x_value: int) -> int:
        return int(self.settings.width * (x_value / 100))

    def translate_y(self: CoordinateSystem, y_value: int) -> int:
        return int(self.settings.height * (y_value / 100))

    def relative_x(self: CoordinateSystem, x: int) -> int:
        return int((x / self.settings.width) * 100)

    def relative_y(self: CoordinateSystem, y: int) -> int:
        return int((y / self.settings.height) * 100)
