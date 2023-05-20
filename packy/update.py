from __future__ import annotations

from datetime import timedelta
from dataclasses import dataclass


@dataclass
class Update:

    elapsed_time: timedelta
