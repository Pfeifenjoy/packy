from __future__ import annotations

from tkinter.font import Font
from typing import Callable

from packy.game_object import StructuralGameObject
from packy.context import Context
from packy.vector import Vector
from packy.shapes import Box
from packy.game_objects.button import Button
from packy.game_objects.text import Text
from packy.scene import Scene


class Menu(Scene, StructuralGameObject):

    def __init__(
            self: Menu,
            context: Context,
            on_play: Callable[[], None]
    ) -> None:
        super().__init__(context)

        self.add_child(
            Text(
                context,
                Vector(50, 20),
                "Packy",
                font=Font(size=self.context.coordinate_system.translate_y(10))
            )
        )

        self.add_child(
            Button(
                context,
                Box(
                    Vector(int(100/3), 35),
                    Vector(int(100/3), 10)
                ),
                "Start",
                lambda point: on_play()
            )
        )

    def get_name(self: Menu) -> str:
        return "Menu"
