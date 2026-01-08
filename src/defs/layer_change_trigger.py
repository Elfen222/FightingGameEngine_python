from defs.trigger import Trigger

class LayerChangeTrigger(Trigger):
    def __init__(self, frame_index: int, layer_index: int):
        super().__init__(frame_index)
        self.__layer_index: int = layer_index  # レイヤーインデックス

    def get_layer_index(self) -> int:
        """
        レイヤーインデックスを取得
        Returns:
            int: レイヤーインデックス
        """
        return self.__layer_index
