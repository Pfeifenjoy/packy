from __future__ import annotations

from abc import abstractmethod

from .game_object import GameObject


class Scene(GameObject):

    @abstractmethod
    def get_name(self: Scene) -> str:
        raise NotImplementedError()
