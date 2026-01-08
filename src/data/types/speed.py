from dataclasses import dataclass


@dataclass
class Speed:
    """
    速度(または加速度)
    Args:
        left (float): 左方向の速度
        right (float): 右方向の速度
        down (float): 下方向の速度
        up (float): 上方向の速度
    """
    left: float
    right: float
    down: float
    up: float

    def __add__(self, other):
        if not isinstance(other, Speed):
            return NotImplemented
        return Speed(
            up=self.up + other.up,
            down=self.down + other.down,
            left=self.left + other.left,
            right=self.right + other.right
        )

    def __sub__(self, other):
        if not isinstance(other, Speed):
            return NotImplemented
        return Speed(
            up=self.up - other.up,
            down=self.down - other.down,
            left=self.left - other.left,
            right=self.right - other.right
        )

    def __mul__(self, scalar: float):
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        return Speed(
            up=int(self.up * scalar),
            down=int(self.down * scalar),
            left=int(self.left * scalar),
            right=int(self.right * scalar)
        )

    def __truediv__(self, scalar: float):
        if not isinstance(scalar, (int, float)) or scalar == 0:
            return NotImplemented
        return Speed(
            up=int(self.up / scalar),
            down=int(self.down / scalar),
            left=int(self.left / scalar),
            right=int(self.right / scalar)
        )

    def __floordiv__(self, scalar: float):
        if not isinstance(scalar, (int, float)) or scalar == 0:
            return NotImplemented
        return Speed(
            up=self.up // int(scalar),
            down=self.down // int(scalar),
            left=self.left // int(scalar),
            right=self.right // int(scalar)
        )

    def to_tuple(self) -> tuple:
        return (self.left, self.right, self.down, self.up)
