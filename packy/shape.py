from __future__ import annotations

from abc import ABC, abstractmethod

from .vector import Vector


class Shape(ABC):

    @abstractmethod
    def inside(self: Shape, point: Vector) -> bool:
        raise NotImplementedError()
