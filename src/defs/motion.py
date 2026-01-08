from data.types.velocity import Velocity
from defs.layer_change_trigger import LayerChangeTrigger
from defs.velocity_change_trigger import VelocityChangeTrigger
from defs.controllable_change_trigger import ControllableChangeTrigger
from bisect import bisect_right


class Motion:
    def __init__(self, frame_length: int,
                 layer_change_trigger: list[LayerChangeTrigger],
                 controlable_change_trigger: list[ControllableChangeTrigger],
                 velocity_change_trigger: list[VelocityChangeTrigger],
                 holdable: bool, is_animation_loop: bool):
        # フレーム数
        self.__frame_length: int = frame_length

        # レイヤー、速度、判定情報はトリガー方式で管理する。
        # 指定したフレームに到達した場合、各々の情報に切り替わる方針。
        # 現在フレームがどのトリガーに該当するかを高速に取得するために、キャッシュを用意する。
        # これらのトリガーには必ずフレーム0の情報が含まれている必要がある。
        # TODO: トリガー関数が増えすぎた場合、共通化を検討する。

        # レイヤー情報
        self.__layer_change_trigger: list[LayerChangeTrigger] = layer_change_trigger
        index_list: list[int] = list(map(lambda x: x.get_frame_index(), self.__layer_change_trigger))
        if 0 not in index_list:
            raise ValueError("LayerChangeTrigger must include frame index 0")

        self.__layer_index_cache: list[int] = self.__make_index_cache(index_list)

        # コントロール可能かどうかの情報
        self.__controlable_change_trigger: list[ControllableChangeTrigger] = controlable_change_trigger
        index_list: list[int] = list(map(lambda x: x.get_frame_index(), self.__controlable_change_trigger))
        if 0 not in index_list:
            raise ValueError("ControllableChangeTrigger must include frame index 0")

        self.__controlable_index_cache: list[int] = self.__make_index_cache(index_list)

        # 速度情報
        self.__velocity_change_trigger: list[VelocityChangeTrigger] = velocity_change_trigger
        index_list: list[int] = list(map(lambda x: x.get_frame_index(), self.__velocity_change_trigger))
        if 0 not in index_list:
            raise ValueError("VelocityChangeTrigger must include frame index 0")
        self.__velocity_index_cache: list[int] = self.__make_index_cache(index_list)

        # ホールド可能かどうか
        self.__holdable: bool = holdable

        # アニメーションがループするかどうか
        # TODO:StartとEndを指定してループした方が柔軟性はある
        self.__is_animation_loop: bool = is_animation_loop

    def get_frame_length(self) -> int:
        """
        フレーム数を取得
        Returns:
            int: フレーム数
        """
        return self.__frame_length

    def get_now_layer_index(self, index: int) -> int:
        """
        指定されたインデックスの現在のレイヤーインデックスを取得
        Args:
            index (int): フレームインデックス
        Returns:
            int: レイヤーインデックス
        """
        return self.__layer_change_trigger[self.__layer_index_cache[index]].get_layer_index()

    def is_controlable(self, index: int) -> bool:
        """
        指定されたインデックスのコントロール可能情報を取得
        Args:
            index (int): フレームインデックス
        Returns:
            bool: コントロール可能ならTrue、そうでなければFalse
        """
        return self.__controlable_change_trigger[self.__controlable_index_cache[index]].is_controlable()

    def is_holdable(self) -> bool:
        """
        モーションがホールド可能かどうかを取得
        Returns:
            bool: ホールド可能ならTrue、そうでなければFalse
        """
        return self.__holdable

    def is_loop(self) -> bool:
        """
        モーションがループするかどうかを取得
        Returns:
            bool: ループするならTrue、そうでなければFalse
        """
        return self.__is_animation_loop

    def get_velocity(self, index: int) -> Velocity:
        """
        指定されたインデックスの速度情報を取得
        Args:
            index (int): 速度情報のインデックス
        Returns:
            Velocity: 速度情報
        """
        return self.__velocity_change_trigger[self.__velocity_index_cache[index]].get_velocity()

    def __make_index_cache(self, trigger_frame_indices: list[int]) -> list[int]:
        """
        各フレームで参照するトリガーインデックスのキャッシュを作成
        計算量を削減するために使用
        """
        index_cache: list[int] = []
        for frame_idx in range(self.__frame_length):
            idx = bisect_right(sorted(trigger_frame_indices), frame_idx) - 1
            index_cache.append(idx)

        return index_cache

MotionKind = str
