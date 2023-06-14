from __future__ import annotations

from abc import ABC, abstractmethod

from .vector import RelativeVector
from .shape_types import ShapeTypes


class Shape(ABC):
    shape_type: ShapeTypes

    def __init__(self: Shape, shape_type: ShapeTypes) -> None:
        self.shape_type = shape_type

    @abstractmethod
    def inside(self: Shape, point: RelativeVector) -> bool:
        raise NotImplementedError()
