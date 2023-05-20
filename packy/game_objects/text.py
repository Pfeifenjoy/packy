from __future__ import annotations

from tkinter import Canvas
from tkinter.font import Font
from typing import Optional

from packy.game_object import GameObject
from packy.context import Context
from packy.vector import RelativeVector


class Text(GameObject):
    position: RelativeVector
    text: str
    font: Font

    def __init__(
            self: Text,
            context: Context,
            position: RelativeVector,
            text: str,
            font: Optional[Font]
    ) -> None:
        super().__init__(context)

        self.position = position
        self.text = text
        self.font = font or Font(
            size=self.context.coordinate_system.absolute_y(0.03)
        )

    def draw(self: Text, canvas: Canvas) -> None:
        position = self.context.coordinate_system.absolute(self.position)

        canvas.create_text(
            position.get_x(),
            position.get_y(),
            text=self.text,
            font=self.font
        )
