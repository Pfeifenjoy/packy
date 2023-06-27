from __future__ import annotations

from pygame import Surface

from packy.game_object import GameObject
from packy.vector import RelativeVector
from packy.context import Context
from packy.game_state import GameState

from .text import Text


class Score(GameObject):

    game_state: GameState

    def __init__(self: Score, context: Context, game_state: GameState) -> None:
        super().__init__(context)

        self.game_state = game_state

    def draw(self: Score, canvas: Surface) -> None:
        position = RelativeVector(930000, 25000)
        raw_text = "Score: " + str(self.game_state.score)
        text = Text(self.context, position, raw_text)
        text.draw(canvas)
