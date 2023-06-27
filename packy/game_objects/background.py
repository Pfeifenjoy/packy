from __future__ import annotations

from pygame import Surface, Color
from packy.game_object import GameObject
from packy.context import Context
from packy.shapes.box import Box
from packy.vector import RelativeVector

from .rectangle import Rectangle


class Background(GameObject):
    rectangle: Rectangle

    def __init__(self: Background, context: Context):
        super().__init__(context)
        self.rectangle = Rectangle(
            context, Box(RelativeVector(0, 0), RelativeVector(1000000, 1000000)),
            fill=Color(255, 255, 255), outline=Color(255, 255, 255)
        )

    def draw(self: Background, canvas: Surface) -> None:
        self.rectangle.draw(canvas)
