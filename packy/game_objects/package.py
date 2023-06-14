from __future__ import annotations

from tkinter import Canvas
from typing import Callable

from packy.game_object import GameObject
from packy.context import Context
from packy.vector import RelativeVector
from packy.shapes import Box
from packy.update import Update

from .rectangle import Rectangle


class Package(GameObject):

    position: RelativeVector
    dimensions: RelativeVector
    on_destroy: Callable[[Package], None]

    velocity: int
    direction: RelativeVector

    def __init__(
            self: Package,
            context: Context,
            position: RelativeVector,
            width: int,
            velocity: int,
            on_destroy: Callable[[Package], None]
    ) -> None:
        super().__init__(context)

        self.position = position
        self.dimensions = RelativeVector(
            width, int(self.context.coordinate_system.get_ratio() * width)
        )
        self.velocity = velocity
        self.on_destroy = on_destroy
        self.direction = RelativeVector(0, 1)

    def get_motion(self: Package, update: Update) -> RelativeVector:
        return self.direction.resize(
            int(self.velocity * (update.elapsed_time.microseconds / 1000000))
        )

    def update(self: Package, update: Update) -> None:
        self.position = self.position.add(self.get_motion(update))

        if self.position.get_y() > 1000000:
            self.on_destroy(self)

    def get_box(self: Package) -> Box:
        return Box(self.position, self.dimensions)

    def draw(self: Package, canvas: Canvas) -> None:
        rectangle = Rectangle(self.context, self.get_box(), fill="blue")
        rectangle.draw(canvas)
