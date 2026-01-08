from typing import Any, Iterable, Optional
import pygame
from logic.battle_logic import BattleLogic
from collaborator.battle_collaborator import BattleCollaborator
from view.battle_view import BattleView
from state.abstruct_state import AbstractState
from keyInput import KeyInput
from defs.stage import Stage

#from icecream import ic


class BattleState(AbstractState):
    """バトル画面のステート。ロジック・ビュー・入力を束ねる。"""

    def __init__(self) -> None:
        super().__init__()

    def initialize(self, request: Optional[Any] = None) -> None:
        """
        request の想定:
        {
          "entity": list[Entity],
          "stage": StageInfo,
          "screen": pygame.Surface
        }
        """
        if request is None:
            raise ValueError("BattleState.initialize requires request parameter")

        stage: Stage = request.get("stage")
        self.key_input: KeyInput = KeyInput()
        self.screen = request.get("screen")
        self.logic = BattleLogic(request.get("entity"), stage)

        self.view = BattleView(stage, self.screen)

    def handle_events(self, events: Iterable[Any]) -> None:
        # ここではキーの押下状態だけ KeyInput に反映
        pressed = pygame.key.get_pressed()
        self.key_input.set_button(pressed)

    def update(self, dt: int = 0) -> None:
        collaborator: BattleCollaborator = self.logic.calc(self.key_input)
        self.view.update(dt, collaborator)

    def draw(self) -> None:
        self.view.draw()

    def on_exit(self) -> None:
        # 必要ならここでクリーンアップ
        pass
