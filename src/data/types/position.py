from data.types.vec2 import Vec2
from data.types.velocity import Velocity
from typing import Self


class Position(Vec2):
    def __add__(self, other: Self | Velocity):
        return Position(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Self | Velocity):
        return Position(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float):
        return Position(int(self.x * scalar), int(self.y * scalar))

    def __truediv__(self, scalar: float):
        if not isinstance(scalar, (int, float)) or scalar == 0:
            return NotImplemented
        return Position(int(self.x / scalar), int(self.y / scalar))

    def __floordiv__(self, scalar: float):
        if not isinstance(scalar, (int, float)) or scalar == 0:
            return NotImplemented
        return Position(self.x // int(scalar), self.y // int(scalar))

    def to_tuple(self) -> tuple[int, int]:
        return (int(self.x), int(self.y))

