from __future__ import annotations

from tkinter import Tk, Event
from typing import Set

from .event_handler import EventHandler


class KeySystem:

    keypress_event_handlers: Set[EventHandler]
    keyrelease_event_handlers: Set[EventHandler]

    def __init__(self: KeySystem, root: Tk) -> None:
        self.keypress_event_handlers = set()
        self.keyrelease_event_handlers = set()
        root.bind("<KeyPress>", self.handle_key_press)
        root.bind("<KeyRelease>", self.handle_key_release)

    def handle_key_press(self: KeySystem, event: Event) -> None:
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
