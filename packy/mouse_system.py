from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Set
from logging import getLogger
from pygame.event import Event
from pygame.constants import MOUSEBUTTONDOWN, MOUSEMOTION

from .vector import RelativeVector, AbsoluteVector
from .shape import Shape
from .coordinate_system import CoordinateSystem


logger = getLogger(__name__)


class Handler(ABC):

    @abstractmethod
    def get_shape(self: Handler) -> Shape:
        raise NotImplementedError()

    def cares(self: Handler, point: RelativeVector) -> bool:
        return self.get_shape().inside(point)


class MotionHandler(Handler):

    @abstractmethod
    def handle_motion(self: MotionHandler, start: RelativeVector, end: RelativeVector) -> None:
        raise NotImplementedError()


class ClickHandler(Handler):

    @abstractmethod
    def handle_click(self: ClickHandler, point: RelativeVector) -> None:
        raise NotImplementedError()


class MouseSystem:

    motion_handlers: Set[MotionHandler]
    click_handlers: Set[ClickHandler]
    cursor_position: RelativeVector
    coordinate_system: CoordinateSystem

    def __init__(self: MouseSystem, coordinate_system: CoordinateSystem) -> None:
        self.motion_handlers = set()
        self.click_handlers = set()
        self.cursor_position = RelativeVector(0, 0)
        self.coordinate_system = coordinate_system

    def motion(self: MouseSystem, event: Event) -> None:
        new_cursor_position = self.coordinate_system.relative(
            AbsoluteVector(event.pos[0], event.pos[1])
        )

        for motion_handler in self.motion_handlers:
            if motion_handler.cares(self.cursor_position) \
                    or motion_handler.cares(new_cursor_position):
                motion_handler.handle_motion(self.cursor_position, new_cursor_position)

        self.cursor_position = new_cursor_position

    def click(self: MouseSystem, event: Event) -> None:
        point = self.coordinate_system.relative(
            AbsoluteVector(event.pos[0], event.pos[1])
        )

        logger.debug(
            "Click event at absolute (%s, %s) relative (%s, %s)",
            event.pos[0], event.pos[1],
            point.get_x(), point.get_y()
        )

        handlers = [
            handler for handler in self.click_handlers if handler.cares(point)
        ]

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

    def process(self: MouseSystem, event: Event) -> None:
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                self.click(event)
        elif event.type == MOUSEMOTION:
            self.motion(event)
