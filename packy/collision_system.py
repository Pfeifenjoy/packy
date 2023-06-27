from __future__ import annotations

from typing import cast

from .coordinate_system import CoordinateSystem
from .shape import Shape
from .shapes import Box
from .shape_types import ShapeTypes
from .vector import RelativeVector


class CollisionSystem:
    coordinate_system: CoordinateSystem

    def __init__(self: CollisionSystem, coordinate_system: CoordinateSystem) -> None:
        self.coordinate_system = coordinate_system

    def collides(self: CollisionSystem, shape1: Shape, shape2: Shape) -> bool:
        if shape1.shape_type == ShapeTypes.BOX and shape2.shape_type == ShapeTypes.BOX:
            return self.collides_box(cast(Box, shape1), cast(Box, shape2))

        raise NotImplementedError()

    def collides_box(self: CollisionSystem, box1: Box, box2: Box) -> bool:
        return self.any_corner_inside(box1, box2) or self.any_corner_inside(box2, box1)

    def any_corner_inside(self: CollisionSystem, box1: Box, box2: Box) -> bool:
        position = box1.get_position()
        dimensions = box1.get_dimensions()

        top_left = position
        top_right = position.add(RelativeVector(dimensions.get_x(), 0))
        bottom_left = position.add(RelativeVector(0, dimensions.get_y()))
        bottom_right = position.add(dimensions)

        return box2.inside(top_left) or box2.inside(top_right) \
            or box2.inside(bottom_left) or box2.inside(bottom_right)
