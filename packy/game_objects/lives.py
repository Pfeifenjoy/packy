from __future__ import annotations

from pygame import Surface, Color, Vector2, draw

from packy.game_object import GameObject
from packy.vector import RelativeVector
from packy.context import Context
from packy.game_state import GameState


class Lives(GameObject):
    game_state: GameState

    def __init__(self: Lives, context: Context, game_state: GameState) -> None:
        super().__init__(context)
        self.game_state = game_state

    def draw(self: Lives, canvas: Surface) -> None:
        # TODO draw lives on the left side of the top bar.
        pass
