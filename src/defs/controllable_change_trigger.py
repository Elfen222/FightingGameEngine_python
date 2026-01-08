from defs.trigger import Trigger

class ControllableChangeTrigger(Trigger):
    def __init__(self, frame_index: int, is_controlable: bool):
        super().__init__(frame_index)
        self.__is_controlable: bool = is_controlable  # 操作可能情報

    def is_controlable(self) -> bool:
        """
        速度情報を取得
        Returns:
            Velocity: 速度情報
        """
        return self.__is_controlable
