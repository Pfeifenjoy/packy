from __future__ import annotations

from typing import Callable
from logging import getLogger


logger = getLogger(__name__)


class GameState:

    score = 0
    lives = 3

    on_game_over: Callable[[GameState], None]

    def __init__(self: GameState, on_game_over: Callable[[GameState], None]) -> None:
        self.on_game_over = on_game_over

    def increase_score(self: GameState) -> None:
        self.score += 1
        logger.info("Score increased to %s.", self.score)

    def decrease_lives(self: GameState) -> None:
        self.lives = max(0, self.lives - 1)
        logger.info("Lost live, remaining %s.", self.lives)

        if self.lives == 0:
            self.on_game_over(self)
