from __future__ import annotations

from typing import Set
from random import randint
from logging import getLogger
from pygame import Surface

from packy.game_object import GameObject
from packy.context import Context
from packy.update import Update
from packy.vector import RelativeVector
from packy.game_state import GameState

from .package import Package


logger = getLogger(__name__)


class PackageMount(GameObject):

    game_state: GameState

    packages: Set[Package]

    positions: int
    package_width: int
    package_height: int

    cursor: int
    velocity = 50000  # cords / sec
    spawn_rate = 7

    spawned_packages = 0

    def __init__(self: PackageMount, context: Context, game_state: GameState) -> None:
        super().__init__(context)
        self.game_state = game_state
        self.packages = set()

        self.positions = 40
        self.package_width = int(1000000 / self.positions)
        self.package_height = int(self.package_width * self.context.coordinate_system.get_ratio())

        self.cursor = 0

    def destroy_package(self: PackageMount, package: Package) -> None:
        logger.info("Destroy package.")
        self.packages.remove(package)
        self.game_state.decrease_lives()

    def generate_package(self: PackageMount) -> Package:
        logger.info("Generate package.")
        location = randint(0, self.positions - 1)
        position = RelativeVector(
            int(location * self.package_width),
            int(-1 * self.package_height)
        )

        package = Package(
            self.context,
            self.spawned_packages,
            position,
            self.package_width,
            self.velocity
        )

        self.packages.add(package)
        self.spawned_packages += 1

        self.velocity = min(200000, self.velocity + 1000)

        if self.spawned_packages % 20 == 0:
            self.spawn_rate = max(self.spawn_rate - 1, 3)

        return package

    def update(self: PackageMount, update: Update) -> None:
        # generate new packages
        self.cursor += int(self.velocity * (update.elapsed_time.microseconds / 1000000))

        if self.cursor >= self.package_height * self.spawn_rate:
            self.generate_package()

            self.cursor = 0

        # update packages
        for package in self.packages:
            package.update(update)

        destroyable_packages = [
            package for package in self.packages
            if package.position.get_y() > 1000000
        ]

        for package in destroyable_packages:
            self.destroy_package(package)

    def draw(self: PackageMount, canvas: Surface) -> None:
        for package in self.packages:
            package.draw(canvas)

    def remove_package(self: PackageMount, package: Package) -> None:
        logger.info("Remove package.")
        self.packages.remove(package)
