from __future__ import annotations

from tkinter import Tk, Event
from logging import getLogger
from typing import Set

from .event_handler import EventHandler


logger = getLogger(__name__)


class KeySystem:

    keypress_event_handlers: Set[EventHandler]

    def __init__(self: KeySystem, root: Tk) -> None:
        self.keypress_event_handlers = set()
        root.bind("<KeyPress>", self.handle_key_press)

    def handle_key_press(self: KeySystem, event: Event) -> None:
        logger.debug("Key pressed (keycode: %s, keysym: %s)", event.keycode, event.keysym)

        for handler in self.keypress_event_handlers:
            handler(event)

    def register_keypress_handler(self: KeySystem, event_handler: EventHandler) -> None:
        self.keypress_event_handlers.add(event_handler)

    def unregister_keypress_handler(self: KeySystem, event_handler: EventHandler) -> None:
        self.keypress_event_handlers.remove(event_handler)
