from __future__ import annotations

from tkinter.font import Font
from typing import Callable

from packy.game_object import StructuralGameObject
from packy.context import Context
from packy.vector import RelativeVector
from packy.shapes import Box
from packy.game_objects.button import Button
from packy.game_objects.text import Text
from packy.scene import Scene


class Menu(StructuralGameObject, Scene):

    def __init__(
            self: Menu,
            context: Context,
            on_play: Callable[[], None]
    ) -> None:
        super().__init__(context)

        self.add_child(
            Text(
                context,
                RelativeVector(0.5, 0.2),
                "Packy",
                font=Font(size=self.context.coordinate_system.absolute_y(0.1))
            )
        )

        self.add_child(
            Button(
                context,
                Box(
                    RelativeVector(1/3, 0.35),
                    RelativeVector(1/3, 0.10)
                ),
                "Start",
                lambda point: on_play()
            )
        )

    def get_name(self: Menu) -> str:
        return "Menu"
