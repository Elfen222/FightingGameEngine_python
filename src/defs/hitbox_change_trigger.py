from defs.trigger import Trigger
from defs.box import Box

class HitboxChangeTrigger(Trigger):
    def __init__(self, frame_index: int, hitbox_list: list[Box]):
        super().__init__(frame_index)
        self.__hitbox_list: list[Box] = hitbox_list  # ヒットボックスリスト

    def get_hitbox_list(self) -> list[Box]:
        """
        レイヤーインデックスを取得
        Returns:
            int: レイヤーインデックス
        """
        return self.__hitbox_list

