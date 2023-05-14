from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RelativeCoordinate:
    """
    Relative coordinates are used to have a screen size independent coordinate system.
    Both the X and Y-Axis are referenced by a value between 0 and 100.
    """

    x_position: int

    y_position: int

    def __init__(self: RelativeCoordinate, x_position: int, y_position: int):
        self.set_x(x_position)
        self.set_y(y_position)

    def set_x(self: RelativeCoordinate, x_position) -> None:
        assert x_position >= 0
        assert x_position <= 100
        self.x_position = x_position

    def set_y(self: RelativeCoordinate, y_position) -> None:
        assert y_position >= 0
        assert y_position <= 100
        self.y_position = y_position

    def get_x(self: RelativeCoordinate) -> int:
        return self.x_position

    def get_y(self: RelativeCoordinate) -> int:
        return self.y_position


@dataclass
class AbsoluteCoordinate:
    """
    An absolute coordinate is used to reference an actual position on the canvas.
    """

    x_position: int

    y_position: int
