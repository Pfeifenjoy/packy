from __future__ import annotations

from packy.scene import Scene
from packy.game_object import StructuralGameObject
from packy.context import Context
from packy.game_objects import Character, Background
from packy.vector import RelativeVector


class Game(StructuralGameObject, Scene):

    def __init__(self: Game, context: Context) -> None:
        super().__init__(context)

        self.add_child(Background(context))
        self.add_child(Character(
            context,
            RelativeVector(500000, 500000)
        ))

    def get_name(self: Game) -> str:
        return "Game"
