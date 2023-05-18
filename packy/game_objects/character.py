from __future__ import annotations

from tkinter import Canvas

from packy.game_object import GameObject
from packy.context import Context
from packy.vector import Vector
from packy.shapes import Box

from .rectangle import Rectangle


class Character(GameObject):

    center: Vector
    dimension: Vector

    def __init__(
            self: Character,
            context: Context,
            start_position: Vector
    ) -> None:
        super().__init__(context)

        self.center = start_position
        self.dimension = Vector(5, 5)

    def get_position(self: Character) -> Vector:
        return self.center.minus(self.dimension.scale(0.5))

    def draw(self: Character, canvas: Canvas) -> None:

        body = Rectangle(
            self.context,
            Box(self.get_position(), self.dimension),
            fill="blue"
        )

        body.draw(canvas)
