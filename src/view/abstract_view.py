from abc import ABC, abstractmethod
import pygame

class AbstractView(ABC):
    # TODO: 必要なメソッドを洗い出す
    def __init__(self, screen: pygame.Surface):
        self._screen: pygame.Surface = screen

    @abstractmethod
    def draw(self):
        self._screen.fill((0, 0, 0))  # デフォルトは黒でクリア
