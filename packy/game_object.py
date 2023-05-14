from __future__ import annotations

from abc import ABC
from tkinter import Canvas

from .context import Context


class GameObject(ABC):
    """
    Game objects have a state and can be rendered.
    """

    context: Context

    def __init__(self: GameObject, context: Context):
        self.context = context

    def update(self: GameObject) -> None:
        """
        Updates the state of the object.
        """

    def render(self: GameObject, canvas: Canvas) -> None:
        """
        Lets the game object draw itself to the canvas.
        """
