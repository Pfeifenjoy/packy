from __future__ import annotations

from typing import Callable
from pygame.event import Event


EventHandler = Callable[[Event], None]
