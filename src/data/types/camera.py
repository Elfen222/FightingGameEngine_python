import pygame
from dataclasses import dataclass
from data.types.position import Position

@dataclass
class Camera:
    position: Position
    width: int
    height: int

    def to_rect(self) -> pygame.Rect:
        """カメラの位置とサイズからpygame.Rectを生成する"""
        return pygame.Rect(
            self.position.x,
            self.position.y,
            self.width,
            self.height
        )

