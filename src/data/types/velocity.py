from data.types.vec2 import Vec2
from typing import Self


class Velocity(Vec2):
    def __add__(self, other: Self):
        return Velocity(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Self):
        return Velocity(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float):
        return Velocity(int(self.x * scalar), int(self.y * scalar))

    def __truediv__(self, scalar: float):
        if not isinstance(scalar, (int, float)) or scalar == 0:
            return NotImplemented
        return Velocity(int(self.x / scalar), int(self.y / scalar))

    def __floordiv__(self, scalar: float):
        if not isinstance(scalar, (int, float)) or scalar == 0:
            return NotImplemented
        return Velocity(self.x // int(scalar), self.y // int(scalar))

    def to_tuple(self) -> tuple:
        return (self.x, self.y)

