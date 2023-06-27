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
        position = RelativeVector(20000, 25000)

        for offset in range(self.game_state.lives):
            relative_position = position.add(
                RelativeVector(30000 * offset, 0)
            )
            draw.circle(
                canvas,
                Color(200, 30, 30),
                Vector2(
                    self.context.coordinate_system.absolute_x(relative_position.get_x()),
                    self.context.coordinate_system.absolute_y(relative_position.get_y())
                ),
                self.context.coordinate_system.absolute_x(10000)
            )
