from __future__ import annotations

from abc import abstractmethod
from tkinter import Canvas

from .context import Context
from .game_object import GameObject
from .game_objects import Rectangle
from .vector import RelativeVector
from .shapes import Box


class Scene(GameObject):

    rectangle: Rectangle

    def __init__(self: Scene, context: Context) -> None:
        super().__init__(context)

        self.rectangle = Rectangle(
            context, Box(RelativeVector(0, 0), RelativeVector(1, 1)),
            fill="white", outline="white"
        )

    @abstractmethod
    def get_name(self: Scene) -> str:
        raise NotImplementedError()

    def draw(self: Scene, canvas: Canvas) -> None:
        self.rectangle.draw(canvas)
