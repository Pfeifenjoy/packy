from __future__ import annotations

from tkinter import Tk, Canvas
from datetime import datetime
from time import sleep
from logging import getLogger

from .settings import Settings
from .coordinate_system import CoordinateSystem
from .context import Context
from .mouse_system import MouseSystem
from .scene_manager import SceneManager
from .key_system import KeySystem

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
        mouse_system = MouseSystem(canvas, coordinate_system)
        key_system = KeySystem(root)

        context = Context(
            coordinate_system,
            mouse_system,
            key_system,
            self.settings
        )

        scene_manager = SceneManager(context)
        root.protocol("WM_DELETE_WINDOW", self.stop)

        scene_manager.mount()

        while self.running:

            scene_manager.update()
            scene_manager.draw(canvas)

            root.update()

            self.sync()

        scene_manager.unmount()

    def sync(self: Engine) -> None:
        now = datetime.now()

        max_fps = 62

        base_delay = 1 / max_fps
        elapsed = now - self.update

        target_delay = max(0, base_delay * 1000000 - elapsed.microseconds)

        sleep(target_delay / 1000000)

        self.update = datetime.now()
