from __future__ import annotations

from typing import Optional
from pygame import Surface
from pygame.font import SysFont, Font, get_default_font
from pygame import Color

from packy.game_object import GameObject
from packy.context import Context
from packy.vector import RelativeVector


class Text(GameObject):
    position: RelativeVector
    text: str
    font: Font

    def __init__(
            self: Text,
            context: Context,
            position: RelativeVector,
            text: str,
            font: Optional[Font] = None
    ) -> None:
        super().__init__(context)

        self.position = position
        self.text = text
        self.font = font or SysFont(get_default_font(), 24)

    def draw(self: Text, canvas: Surface) -> None:
        position = self.context.coordinate_system.absolute(self.position)

        image = self.font.render(self.text, True, Color(0, 0, 0))
        image.get_height()
        canvas.blit(image, (
            position.get_x() - image.get_width() / 2,
            position.get_y() - image.get_height() / 2
        ))
