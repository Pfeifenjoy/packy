from __future__ import annotations

from typing import Callable
from pygame import Surface, Color, Vector2, draw

from packy.game_object import GameObject
from packy.vector import RelativeVector
from packy.context import Context


class Lives(GameObject):
    lives = 3
    on_no_lives: Callable[[], None]

    def __init__(self: Lives, context: Context, on_no_lives: Callable[[], None]) -> None:
        super().__init__(context)
        self.on_no_lives = on_no_lives

    def decrease(self: Lives) -> None:
        self.lives = max(0, self.lives - 1)

        if self.lives == 0:
            self.on_no_lives()

    def draw(self: Lives, canvas: Surface) -> None:
        position = RelativeVector(20000, 25000)

        for offset in range(self.lives):
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
