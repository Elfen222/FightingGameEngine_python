"""
暫定レイヤーエイリアス

現状、Layer 実装は data/layer.py にありますが、将来的に描画資源は assets/rendering に
集約する方針のため、ここで一時的に再エクスポートします。

TODO:
- 実装本体を assets 側へ移設し、このエイリアスを削除する。
"""

__all__ = ["Layer"]
import pygame
from PIL import Image


class Layer:
    def __init__(self):
        self.frame_count: int = 1
        self.frames: list[pygame.Surface] = []
        self.delays: list[int] = []
        self.size: list[tuple[int, int]] = []

    def gif_to_layer(self, path: str):
        self.__init__()

        pil_gif = Image.open(path)
        try:
            # GIFの各フレームを読み込み
            while True:
                # フレームをRGBAモードに変換
                frame = pil_gif.convert('RGBA')
                mode: str = frame.mode
                size: tuple[int, int] = frame.size
                data: bytes = frame.tobytes()
                surface: pygame.Surface = (
                    pygame.image.fromstring(data, size, mode))
                self.frames.append(surface)
                self.size.append(size)

                # フレームの遅延時間を取得
                self.delays.append(pil_gif.info.get('duration', 100))

                pil_gif.seek(pil_gif.tell() + 1)

        except EOFError:
            pass

    def set_image(self, path: str):
        self.__init__()
        # 画像を読み込み
        surface: pygame.Surface = pygame.image.load(path).convert_alpha()
        self.frames.append(surface)
        self.delays.append(100)
        self.size = [surface.get_size()]

    def get_width(self) -> int:
        """
        レイヤーの幅を取得
        Returns:
            int: レイヤーの幅
        """
        return self.size[0][0]

    def get_height(self) -> int:
        """
        レイヤーの高さを取得
        Returns:
            int: レイヤーの高さ
        """
        return self.size[0][1]


LayerDict = dict[str, Layer]
