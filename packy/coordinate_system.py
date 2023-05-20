from __future__ import annotations

from .settings import Settings
from .vector import RelativeVector, AbsoluteVector


class CoordinateSystem:
    settings: Settings

    def __init__(self: CoordinateSystem, settings: Settings):
        self.settings = settings

    def absolute(self: CoordinateSystem, vector: RelativeVector) -> AbsoluteVector:
        return AbsoluteVector(
            self.get_x(vector.get_x()),
            self.get_y(vector.get_y())
        )

    def relative(self: CoordinateSystem, vector: AbsoluteVector) -> RelativeVector:
        return RelativeVector(
            self.relative_x(vector.get_x()),
            self.relative_y(vector.get_y())
        )

    def get_width(self: CoordinateSystem) -> int:
        return self.settings.width

    def get_height(self: CoordinateSystem) -> int:
        return self.settings.height

    def get_x(self: CoordinateSystem, x_position: int) -> int:
        return self.absolute_x(x_position)

    def get_y(self: CoordinateSystem, y_position: int) -> int:
        return self.absolute_y(y_position)

    def absolute_x(self: CoordinateSystem, x: int) -> int:
        return int(self.settings.width * (x / 1000000))

    def absolute_y(self: CoordinateSystem, y: int) -> int:
        return int(self.settings.height * (y / 1000000))

    def relative_x(self: CoordinateSystem, x: int) -> int:
        return int(x / self.settings.width * 1000000)

    def relative_y(self: CoordinateSystem, y: int) -> int:
        return int(y / self.settings.height * 1000000)

    def quad(self: CoordinateSystem, x: int) -> RelativeVector:
        return RelativeVector(
            x,
            int(x * self.get_ratio())
        )

    def get_ratio(self: CoordinateSystem) -> float:
        return self.settings.width / self.settings.height
