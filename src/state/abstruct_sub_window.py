from abc import ABC, abstractmethod
from constants.window_kind import WindowKind

# 抽象化する必要ある？
class AbstractSubWindow(ABC):
    title: str
    window_kind: WindowKind
    menu_items: list[str]

    def __init__(self, title: str, window_kind: WindowKind, menu_items: list[str] = []):
        self.title = title
        self.window_kind = window_kind
        self.menu_items = menu_items

    @abstractmethod
    def open(self):
        pass