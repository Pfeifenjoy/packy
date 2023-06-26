from __future__ import annotations

from abc import ABC

from pygame import Surface


class Drawable(ABC):

    def draw(self: Drawable, canvas: Surface) -> None:
        """
        Method to be overriden for drawings.
        """
