from __future__ import annotations

from typing import cast

from .coordinate_system import CoordinateSystem
from .shape import Shape
from .shapes import Box
from .shape_types import ShapeTypes


class CollisionSystem:
    coordinate_system: CoordinateSystem

    def __init__(self: CollisionSystem, coordinate_system: CoordinateSystem) -> None:
        self.coordinate_system = coordinate_system

    def collides(self: CollisionSystem, shape1: Shape, shape2: Shape) -> bool:
        if shape1.shape_type == ShapeTypes.BOX and shape2.shape_type == ShapeTypes.BOX:
            return self.collides_box(cast(Box, shape1), cast(Box, shape2))

        raise NotImplementedError()

    def collides_box(self: CollisionSystem, box1: Box, box2: Box) -> bool:
        # Add code to check that box1 collides with box 2

        # The function should return True if both boxes overlap and false if they do not.

        return False
