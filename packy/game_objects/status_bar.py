from __future__ import annotations

from pygame import Surface, Color

from packy.game_object import GameObject
from packy.context import Context
from packy.shapes import Box
from packy.vector import RelativeVector
from packy.game_state import GameState

from .score import Score
from .lives import Lives
from .rectangle import Rectangle


class StatusBar(GameObject):
    background: Rectangle
    score: Score

    def __init__(
        self: StatusBar,
        context: Context,
        game_state: GameState
    ) -> None:
        super().__init__(context)
        self.score = Score(context, game_state)
        self.lives = Lives(context, game_state)
        self.background = Rectangle(
            context,
            Box(RelativeVector(0, 0), RelativeVector(1000000, 50000)),
            Color(230, 230, 230, 150),
            Color(230, 230, 230, 150)
        )

    def draw(self: StatusBar, canvas: Surface) -> None:
        self.background.draw(canvas)
        self.score.draw(canvas)
        self.lives.draw(canvas)
