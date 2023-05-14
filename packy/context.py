from __future__ import annotations

from dataclasses import dataclass

from .coordinate_system import CoordinateSystem
from .settings import Settings


@dataclass
class Context:
    coordinate_system: CoordinateSystem
    settings: Settings
