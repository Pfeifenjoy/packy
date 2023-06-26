from __future__ import annotations

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
                RelativeVector(500000, 200000),
                "Packy",
            )
        )

        self.add_child(
            Button(
                context,
                Box(
                    RelativeVector(int(1000000/3), 350000),
                    RelativeVector(int(1000000/3), 100000)
                ),
                "Start",
                lambda point: on_play()
            )
        )

    def get_name(self: Menu) -> str:
        return "Menu"
