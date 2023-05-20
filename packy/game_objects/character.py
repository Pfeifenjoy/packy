from __future__ import annotations

from tkinter import Canvas, Event

from packy.game_object import GameObject
from packy.context import Context
from packy.vector import Vector
from packy.shapes import Box

from .rectangle import Rectangle


class Character(GameObject):

    center: Vector
    dimension: Vector
    step_size = 1

    def __init__(
            self: Character,
            context: Context,
            start_position: Vector
    ) -> None:
        super().__init__(context)

        self.center = start_position
        self.dimension = self.context.coordinate_system.quad(5)
        print(self.dimension)

    def mount(self: Character) -> None:
        self.context.key_system.register_keypress_handler(self.handle_keyevent)

    def unmount(self: Character) -> None:
        self.context.key_system.unregister_keypress_handler(self.handle_keyevent)

    def handle_keyevent(self: Character, event: Event) -> None:
        step = Vector(self.step_size, self.step_size)

        match event.keysym:
            case "Up":
                step = step.multiply(Vector(0, -1))
            case "Down":
                step = step.multiply(Vector(0, 1))
            case "Left":
                step = step.multiply(Vector(-1, 0))
            case "Right":
                step = step.multiply(Vector(1, 0))

        self.center = self.center.add(step)

    def get_position(self: Character) -> Vector:
        return self.center.minus(self.dimension.scale(0.5))

    def draw(self: Character, canvas: Canvas) -> None:

        body = Rectangle(
            self.context,
            Box(self.get_position(), self.dimension),
            fill="blue"
        )

        body.draw(canvas)
