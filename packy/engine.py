from __future__ import annotations

from tkinter import Tk, Canvas
from datetime import datetime
from time import sleep
from logging import getLogger

from .game_objects import Background
from .settings import Settings
from .coordinate_system import CoordinateSystem
from .context import Context

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
        root = Tk()

        canvas = Canvas(
            root,
            width=self.settings.width,
            height=self.settings.height
        )
        canvas.pack(expand=True)

        coordinate_system = CoordinateSystem(self.settings)

        context = Context(
            coordinate_system,
            self.settings
        )

        game_objects = [
            Background(context)
        ]
        root.protocol("WM_DELETE_WINDOW", self.stop)

        while self.running:

            for game_object in game_objects:

                game_object.update()
                game_object.draw(canvas)

            root.update()

            self.sync()

    def sync(self: Engine) -> None:
        now = datetime.now()

        max_fps = 62

        base_delay = 1 / max_fps
        elapsed = now - self.update

        target_delay = max(0, base_delay * 1000000 - elapsed.microseconds)

        sleep(target_delay / 1000000)

        self.update = datetime.now()
