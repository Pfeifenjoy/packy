from __future__ import annotations

from tkinter.font import Font
from typing import Optional, Callable, List

from packy.game_object import StructuralGameObject, GameObject
from packy.context import Context
from packy.shapes import Box
from packy.shape import Shape
from packy.mouse_system import MotionHandler, ClickHandler
from packy.vector import Vector

from .rectangle import Rectangle
from .text import Text


class ButtonClickHandler(ClickHandler):
    on_click: Callable[[Vector], None]
    shape: Shape

    def __init__(
            self: ButtonClickHandler,
            shape: Shape,
            on_click: Callable[[Vector], None]
    ) -> None:
        self.on_click = on_click
        self.shape = shape

    def handle_click(self: ButtonClickHandler, point: Vector) -> None:
        self.on_click(point)

    def get_shape(self: ButtonClickHandler) -> Shape:
        return self.shape


class Button(StructuralGameObject, MotionHandler):

    box: Box
    rectangle: Rectangle
    click_handler: ButtonClickHandler
    children: List[GameObject]

    def __init__(
            self: Button,
            context: Context,
            box: Box,
            text: str,
            on_click: Callable[[Vector], None],
            font: Optional[Font] = None
    ) -> None:
        super().__init__(context)

        self.box = box

        self.rectangle = Rectangle(
            self.context,
            self.box,
            fill="#B4ADD9"
        )
        self.add_child(self.rectangle)
        self.add_child(
            Text(
                context,
                self.box.center(),
                text,
                font or Font(size=context.coordinate_system.translate_y(3))
            )
        )

        self.click_handler = ButtonClickHandler(
            self.get_shape(),
            on_click
        )

    def get_children(self: Button) -> List[GameObject]:
        return self.children

    def mount(self: Button) -> None:
        super().mount()

        self.context.mouse_system.add_motion_handler(self)
        self.context.mouse_system.add_click_handler(self.click_handler)

    def unmount(self: Button) -> None:
        super().unmount()

        self.context.mouse_system.remove_motion_handler(self)
        self.context.mouse_system.remove_click_handler(self.click_handler)

    def get_shape(self: Button) -> Shape:
        return self.box

    def handle_motion(self: Button, start: Vector, end: Vector) -> None:
        if self.box.inside(end):
            self.rectangle.fill = "green"
        else:
            self.rectangle.fill = "#B4ADD9"
