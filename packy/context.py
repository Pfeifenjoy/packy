from __future__ import annotations

from dataclasses import dataclass

from .coordinate_system import CoordinateSystem
from .mouse_system import MouseSystem
from .settings import Settings


@dataclass
class Context:
    coordinate_system: CoordinateSystem
    mouse_system: MouseSystem
    settings: Settings
