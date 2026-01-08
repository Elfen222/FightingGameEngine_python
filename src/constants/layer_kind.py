from enum import Enum


class LayerKind(Enum):
    """
    レイヤーの種類を定義する列挙型
    """
    BACKGROUND = 0
    FLOOR = 1
    CHARA_1P = 2
    CHARA_2P = 3
