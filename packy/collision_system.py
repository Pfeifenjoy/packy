from __future__ import annotations

from typing import Set, cast
from abc import ABC, abstractmethod

from .coordinate_system import CoordinateSystem
from .shape import Shape
from .shapes import Box
from .shape_types import ShapeTypes
from .vector import RelativeVector


class Collidable(ABC):

    @abstractmethod
    def get_shape(self: Collidable) -> Shape:
        raise NotImplementedError()


class Actor(Collidable):

    @abstractmethod
    def handle_collision(self: Actor, other: Collidable) -> None:
        raise NotImplementedError()



class CollisionSystem:
    coordinate_system: CoordinateSystem

    collidables: Set[Collidable]
    actors: Set[Actor]


    def __init__(self: CollisionSystem, coordinate_system: CoordinateSystem) -> None:
        self.coordinate_system = coordinate_system

        self.collidables = set()
        self.actors = set()

    def update(self: CollisionSystem) -> None:
        for actor in self.actors:
            for target in self.collidables:
                if self.collides(actor.get_shape(), target.get_shape()):
                    actor.handle_collision(target)

    def collides(self: CollisionSystem, shape1: Shape, shape2: Shape) -> bool:
        if shape1.shape_type == ShapeTypes.BOX and shape2.shape_type == ShapeTypes.BOX:
            return self.collides_box(cast(Box, shape1), cast(Box, shape2))

        raise NotImplementedError()

    def collides_box(self: CollisionSystem, box1: Box, box2: Box) -> bool:
        position = box1.get_position()
        dimensions = box1.get_dimensions()

        top_left = position
        top_right = position.add(RelativeVector(dimensions.get_x(), 0))
        bottom_left = position.add(RelativeVector(0, dimensions.get_y()))
        bottom_right = position.add(dimensions)

        return box2.inside(top_left) or box2.inside(top_right) \
            or box2.inside(bottom_left) or box2.inside(bottom_right)
