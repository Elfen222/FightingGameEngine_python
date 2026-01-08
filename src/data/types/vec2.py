class Vec2:
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y

    def __add__(self, other):
        if not isinstance(other, Vec2):
            return NotImplemented
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, Vec2):
            return NotImplemented
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float):
        return Vec2(int(self.x * scalar), int(self.y * scalar))

    def __truediv__(self, scalar: float):
        if not isinstance(scalar, (int, float)) or scalar == 0:
            return NotImplemented
        return Vec2(int(self.x / scalar), int(self.y / scalar))

    def __floordiv__(self, scalar: float):
        if not isinstance(scalar, (int, float)) or scalar == 0:
            return NotImplemented
        return Vec2(self.x // int(scalar), self.y // int(scalar))

    def to_tuple(self) -> tuple:
        return (self.x, self.y)

