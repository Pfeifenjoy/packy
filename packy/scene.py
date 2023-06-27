from __future__ import annotations

from abc import abstractmethod
import pygame
from pygame import Surface

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
            fill=pygame.Color(255, 255, 255), outline=pygame.Color(255, 255, 255)
        )

    @abstractmethod
    def get_name(self: Scene) -> str:
        raise NotImplementedError()

    def draw(self: Scene, canvas: Surface) -> None:
        self.rectangle.draw(canvas)
