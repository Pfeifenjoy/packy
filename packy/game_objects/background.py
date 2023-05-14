from __future__ import annotations

from tkinter import Canvas
from packy.game_object import GameObject
from packy.context import Context


class Background(GameObject):
    def __init__(self: Background, context: Context):
        super().__init__(context)

    def draw(self: Background, canvas: Canvas) -> None:
        width = self.context.coordinate_system.get_width()
        height = self.context.coordinate_system.get_height()

        canvas.create_rectangle(0, 0, width, height, fill="#01A7E1")
