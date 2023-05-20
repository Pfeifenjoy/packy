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

    def get_x(self: CoordinateSystem, x_position: float) -> int:
        return self.absolute_x(x_position)

    def get_y(self: CoordinateSystem, y_position: float) -> int:
        return self.absolute_y(y_position)

    def absolute_x(self: CoordinateSystem, x: float) -> int:
        return int(self.settings.width * x)

    def absolute_y(self: CoordinateSystem, y: float) -> int:
        return int(self.settings.height * y)

    def relative_x(self: CoordinateSystem, x: int) -> float:
        return x / self.settings.width

    def relative_y(self: CoordinateSystem, y: int) -> float:
        return y / self.settings.height

    def quad(self: CoordinateSystem, x: float) -> RelativeVector:
        return RelativeVector(
            x,
            x * (self.settings.width / self.settings.height)
        )
