from defs.box import Box
from constants.box_kind import BoxKind


class Frame:
    """
    フレームの情報を管理するクラス
    TODO: 実装する
    """
    __box: list[Box]

    def get_box(self) -> list[Box]:
        """
        box情報を取得する
        :return: boxInfoのインスタンス
        """
        return self.__box

    def get_box_at(self, index: int) -> Box:
        """
        指定されたインデックスのbox情報を取得する
        :param index: boxのインデックス
        :return: boxInfoのインスタンス
        """
        return self.__box[index]

    def get_box_kind(self) -> list[BoxKind]:
        """
        フレームに含まれるboxの種類を取得する
        :return: boxの種類のリスト
        """
        return [box.get_kind() for box in self.__box]

    def get_box_kind_at(self, index: int) -> BoxKind:
        """
        指定されたインデックスのboxの種類を取得する
        :param index: boxのインデックス
        :return: boxの種類
        """
        return self.__box[index].get_kind()

    def get_box_count(self) -> int:
        """
        フレームに含まれるboxの数を取得する
        :return: boxの数
        """
        return len(self.__box)


FrameList = list[Frame]
