from abc import ABC, abstractmethod
from typing import Any, Iterable, Optional


class AbstractState(ABC):
    """
    画面ステートの共通インターフェイス（ライフサイクル）

    推奨ライフサイクル:
    - initialize(context): ステート開始時に一度実行（リソース初期化など）
    - handle_events(events): 入力イベントの処理（pygame.event.get()の結果など）
    - update(dt): 更新処理（ロジック・物理）
    - draw(screen): 描画処理
    - on_exit(): ステート終了時のクリーンアップ
    - pause()/resume(): スタック運用時の一時停止/再開（任意）
    """

    def __init__(self) -> None:
        self.pop_flg: bool = False  # ステートマシンにこのステートをポップするよう指示するフラグ
        self.goto_state: Optional[str] = None  # 遷移先ステート名（必要なら）
        self.request: dict[str, Any] = {}  # ステート間で渡すデータ（必要なら）

    @abstractmethod
    def initialize(self, request: dict[str, Any]) -> None:
        """ステート開始時に1回だけ呼ばれる初期化"""
        raise NotImplementedError

    @abstractmethod
    def handle_events(self, events: Iterable[Any]) -> None:
        """イベント処理（pygame.event の列を想定）"""
        raise NotImplementedError

    @abstractmethod
    def update(self, dt: int = 0) -> None:
        """毎フレームの更新。dt はミリ秒または秒（呼び出し元と合わせる）"""
        raise NotImplementedError

    @abstractmethod
    def draw(self) -> None:
        """描画処理"""
        raise NotImplementedError

    def on_exit(self) -> None:
        """ステート終了時のクリーンアップ。必要な場合だけオーバーライド"""
        pass

    def pause(self) -> None:
        """他ステートにフォーカスが移る際の一時停止。必要な場合だけオーバーライド"""
        pass

    def resume(self) -> None:
        """一時停止からの復帰。必要な場合だけオーバーライド"""
        pass

    def goto(self, state_name: str, pop: bool = False, request: Optional[dict[str, Any]] = None) -> None:
        """指定したステートへ遷移する意思を設定（switch）"""
        self.goto_state = state_name
        self.request = request or {}
        if pop:
            self.pop_flg = True

    def pop(self) -> None:
        """このステートを終了する意思を設定"""
        self.pop_flg = True
