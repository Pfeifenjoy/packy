from __future__ import annotations

from abc import ABC, abstractmethod

from .vector import RelativeVector


class Shape(ABC):

    @abstractmethod
    def inside(self: Shape, point: RelativeVector) -> bool:
        raise NotImplementedError()
