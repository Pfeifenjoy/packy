from __future__ import annotations

from tkinter import Tk, Canvas
from datetime import datetime
from time import sleep
from logging import getLogger

from packy.game_objects import Background

logger = getLogger(__name__)


class Engine:

    update: datetime
    running: bool = True

    def __init__(self: Engine):
        self.update = datetime.now()

    def stop(self: Engine) -> None:
        logger.info("Stopping engine")
        self.running = False

    def run(self: Engine) -> None:
        logger.info("Starting engine")
        root = Tk()
        # root.attributes("-fullscreen", True)

        canvas = Canvas(root, width=800, height=600)
        canvas.pack(expand=True)

        game_objects = [
            Background()
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
