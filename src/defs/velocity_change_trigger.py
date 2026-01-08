from defs.trigger import Trigger
from data.types.velocity import Velocity

class VelocityChangeTrigger(Trigger):
    def __init__(self, frame_index: int, velocity: Velocity):
        super().__init__(frame_index)
        self.__velocity: Velocity = velocity  # 速度情報

    def get_velocity(self) -> Velocity:
        """
        速度情報を取得
        Returns:
            Velocity: 速度情報
        """
        return self.__velocity
