from defs.character import Character
from defs.motion import Motion, MotionKind
from constants.character_list import CHARACTER_LIST
from data.types.position import Position
from constants.side import Side

from icecream import ic


class Entity:
    def __init__(self, character: str, is_player: bool = False, side: Side = Side.LEFT):
        self.__position:  Position = Position(0, 0)
        self.__character: Character = CHARACTER_LIST[character]
        self.__motion_kind:     MotionKind = "STAND"
        self.__state_frame_idx: int = 0
        self.__accelaration:    float = 0
        self.__is_player:       bool = is_player
        self.__side:            Side = side

    def set_position(self, position: Position):
        self.__position = position

    def set_acceleration(self, acceleration: float):
        """
        キャラクターの加速度を設定
        Args:
            acceleration (int): 加速度
        """
        self.__accelaration = acceleration

    def set_side(self, side: Side):
        """
        キャラクターの向きを設定
        Args:
            side (Side): 向き
        """
        self.__side = side

    def set_state(self, motion_kind: MotionKind) -> None:
        """
        キャラクターの状態を設定
        Args:
            state (str): 状態
        """
        if self.__character.has_motion(motion_kind) is False:
            raise ValueError(f"Character don't has motion: {motion_kind}")

        self.__motion_kind = motion_kind

    def reset_state_index(self) -> None:
        """
        キャラクターの状態フレームインデックスをリセット
        """
        self.__state_frame_idx = 0

    def increment_state_index(self) -> None:
        """
        キャラクターの状態フレームインデックスをインクリメント
        """
        self.__state_frame_idx += 1
        if self.__state_frame_idx >= self.get_now_motion().get_frame_length():
            self.__state_frame_idx = 0

    def is_end_of_motion(self) -> bool:
        """モーションの最後のフレームに到達したかどうかを判定"""
        return self.__state_frame_idx == self.get_now_motion().get_frame_length() - 1

    def get_position(self) -> Position:
        """
        キャラクターの位置を取得
        Returns:
            list[int, int]: 位置 (x, y)
        """
        return self.__position

    def get_acceleration(self):
        """
        キャラクターの加速度を取得
        Returns:
            int: 加速度
        """
        return self.__accelaration

    def get_character(self) -> Character:
        """
        キャラクターの定義を取得
        Returns:
            Character: キャラクターの定義
        """
        return self.__character

    def get_motion(self, state: str) -> Motion:
        """
        キャラクターのモーションを取得
        """
        return self.__character.get_motion(state)

    def get_now_motion(self) -> Motion:
        """
        キャラクターの現在のモーションを取得
        Returns:
            Motion: 現在のモーション
        """
        return self.get_motion(self.__motion_kind)

    def get_motion_index(self) -> int:
        """
        キャラクターの現在の状態フレームインデックスを取得
        Returns:
            int: 状態フレームインデックス
        """
        return self.__state_frame_idx

    def is_controllable(self) -> bool:
        """
        キャラクターが操作可能かどうかを取得
        Returns:
            bool: 操作可能ならTrue、そうでなければFalse
        """
        is_controlable = self.get_now_motion().is_controlable(self.__state_frame_idx)
        return is_controlable and self.__is_player

    def get_state_frame_idx(self) -> int:
        """
        キャラクターの現在の状態フレームインデックスを取得
        Returns:
            int: 状態フレームインデックス
        """
        return self.__state_frame_idx

    def get_motion_kind(self) -> MotionKind:
        """
        キャラクターの現在のモーション種類を取得
        Returns:
            MotionKind: 現在のモーション種類
        """
        return self.__motion_kind

    def get_side(self) -> Side:
        """
        キャラクターの向きを取得
        Returns:
            Side: 向き
        """
        return self.__side
