from packy.vector import Vector


def test_vector_scale() -> None:
    v = Vector(1, 1)
    v = v.scale(2)
    assert v.get_x() == 2 and v.get_y() == 2
