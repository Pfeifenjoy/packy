from __future__ import annotations

from typing import Set
from logging import getLogger
from pygame.event import Event
from pygame.constants import KEYDOWN, KEYUP

from .event_handler import EventHandler


logger = getLogger(__name__)


class KeySystem:

    keypress_event_handlers: Set[EventHandler]
    keyrelease_event_handlers: Set[EventHandler]

    def __init__(self: KeySystem) -> None:
        self.keypress_event_handlers = set()
        self.keyrelease_event_handlers = set()

    def handle_key_press(self: KeySystem, event: Event) -> None:
        logger.debug("Pressed key %s.", event.key)
        for handler in self.keypress_event_handlers:
            handler(event)

    def register_keypress_handler(self: KeySystem, event_handler: EventHandler) -> None:
        self.keypress_event_handlers.add(event_handler)

    def unregister_keypress_handler(self: KeySystem, event_handler: EventHandler) -> None:
        self.keypress_event_handlers.remove(event_handler)

    def handle_key_release(self: KeySystem, event: Event) -> None:
        logger.debug("Released key %s.", event.key)
        for handler in self.keyrelease_event_handlers:
            handler(event)

    def register_keyrelease_handler(self: KeySystem, event_handler: EventHandler) -> None:
        self.keyrelease_event_handlers.add(event_handler)

    def unregister_keyrelease_handler(self: KeySystem, event_handler: EventHandler) -> None:
        self.keyrelease_event_handlers.remove(event_handler)

    def process(self: KeySystem, event: Event) -> None:
        if event.type == KEYDOWN:
            self.handle_key_press(event)
        elif event.type == KEYUP:
            self.handle_key_release(event)
