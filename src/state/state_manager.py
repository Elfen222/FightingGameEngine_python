from typing import Any, Iterable, Optional
from state.abstruct_state import AbstractState
from state.route import route


class StateManager:
    """ステートのスタック管理とデリゲーション"""

    def __init__(self):
        self.states: list[AbstractState] = []

    def push_state(self, state: AbstractState, request: Optional[dict[str, Any]] = None) -> None:
        if self.states:
            # 既存トップを一時停止
            self.states[-1].pause()
        self.states.append(state)
        state.initialize(request)

    def pop_state(self) -> Optional[AbstractState]:
        if not self.states:
            return None
        top = self.states.pop()
        top.on_exit()
        if self.states:
            # 復帰
            self.states[-1].resume()
        return top

    def switch_state(self, state: AbstractState, context: Optional[Any] = None) -> None:
        """現在のステートを置き換える（pop → push）"""
        self.pop_state()
        self.push_state(state, context)

    def handle_events(self, events: Iterable[Any]) -> None:
        if self.states:
            self.states[-1].handle_events(events)

    def update(self, dt: int = 0) -> None:
        if self.states:
            current = self.states[-1]
            current.update(dt)

            # 遷移チェック（update 後に安全に実行）
            if current.pop_flg:
                self.pop_state()
            elif current.goto_state:
                # route から次のステートクラスを取得
                next_state_class = route.get(current.goto_state)
                if next_state_class:
                    next_state = next_state_class()
                    self.switch_state(next_state, current.request)
                # フラグをリセット
                current.goto_state = None
                current.request = {}

    def draw(self) -> None:
        if self.states:
            self.states[-1].draw()

    def get_current_state(self) -> Optional[AbstractState]:
        return self.states[-1] if self.states else None
