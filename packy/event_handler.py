from __future__ import annotations

from pygame.event import Event
from typing import Callable


EventHandler = Callable[[Event], None]
