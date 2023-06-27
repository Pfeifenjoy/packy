from __future__ import annotations

from typing import Callable

from packy.scene import Scene
from packy.game_object import StructuralGameObject
from packy.context import Context
from packy.game_objects import Character, Background, PackageMount, StatusBar
from packy.vector import RelativeVector


class Game(StructuralGameObject, Scene):

    def __init__(self: Game, context: Context, on_game_over: Callable[[], None]) -> None:
        super().__init__(context)

        status_bar = StatusBar(context, on_game_over)
        package_mount = PackageMount(self.context, status_bar.lives)

        self.add_child(Background(context))
        self.add_child(package_mount)
        self.add_child(status_bar)
        self.add_child(Character(
            context,
            RelativeVector(500000, 500000),
            package_mount,
            status_bar.score
        ))

    def get_name(self: Game) -> str:
        return "Game"
