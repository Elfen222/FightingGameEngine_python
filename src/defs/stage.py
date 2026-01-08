import json
import os

from enum import Enum
from constants import const


class Stage:
    """
    ステージ情報を管理するクラス

    Args:
        stage (str): ステージ名

    """

    def __init__(self, stage_name: str):
        with open(os.path.join(const.ASSETS_DIR, const.STAGES_DIR, stage_name, 'config.json')) as f:
            config = json.load(f)

        self.__stage_name:   str = stage_name
        self.__stage_size:   tuple[int, int] = config["stage_size"]
        self.__floor_height: int = config["floor_height"]
        self.__image_file_name_list: list[str] = config["image_file_name_list"]

    def get_stage_name(self):
        """
        ステージ名を取得
        Returns:
            str: ステージ名
        """
        return self.__stage_name

    def get_image_file_name_list(self) -> list[str]:
        """
        ステージのレイヤーファイル名を取得
        Returns:
            list[str]: ステージのレイヤーファイル名のリスト
        """
        return self.__image_file_name_list

    def get_stage_size(self):
        """
        ステージのサイズを取得
        Returns:
            tuple[int, int]: ステージのサイズ (幅, 高さ)
        """
        return self.__stage_size

    def get_width(self):
        """
        ステージの幅を取得
        Returns:
            int: ステージの幅
        """
        return self.__stage_size[0]

    def get_height(self):
        """
        ステージの高さを取得
        Returns:
            int: ステージの高さ
        """
        return self.__stage_size[1]

    def get_floor_height(self):
        """
        ステージの床の高さを取得
        Returns:
            int: 床の高さ
        """
        return self.__floor_height
