import os
from typing import Dict, Tuple

from constants import const
from defs.motion import MotionKind
from assets.layer import Layer


class AnimationCache:
    """
    モーションのアニメーション(Layer)をキャッシュして取得するユーティリティ。

    依存を集約することで、spec 層が Layer(Pygame Surface) を直接扱わない設計に寄せる。
    """

    __character_cache: Dict[Tuple[str, MotionKind], Layer] = {}
    __stage_cache: Dict[Tuple[str, str], Layer] = {}

    @classmethod
    def get_character_layer(cls, character_name: str, motion_kind: MotionKind) -> Layer:
        key = (character_name, motion_kind)
        if key in cls.__character_cache:
            return cls.__character_cache[key]

        layer = Layer()
        gif_path = os.path.join(
            const.ASSETS_DIR,
            const.CHARACTERS_DIR,
            character_name,
            f"{motion_kind}.gif",
        )
        layer.gif_to_layer(gif_path)
        cls.__character_cache[key] = layer
        return layer

    @classmethod
    def get_stage_layer(cls, stage_folder: str, image_file_name: str) -> Layer:
        key = (stage_folder, image_file_name)
        if key in cls.__stage_cache:
            return cls.__stage_cache[key]

        layer = Layer()
        gif_path = os.path.join(
            const.ASSETS_DIR,
            const.STAGES_DIR,
            stage_folder,
            image_file_name,
        )
        layer.gif_to_layer(gif_path)
        cls.__stage_cache[key] = layer
        return layer
