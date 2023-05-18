from __future__ import annotations


class Vector:

    _x: int

    _y: int

    def __init__(self: Vector, x: int, y: int) -> None:
        self.set_x(x)
        self.set_y(y)

    def get_x(self: Vector) -> int:
        return self._x

    def get_y(self: Vector) -> int:
        return self._y

    def set_x(self: Vector, x: int) -> None:
        self._x = x

    def set_y(self: Vector, y: int) -> None:
        self._y = y

    def add(self: Vector, other: Vector) -> Vector:
        return Vector(
            self.get_x() + other.get_x(),
            self.get_y() + other.get_y()
        )

    def minus(self: Vector, other: Vector) -> Vector:
        return Vector(
            self.get_x() - other.get_x(),
            self.get_y() - other.get_y()
        )

    def scale(self: Vector, scale: float) -> Vector:
        return Vector(
            int(self.get_x() * scale),
            int(self.get_y() * scale)
        )

    def __str__(self: Vector) -> str:
        return f"Vector({ self.get_x() }, { self.get_y() })"
