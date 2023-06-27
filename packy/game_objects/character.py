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
from .package_mount import PackageMount
from .score import Score


logger = getLogger(__name__)


class Character(GameObject):

    box: Box

    speed: float = 200000  # cord / sec

    direction: RelativeVector = RelativeVector(0, 0)

    package_mount: PackageMount
    score: Score

    def __init__(
            self: Character,
            context: Context,
            start_position: RelativeVector,
            package_mount: PackageMount,
            score: Score
    ) -> None:
        super().__init__(context)

        self.box = Box(
            start_position,
            self.context.coordinate_system.quad(50000)
        )
        self.package_mount = package_mount
        self.score = score

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
        return self.box.center().minus(self.box.get_dimensions().scale(0.5))

    def update(self: Character, update: Update) -> None:
        self.box.move(self.get_motion(update.elapsed_time))

        collided_packages = [
            package for package in self.package_mount.packages
            if self.context.collision_system.collides(self.box, package.get_box())
        ]

        for package in collided_packages:
            self.package_mount.remove_package(package)
            self.score.increment()

    def draw(self: Character, canvas: Surface) -> None:

        body = Rectangle(
            self.context,
            Box(self.get_position(), self.box.get_dimensions()),
            fill=Color(0, 0, 255)
        )

        body.draw(canvas)
