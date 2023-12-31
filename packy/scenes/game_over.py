from __future__ import annotations

from typing import Callable
from pygame.font import SysFont, get_default_font

from packy.scene import Scene
from packy.game_object import StructuralGameObject
from packy.context import Context
from packy.game_objects import Text, Button
from packy.vector import RelativeVector
from packy.shapes import Box
from packy.game_state import GameState


class GameOver(StructuralGameObject, Scene):

    def __init__(
        self: GameOver,
        context: Context,
        game_state: GameState,
        on_restart: Callable[[], None]
    ) -> None:
        super().__init__(context)

        heading = Text(
            context,
            RelativeVector(500000, 200000),
            "Game Over",
            SysFont(get_default_font(), 50)
        )

        self.add_child(heading)

        score = Text(
            context,
            RelativeVector(500000, 270000),
            "Your Score: " + str(game_state.score),
            SysFont(get_default_font(), 35)
        )

        self.add_child(score)

        restart_button = Button(
            context,
            Box(
                RelativeVector(int(1000000/3), 350000),
                RelativeVector(int(1000000/3), 100000)
            ),
            "Restart",
            lambda point: on_restart()
        )

        self.add_child(restart_button)

    def get_name(self: GameOver) -> str:
        return "GameOver"
