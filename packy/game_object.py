from __future__ import annotations

from abc import ABC
from tkinter import Canvas
from typing import List

from .context import Context


class GameObject(ABC):
    """
    Game objects have a state and can be rendered.
    """

    context: Context

    def __init__(self: GameObject, context: Context) -> None:
        self.context = context

    def update(self: GameObject) -> None:
        """
        Updates the state of the object.
        """

    def draw(self: GameObject, canvas: Canvas) -> None:
        """
        Lets the game object draw itself to the canvas.
        """

    def mount(self: GameObject) -> None:
        """
        This method is called before the game object becomes active.
        """

    def unmount(self: GameObject) -> None:
        """
        This methid is called after the game object becomes inactive.
        """


class StructuralGameObject(GameObject, ABC):

    children: List[GameObject]

    def __init__(self: StructuralGameObject, context: Context) -> None:
        super().__init__(context)

        self.children = []

    def update(self: StructuralGameObject) -> None:
        for child in self.children:
            child.update()

    def draw(self: StructuralGameObject, canvas: Canvas) -> None:
        for child in self.children:
            child.draw(canvas)

    def mount(self: StructuralGameObject) -> None:
        for child in self.children:
            child.mount()

    def unmount(self: StructuralGameObject) -> None:
        for child in self.children:
            child.unmount()

    def add_child(self: StructuralGameObject, child: GameObject) -> None:
        self.children.append(child)
