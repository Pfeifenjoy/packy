from __future__ import annotations

from math import sqrt



class RelativeVector:

    x: int # between 0 and 1000000
    y: int # between 0 and 1000000

    def __init__(self: RelativeVector, x: int, y: int) -> None:
        self.set_x(x)
        self.set_y(y)

    def get_x(self: RelativeVector) -> int:
        return self.x

    def get_y(self: RelativeVector) -> int:
        return self.y

    def set_x(self: RelativeVector, x: int) -> None:
        self.x = x

    def set_y(self: RelativeVector, y: int) -> None:
        self.y = y

    def add(self: RelativeVector, other: RelativeVector) -> RelativeVector:
        return RelativeVector(
            self.get_x() + other.get_x(),
            self.get_y() + other.get_y()
        )

    def minus(self: RelativeVector, other: RelativeVector) -> RelativeVector:
        return RelativeVector(
            self.get_x() - other.get_x(),
            self.get_y() - other.get_y()
        )

    def scale(self: RelativeVector, scale: float) -> RelativeVector:
        return RelativeVector(
            int(self.get_x() * scale),
            int(self.get_y() * scale)
        )

    def multiply(self: RelativeVector, other: RelativeVector) -> RelativeVector:
        return RelativeVector(
            self.get_x() * other.get_x(),
            self.get_y() * other.get_y()
        )

    def resize(self: RelativeVector, new_length: int) -> RelativeVector:
        if self.length() == 0:
            return RelativeVector(0, 0)

        length = self.length()

        return RelativeVector(
            int((self.get_x() / length) * new_length),
            int((self.get_y() / length) * new_length)
        )

    def length(self: RelativeVector) -> float:
        return sqrt(self.get_x()**2 + self.get_y()**2)

    def __str__(self: RelativeVector) -> str:
        return f"Vector({ self.get_x() }, { self.get_y() })"


class AbsoluteVector:

    x: int
    y: int

    def __init__(self: AbsoluteVector, x: int, y: int) -> None:
        self.set_x(x)
        self.set_y(y)

    def get_x(self: AbsoluteVector) -> int:
        return self.x

    def get_y(self: AbsoluteVector) -> int:
        return self.y

    def set_x(self: AbsoluteVector, x: int) -> None:
        self.x = x

    def set_y(self: AbsoluteVector, y: int) -> None:
        self.y = y

    def add(self: AbsoluteVector, other: AbsoluteVector) -> AbsoluteVector:
        return AbsoluteVector(
            self.get_x() + other.get_x(),
            self.get_y() + other.get_y()
        )

    def minus(self: AbsoluteVector, other: AbsoluteVector) -> AbsoluteVector:
        return AbsoluteVector(
            self.get_x() - other.get_x(),
            self.get_y() - other.get_y()
        )

    def scale(self: AbsoluteVector, scale: int) -> AbsoluteVector:
        return AbsoluteVector(
            self.get_x() * scale,
            self.get_y() * scale
        )

    def multiply(self: AbsoluteVector, other: AbsoluteVector) -> AbsoluteVector:
        return AbsoluteVector(
            self.get_x() * other.get_x(),
            self.get_y() * other.get_y()
        )

    def __str__(self: AbsoluteVector) -> str:
        return f"Vector({ self.get_x() }, { self.get_y() })"
