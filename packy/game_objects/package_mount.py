from __future__ import annotations

from typing import Set
from random import randint
from pygame import Surface
from logging import getLogger

from packy.game_object import GameObject
from packy.context import Context
from packy.update import Update
from packy.vector import RelativeVector

from .package import Package


logger = getLogger(__name__)


class PackageMount(GameObject):

    packages: Set[Package]

    positions: int
    package_width: int
    package_height: int

    cursor: int
    velocity: int

    def __init__(self: PackageMount, context: Context) -> None:
        super().__init__(context)
        self.packages = set()

        self.positions = 40
        self.package_width = int(1000000 / self.positions)
        self.package_height = int(self.package_width * self.context.coordinate_system.get_ratio())

        self.cursor = 0
        self.velocity = 50000  # cords / sec

    def destroy_package(self: PackageMount, package: Package) -> None:
        logger.info("Destroy package.")
        self.packages.remove(package)

    def generate_package(self: PackageMount) -> Package:
        logger.info("Generate package.")
        location = randint(0, self.positions)
        position = RelativeVector(
            int(location * self.package_width),
            int(-1 * self.package_height)
        )

        package = Package(
            self.context,
            position,
            self.package_width,
            self.velocity,
            self.destroy_package
        )

        self.packages.add(package)

        return package

    def update(self: PackageMount, update: Update) -> None:
        # generate new packages
        self.cursor += int(self.velocity * (update.elapsed_time.microseconds / 1000000))

        if self.cursor >= self.package_height:
            self.generate_package()

            self.cursor = 0

        # update packages
        for package in set(self.packages):
            package.update(update)

    def draw(self: PackageMount, canvas: Surface) -> None:
        for package in self.packages:
            package.draw(canvas)
