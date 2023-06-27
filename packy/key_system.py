from __future__ import annotations

from typing import Set
from pygame.event import Event

from .event_handler import EventHandler


class KeySystem:

    keypress_event_handlers: Set[EventHandler]
    keyrelease_event_handlers: Set[EventHandler]

    def __init__(self: KeySystem) -> None:
        self.keypress_event_handlers = set()
        self.keyrelease_event_handlers = set()

    def handle_key_press(self: KeySystem, event: Event) -> None:
        pass  # TODO
        for handler in self.keypress_event_handlers:
            handler(event)

    def register_keypress_handler(self: KeySystem, event_handler: EventHandler) -> None:
        self.keypress_event_handlers.add(event_handler)

    def unregister_keypress_handler(self: KeySystem, event_handler: EventHandler) -> None:
        self.keypress_event_handlers.remove(event_handler)

    def handle_key_release(self: KeySystem, event: Event) -> None:
        for handler in self.keyrelease_event_handlers:
            handler(event)

    def register_keyrelease_handler(self: KeySystem, event_handler: EventHandler) -> None:
        self.keyrelease_event_handlers.add(event_handler)

    def unregister_keyrelease_handler(self: KeySystem, event_handler: EventHandler) -> None:
        self.keyrelease_event_handlers.remove(event_handler)
