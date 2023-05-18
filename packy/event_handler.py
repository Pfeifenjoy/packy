from __future__ import annotations

from tkinter import Event
from typing import Callable


EventHandler = Callable[[Event], None]
