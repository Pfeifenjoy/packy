from __future__ import annotations

from typing import Optional
from pygame import Surface, draw, Rect, Color

from packy.game_object import GameObject
from packy.context import Context
from packy.shapes import Box


class Rectangle(GameObject):
    box: Box

    fill: Color
    outline: Color
    outline_width: int

    def __init__(
            self: Rectangle,
            context: Context,
            box: Box,
            fill: Optional[Color] = None,
            outline: Optional[Color] = None
    ) -> None:
        super().__init__(context)
        self.box = box
        self.fill = fill or Color(0, 0, 0)
        self.outline = outline or Color(0, 0, 0)
        self.outline_width = 1

    def draw(self: Rectangle, canvas: Surface) -> None:
        absolute_position = self.context.coordinate_system.absolute(self.box.position)
        absolute_dimensions = self.context.coordinate_system.absolute(self.box.dimensions)

        draw.rect(canvas, self.outline, Rect(
            absolute_position.get_x(),
            absolute_position.get_y(),
            absolute_dimensions.get_x(),
            absolute_dimensions.get_y()
        ))
        draw.rect(canvas, self.fill, Rect(
            absolute_position.get_x() + self.outline_width,
            absolute_position.get_y() + self.outline_width,
            absolute_dimensions.get_x() - 2 * self.outline_width,
            absolute_dimensions.get_y() - 2 * self.outline_width
        ))
