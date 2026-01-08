from dataclasses import dataclass
from data.types.position import Position
from constants.box_kind import BoxKind


@dataclass(frozen=True)
class Box:
    kind: BoxKind
    startPosition: Position
    endPosition: Position

    def get_start_position(self) -> Position:
        """
        ボックスの開始位置を取得する
        :return: Positionのインスタンス
        """
        return self.startPosition

    def get_end_position(self) -> Position:
        """
        ボックスの終了位置を取得する
        :return: Positionのインスタンス
        """
        return self.endPosition

    def get_width(self) -> int:
        """
        ボックスの幅を取得する
        :return: 幅(int)
        """
        return int(self.endPosition.x - self.startPosition.x)

    def get_height(self) -> int:
        """
        ボックスの高さを取得する
        :return: 高さ(int)
        """
        return int(self.endPosition.y - self.startPosition.y)

    def get_kind(self) -> BoxKind:
        """
        ボックスの種類を取得する
        :return: BoxKindのインスタンス
        """
        return self.kind


BoxList = list[Box]
