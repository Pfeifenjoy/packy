from __future__ import annotations


class RelativeVector:

    x: float
    y: float

    def __init__(self: RelativeVector, x: float, y: float) -> None:
        self.set_x(x)
        self.set_y(y)

    def get_x(self: RelativeVector) -> float:
        return self.x

    def get_y(self: RelativeVector) -> float:
        return self.y

    def set_x(self: RelativeVector, x: float) -> None:
        self.x = x

    def set_y(self: RelativeVector, y: float) -> None:
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
            self.get_x() * scale,
            self.get_y() * scale
        )

    def multiply(self: RelativeVector, other: RelativeVector) -> RelativeVector:
        return RelativeVector(
            self.get_x() * other.get_x(),
            self.get_y() * other.get_y()
        )

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
