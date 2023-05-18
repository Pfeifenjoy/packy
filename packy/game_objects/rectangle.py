from __future__ import annotations

from typing import Optional
from tkinter import Canvas

from packy.game_object import GameObject
from packy.context import Context
from packy.shapes import Box


class Rectangle(GameObject):
    box: Box

    fill: Optional[str]
    outline: Optional[str]

    def __init__(
            self: Rectangle,
            context: Context,
            box: Box,
            fill: Optional[str] = None,
            outline: Optional[str] = None
    ) -> None:
        super().__init__(context)
        self.box = box
        self.fill = fill
        self.outline = outline

    def draw(self: Rectangle, canvas: Canvas) -> None:
        absolute_position = self.context.coordinate_system.absolute(self.box.position)
        absolute_dimensions = self.context.coordinate_system.absolute(self.box.dimensions)

        canvas.create_rectangle(
            absolute_position.get_x(),
            absolute_position.get_y(),
            absolute_position.add(absolute_dimensions).get_x(),
            absolute_position.add(absolute_dimensions).get_y(),
            fill=self.fill or "white",
            outline=self.outline or "black"
        )
