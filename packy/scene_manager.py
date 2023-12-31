from __future__ import annotations

from logging import getLogger
from pygame import Surface

from .game_object import GameObject
from .context import Context
from .scene import Scene
from .scenes import Menu, Game, GameOver
from .update import Update
from .game_state import GameState


logger = getLogger(__name__)


class SceneManager(GameObject):

    scene: Scene

    def __init__(self: SceneManager, context: Context):
        super().__init__(context)
        self.scene = Menu(self.context, on_play=self.start_game)

    def start_game(self: SceneManager) -> None:
        self.update_scene(Game(self.context, self.game_over))

    def game_over(self: SceneManager, game_state: GameState) -> None:
        self.update_scene(GameOver(self.context, game_state, self.start_game))

    def update(self: SceneManager, update: Update) -> None:
        self.scene.update(update)

    def draw(self: SceneManager, canvas: Surface) -> None:
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
