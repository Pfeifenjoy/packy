from __future__ import annotations

from packy.shape import Shape
from packy.vector import RelativeVector


class Box(Shape):
    position: RelativeVector
    dimensions: RelativeVector

    def __init__(self: Box, position: RelativeVector, dimensions: RelativeVector) -> None:
        self.position = position
        self.dimensions = dimensions

    def inside(self: Box, point: RelativeVector) -> bool:
        return point.get_x() >= self.position.get_x() \
            and point.get_y() >= self.position.get_y() \
            and point.get_x() <= self.position.add(self.dimensions).get_x() \
            and point.get_y() <= self.position.add(self.dimensions).get_y()

    def center(self: Box) -> RelativeVector:
        return self.position.add(self.dimensions.scale(0.5))

    def __str__(self: Box) -> str:
        return f"Box({ self.position }, { self.dimensions })"
