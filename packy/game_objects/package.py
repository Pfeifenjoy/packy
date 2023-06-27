from __future__ import annotations

from pygame import Surface, Color
from pygame.font import SysFont, get_default_font

from packy.game_object import GameObject
from packy.context import Context
from packy.vector import RelativeVector
from packy.shapes import Box
from packy.update import Update

from .rectangle import Rectangle
from .text import Text


class Package(GameObject):
    number: int
    position: RelativeVector
    dimensions: RelativeVector

    velocity: int
    direction: RelativeVector

    def __init__(
            self: Package,
            context: Context,
            number: int,
            position: RelativeVector,
            width: int,
            velocity: int,
    ) -> None:
        super().__init__(context)
        self.number = number

        self.position = position
        self.dimensions = RelativeVector(
            width, int(self.context.coordinate_system.get_ratio() * width)
        )
        self.velocity = velocity
        self.direction = RelativeVector(0, 1)

    def get_motion(self: Package, update: Update) -> RelativeVector:
        return self.direction.resize(
            int(self.velocity * (update.elapsed_time.microseconds / 1000000))
        )

    def update(self: Package, update: Update) -> None:
        self.position = self.position.add(self.get_motion(update))

    def get_box(self: Package) -> Box:
        return Box(self.position, self.dimensions)

    def draw(self: Package, canvas: Surface) -> None:
        rectangle = Rectangle(
            self.context,
            self.get_box(),
            fill=Color(160, 117, 88),
            outline=Color(115, 83, 62)
        )
        rectangle.draw(canvas)
        text = Text(
            self.context,
            self.get_box().center(),
            str(self.number),
            SysFont(get_default_font(), 20)
        )
        text.draw(canvas)

    def __hash__(self: Package) -> int:
        return self.number
