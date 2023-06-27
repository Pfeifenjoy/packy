from __future__ import annotations

from typing import Callable

from packy.scene import Scene
from packy.game_object import StructuralGameObject
from packy.context import Context
from packy.game_objects import Character, Background, PackageMount, StatusBar
from packy.vector import RelativeVector
from packy.game_state import GameState


class Game(StructuralGameObject, Scene):

    def __init__(
        self: Game,
        context: Context,
        on_game_over: Callable[[GameState], None]
    ) -> None:
        super().__init__(context)

        game_state = GameState(on_game_over)
        status_bar = StatusBar(context, game_state)
        package_mount = PackageMount(self.context, game_state)

        self.add_child(Background(context))
        self.add_child(package_mount)
        self.add_child(status_bar)
        self.add_child(Character(
            context,
            RelativeVector(500000, 500000),
            game_state,
            package_mount
        ))

    def get_name(self: Game) -> str:
        return "Game"
