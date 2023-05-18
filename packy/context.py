from __future__ import annotations

from dataclasses import dataclass

from .coordinate_system import CoordinateSystem
from .mouse_system import MouseSystem
from .settings import Settings
from .key_system import KeySystem


@dataclass
class Context:
    coordinate_system: CoordinateSystem
    mouse_system: MouseSystem
    key_system: KeySystem
    settings: Settings
