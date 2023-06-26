from __future__ import annotations

from tkinter import Event
from pygame import Surface
from datetime import timedelta
from logging import getLogger

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
        match event.keysym:
            case "Up":
                return RelativeVector(0, -1)
            case "Down":
                return RelativeVector(0, 1)
            case "Left":
                return RelativeVector(-1, 0)
            case "Right":
                return RelativeVector(1, 0)
            case _:
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
            fill="blue"
        )

        body.draw(canvas)
