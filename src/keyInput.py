import pygame
from config import config
from constants import key

PRESSED_STR: dict[int, str] = {
    key.UP:     "U",
    key.DOWN:   "D",
    key.LEFT:   "L",
    key.RIGHT:  "R",
    key.LOW_P:  "LP",
    key.MID_P:  "MP",
    key.HIGH_P: "HP",
    key.LOW_K:  "LK",
    key.MID_K:  "NK",
    key.HIGH_K: "HK",
    key.START:  "ST"
}

class KeyInput(object):
    def __init__(self):
        self.__pressed = {
            key.UP:     False,
            key.DOWN:   False,
            key.LEFT:   False,
            key.RIGHT:  False,
            key.LOW_P:  False,
            key.MID_P:  False,
            key.HIGH_P: False,
            key.LOW_K:  False,
            key.MID_K:  False,
            key.HIGH_K: False,
            key.START:  False
        }

    def __eq__(self, other):
        if not isinstance(other, KeyInput):
            return False
        return self.__pressed == other.__pressed

    def __ne__(self, other):
        return not self.__eq__(other)

    def set_button(self, input_key: pygame.key.ScancodeWrapper):
        for button in self.__pressed.keys():
            self.__pressed[button] = input_key[config.key_config[button]]

        # 上下左右同時押し無効化
        if self.__pressed[key.UP] and self.__pressed[key.DOWN]:
            self.__pressed[key.UP] = False
            self.__pressed[key.DOWN] = False

        if self.__pressed[key.LEFT] and self.__pressed[key.RIGHT]:
            self.__pressed[key.LEFT] = False
            self.__pressed[key.RIGHT] = False

    def is_pressed(self, input_key: int) -> bool:
        if input_key not in self.__pressed:
            raise ValueError(f"Invalid key: {input_key}")
        return self.__pressed[input_key]

    def get_pressed(self) -> dict[int, bool]:
        """
        現在のキー入力状態を表す辞書を返します。

        Returns:
            dict[int, bool]: 各キーの押下状態（True: 押されている, False: 押されていない）
        """
        return self.__pressed

    def to_str(self) -> str:
        """
        キー入力を文字列に変換
        """
        result = ""

        for key in self.__pressed.keys():
            if self.__pressed[key]:
                result += PRESSED_STR[key] + " "

        return result.strip()
