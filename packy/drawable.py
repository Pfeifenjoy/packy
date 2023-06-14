from __future__ import annotations

from abc import ABC

from tkinter import Canvas


class Drawable(ABC):

    def draw(self: Drawable, canvas: Canvas) -> None:
        """
        Method to be overriden for drawings.
        """
