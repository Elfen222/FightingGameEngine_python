class Trigger:
    def __init__(self, frame_index: int):
        self.__frame_index: int = frame_index # トリガー発生フレーム

    def get_frame_index(self) -> int:
        """
        トリガー発生フレームを取得
        Returns:
            int: トリガー発生フレーム
        """
        return self.__frame_index
