from __future__ import annotations

from datetime import datetime
from time import sleep
from logging import getLogger
import pygame

from .settings import Settings
from .coordinate_system import CoordinateSystem
from .context import Context
from .mouse_system import MouseSystem
from .scene_manager import SceneManager
from .key_system import KeySystem
from .update import Update

logger = getLogger(__name__)


class Engine:

    update: datetime
    running: bool = True
    settings: Settings

    def __init__(self: Engine, settings: Settings = Settings()):
        self.update = datetime.now()
        self.settings = settings

    def stop(self: Engine) -> None:
        logger.info("Stopping engine")
        self.running = False

    def run(self: Engine) -> None:
        logger.info("Starting engine")
        pygame.init()
        screen = pygame.display.set_mode([self.settings.width, self.settings.height])
        clock = pygame.time.Clock()

        coordinate_system = CoordinateSystem(self.settings)
        mouse_system = MouseSystem(coordinate_system)
        key_system = KeySystem()

        context = Context(
            coordinate_system,
            mouse_system,
            key_system,
            self.settings
        )

        scene_manager = SceneManager(context)
        scene_manager.mount()

        last_update = datetime.now()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop()
                    continue
                mouse_system.process(event)

            now = datetime.now()
            update = Update(
                now - last_update
            )
            last_update = now

            scene_manager.update(update)
            scene_manager.draw(screen)

            pygame.display.flip()
            clock.tick(self.settings.fps)

        scene_manager.unmount()

    def sync(self: Engine) -> None:
        now = datetime.now()

        max_fps = 62

        base_delay = 1 / max_fps
        elapsed = now - self.update

        target_delay = max(0, base_delay * 1000000 - elapsed.microseconds)

        sleep(target_delay / 1000000)

        self.update = datetime.now()
