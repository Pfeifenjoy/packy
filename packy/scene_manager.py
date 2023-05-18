from __future__ import annotations

from tkinter import Canvas
from logging import getLogger

from packy.game_object import GameObject
from packy.context import Context
from packy.scene import Scene

from .scenes import Menu, Game


logger = getLogger(__name__)


class SceneManager(GameObject):

    scene: Scene

    def __init__(self: SceneManager, context: Context):
        super().__init__(context)
        self.scene = Menu(self.context, on_play=self.start_game)

    def start_game(self: SceneManager) -> None:
        self.update_scene(Game(self.context))

    def update(self: SceneManager) -> None:
        self.scene.update()

    def draw(self: SceneManager, canvas: Canvas) -> None:
        self.scene.draw(canvas)

    def mount(self: SceneManager) -> None:
        self.scene.mount()

    def unmount(self: SceneManager) -> None:
        self.scene.unmount()

    def update_scene(self: SceneManager, scene: Scene) -> None:
        logger.info("Updating scene to: %s", scene.get_name())
        self.scene.unmount()
        self.scene = scene
        self.scene.mount()
