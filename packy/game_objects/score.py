from __future__ import annotations

from pygame import Surface

from packy.game_object import GameObject
from packy.vector import RelativeVector

from .text import Text


class Score(GameObject):

    count = 0

    def increment(self: Score) -> None:
        self.count += 1

    def draw(self: Score, canvas: Surface) -> None:
        position = RelativeVector(930000, 25000)
        raw_text = "Score: " + str(self.count)
        text = Text(self.context, position, raw_text)
        text.draw(canvas)
