from __future__ import annotations

from datetime import timedelta
from logging import getLogger
from pygame import Surface, Color
from pygame.event import Event
from pygame.constants import K_LEFT, K_RIGHT, K_UP, K_DOWN

from packy.game_object import GameObject
from packy.context import Context
from packy.vector import RelativeVector
from packy.shapes import Box
from packy.update import Update

from .rectangle import Rectangle


logger = getLogger(__name__)


class Character(GameObject):

    center: RelativeVector
    dimension: RelativeVector

    speed: float = 200000  # cord / sec

    direction: RelativeVector = RelativeVector(0, 0)

    def __init__(
            self: Character,
            context: Context,
            start_position: RelativeVector
    ) -> None:
        super().__init__(context)

        self.center = start_position
        self.dimension = self.context.coordinate_system.quad(50000)

    def mount(self: Character) -> None:
        self.context.key_system.register_keypress_handler(self.handle_keypress)
        self.context.key_system.register_keyrelease_handler(self.handle_keyrelease)

    def unmount(self: Character) -> None:
        self.context.key_system.unregister_keypress_handler(self.handle_keypress)
        self.context.key_system.unregister_keyrelease_handler(self.handle_keyrelease)

    def get_key_direction(self: Character, event: Event) -> RelativeVector:
        if event.key == K_UP:
            return RelativeVector(0, -1)
        if event.key == K_DOWN:
            return RelativeVector(0, 1)
        if event.key == K_LEFT:
            return RelativeVector(-1, 0)
        if event.key == K_RIGHT:
            return RelativeVector(1, 0)

        return RelativeVector(0, 0)

    def handle_keypress(self: Character, event: Event) -> None:
        self.direction = self.direction.add(self.get_key_direction(event))

    def handle_keyrelease(self: Character, event: Event) -> None:
        self.direction = self.direction.minus(self.get_key_direction(event))

    def get_motion(self: Character, elapsed_time: timedelta) -> RelativeVector:
        return self.direction.resize(int(self.speed * (elapsed_time.microseconds / 1000000)))

    def get_position(self: Character) -> RelativeVector:
        return self.center.minus(self.dimension.scale(0.5))

    def update(self: Character, update: Update) -> None:
        self.center = self.center.add(
            self.get_motion(update.elapsed_time)
        )

    def draw(self: Character, canvas: Surface) -> None:

        body = Rectangle(
            self.context,
            Box(self.get_position(), self.dimension),
            fill=Color(0, 0, 255)
        )

        body.draw(canvas)
