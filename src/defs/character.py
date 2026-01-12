import json
import os

from constants.box_kind import BoxKind
from constants import const, key
from data.types.velocity import Velocity
from data.types.position import Position
from defs.motion import Motion, MotionKind
from defs.layer_change_trigger import LayerChangeTrigger
from defs.velocity_change_trigger import VelocityChangeTrigger
from defs.controllable_change_trigger import ControllableChangeTrigger
from defs.box import Box

from icecream import ic

class Character:
    """
    キャラクター情報クラス

    Args:
        maxHp (int): 最大HP
        speed (list[int]): 各方向のの移動速度
        folder_name (str): キャラクターのフォルダ名
    """

    def __init__(self, character_name: str):
        """
        jsonファイルからキャラクターの情報を読み込む
        """
        with open(os.path.join(const.ASSETS_DIR, const.CHARACTERS_DIR, character_name, 'config.json')) as f:
            config = json.load(f)

        self.__character_folder: str = character_name
        self.__max_hp: int = config["max_hp"]
        self.__motion_dict: dict[MotionKind, Motion] = {}
        self.__command_dict: dict[MotionKind, list[int]] = {}

        for motion_kind in config["motion"]:
            motion = config["motion"][motion_kind]
            frame_length: int = motion["frame_length"]
            layer_frame_step_trigger: list[LayerChangeTrigger] = list(map(
                lambda t: LayerChangeTrigger(t["frame"], t["layer_index"]),
                motion["layer_frame_step_trigger"]
            ))
            controllable_change_trigger: list[ControllableChangeTrigger] = list(map(
                lambda t: ControllableChangeTrigger(t["frame"], t["controllable"]),
                motion["controllable_change_trigger"]
            ))
            velocity_change_trigger: list[VelocityChangeTrigger] = list(map(
                lambda t: VelocityChangeTrigger(t["frame"], Velocity(t["velocity"][0], t["velocity"][1])),
                motion["velocity_change_trigger"]
            ))
            for trigger in motion["hitbox_change_trigger"]:
                box_list: list[Box] = []
                for h in trigger["hitbox_list"]:
                    kind: BoxKind = h["kind"]
                    box_map = h["box_map"]
                    start: Position = Position(box_map["start"][0], box_map["start"][1])
                    end:   Position = Position(box_map["end"][0], box_map["end"][1])
                    box_list.append(Box(kind, start, end))
            holdable: bool = motion["holdable"]
            is_loop: bool = motion["is_loop"]
            self.__motion_dict[motion_kind] = Motion(frame_length, layer_frame_step_trigger,
                                                     controllable_change_trigger,
                                                     velocity_change_trigger, holdable, is_loop)

            # コマンド情報の読み込み
            if "command" in config["motion"][motion_kind]:
                command = config["motion"][motion_kind]["command"]
                self.__command_dict[motion_kind] = list(map(lambda x: key.INPUT_MAP[x], command))

    def get_character_folder(self) -> str:
        """
        キャラクターのフォルダ名を取得
        Returns:
            str: キャラクターのフォルダ名
        """
        return self.__character_folder

    def get_max_hp(self) -> int:
        """
        キャラクターの最大HPを取得
        Returns:
            int: 最大HP
        """
        return self.__max_hp

    def get_command_dict(self) -> dict[MotionKind, list[int]]:
        return self.__command_dict

    def get_motion_kind_list(self) -> list[MotionKind]:
        return list(self.__motion_dict.keys())

    def get_motion(self, motion_kind: str) -> Motion:
        """
        キャラクターのモーション情報を取得
        Args:
            motion (Motion): モーションの種類
        Returns:
            Motion: モーション情報
        """
        return self.__motion_dict[motion_kind]

    def has_motion(self, motion_kind: MotionKind) -> bool:
        """
        キャラクターが指定されたモーションを持っているかどうかを取得
        Args:
            motion_kind (MotionKind): モーションの種類
        Returns:
            bool: 指定されたモーションを持っているかどうか
        """
        return motion_kind in self.__motion_dict

    def get_holdable_dict(self) -> dict[MotionKind, bool]:
        """
        キャラクターの各モーションのホールド可能フラグ辞書を取得
        Returns:
            dict[MotionKind, bool]: 各モーションのホールド可能フラグ辞書
        """
        holdable_dict: dict[MotionKind, bool] = {}
        for motion_kind in self.__motion_dict.keys():
            holdable_dict[motion_kind] = self.__motion_dict[motion_kind].is_holdable()
        return holdable_dict
