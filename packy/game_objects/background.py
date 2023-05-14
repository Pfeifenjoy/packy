from __future__ import annotations

from tkinter import Canvas
from packy.game_object import GameObject


class Background(GameObject):

    def draw(self: Background, canvas: Canvas) -> None:
        width = canvas.winfo_width()
        height = canvas.winfo_height()

        canvas.create_rectangle(0, 0, width, height, fill="#01A7E1")
