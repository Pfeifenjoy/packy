from __future__ import annotations

from typing import Set
from tkinter import Canvas, Event
from abc import ABC, abstractmethod

from .vector import Vector
from .shape import Shape
from .coordinate_system import CoordinateSystem


class Handler(ABC):

    @abstractmethod
    def get_shape(self: Handler) -> Shape:
        raise NotImplementedError()

    def cares(self: Handler, point: Vector) -> bool:
        return self.get_shape().inside(point)


class MotionHandler(Handler):

    @abstractmethod
    def handle_motion(self: MotionHandler, start: Vector, end: Vector) -> None:
        raise NotImplementedError()


class ClickHandler(Handler):

    @abstractmethod
    def handle_click(self: ClickHandler, point: Vector) -> None:
        raise NotImplementedError()


class MouseSystem:

    motion_handlers: Set[MotionHandler]
    click_handlers: Set[ClickHandler]
    cursor_position: Vector
    coordinate_system: CoordinateSystem

    def __init__(self: MouseSystem, canvas: Canvas, coordinate_system: CoordinateSystem) -> None:
        self.motion_handlers = set()
        self.click_handlers = set()
        self.cursor_position = Vector(0, 0)
        self.coordinate_system = coordinate_system

        canvas.bind("<Motion>", self.motion)
        canvas.bind("<Button-1>", self.click)

    def motion(self: MouseSystem, event: Event) -> None:
        new_cursor_position = self.coordinate_system.relative(Vector(event.x, event.y))

        for motion_handler in self.motion_handlers:
            if motion_handler.cares(self.cursor_position) \
                    or motion_handler.cares(Vector(event.x, event.y)):
                motion_handler.handle_motion(self.cursor_position, new_cursor_position)

        self.cursor_position = new_cursor_position

    def click(self: MouseSystem, event: Event) -> None:
        point = self.coordinate_system.relative(Vector(event.x, event.y))

        handlers = [handler for handler in self.click_handlers if handler.cares(point)]

        for handler in handlers:
            handler.handle_click(point)

    def add_motion_handler(self: MouseSystem, motion_handler: MotionHandler) -> None:
        self.motion_handlers.add(motion_handler)

    def remove_motion_handler(self: MouseSystem, motion_handler: MotionHandler) -> None:
        self.motion_handlers.remove(motion_handler)

    def add_click_handler(self: MouseSystem, click_handler: ClickHandler) -> None:
        self.click_handlers.add(click_handler)

    def remove_click_handler(self: MouseSystem, click_handler: ClickHandler) -> None:
        self.click_handlers.remove(click_handler)
