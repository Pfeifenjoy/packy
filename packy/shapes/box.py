from __future__ import annotations

from packy.shape import Shape
from packy.vector import Vector


class Box(Shape):
    position: Vector
    dimensions: Vector

    def __init__(self: Box, position: Vector, dimensions: Vector) -> None:
        self.position = position
        self.dimensions = dimensions

    def inside(self: Box, point: Vector) -> bool:
        return point.get_x() >= self.position.get_x() \
            and point.get_y() >= self.position.get_y() \
            and point.get_x() <= self.position.add(self.dimensions).get_x() \
            and point.get_y() <= self.position.add(self.dimensions).get_y()

    def center(self: Box) -> Vector:
        return self.position.add(self.dimensions.scale(0.5))

    def __str__(self: Box) -> str:
        return f"Box({ self.position }, { self.dimensions })"
