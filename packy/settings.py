from __future__ import annotations

from pydantic import BaseModel


class Settings(BaseModel):

    width: int = 800
    height: int = 600

    fps: int = 62
