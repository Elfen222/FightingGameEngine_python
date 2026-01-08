from dataclasses import dataclass
from keyInput import KeyInput


@dataclass
class InputHistory:
    """
    入力履歴
    """
    keyInput: KeyInput
    frameCount: int
