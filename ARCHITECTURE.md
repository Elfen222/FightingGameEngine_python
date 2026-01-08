# アーキテクチャ概要（data と defs の切り分け）

この文書は、本プロジェクトにおける `data/` と `defs/` の責務と依存関係の指針を定義します。迷ったときはまずここを読み、追加/変更前にチェックリストで確認してください。

## 目的
- 仕様（不変の設計情報）と、実行時状態（可変のゲーム状態）を分離し、見通しと変更容易性を高める。
- レイヤー間の依存方向を固定し、循環依存や責務の混在を防ぐ。

## フォルダの責務

- `defs/`（Blueprints / Immutable Definitions）
  - ゲーム内の「定義・仕様・設計書」をコードで表現した層。
  - 例: キャラクターの最大HP、移動速度、各モーションのフレーム数や当たり判定(Box)など。
  - 特徴: 基本的に「不変」。ロード後に内容を書き換えない（データクラスは `frozen=True` を推奨）。
  - 外部アセットの「パスやキー」を持ってもよいが、Pygame Surface などの実体（重いリソース）を保持しない。

- `data/types/`（Value Objects / Basic Types）
  - 基本的な値オブジェクトを定義する層。
  - 例: `Position`, `Velocity`, `Vec2` など、ゲーム全体で使われる基本型。
  - 特徴: 不変または単純な値を表現。ビジネスロジックを持たない。

- `data/runtime/`（Runtime State / Mutable Models）
  - 実行時に変化するゲーム状態を表す層。
  - 例: `Entity` の現在位置、速度、現在のモーションインデックス、入力履歴など。
  - 特徴: 「可変」。ゲームループ中に頻繁に更新される。
  - `defs/` の定義を「参照」して振る舞いを決める。

- `assets/` or `resources/`（Optional: ローダ/キャッシュ）
  - 実ファイル（画像・音・JSON）をロードし、キャッシュする層。
  - 例: `Layer`（Pygame Surface 群）はここ、または `view/` に近い層に置く。
  - `defs/` はアセットのキー/パスだけを持ち、Surface 等の実体はこの層で管理。

- `logic/`
  - ゲーム進行・当たり判定・遷移などのドメインロジック。
  - `data.runtime/` を更新し、参照先として `defs/` を読むことは OK。`view/` や Surface に直接依存しないこと。

- `view/`
  - 描画やアニメーションの更新、UI 系。
  - `data.runtime/` の状態と `assets/` の実体を用いて画面を作る。

## 依存方向（原則）

```
constants/
  ↓
data/types/          # 基本型（Position, Velocity等）
  ↓
defs/                # 仕様定義（Character, Motion等）
  ↓
data/runtime/        # 実行時状態（Entity等）
  ↓
logic/               # ゲームロジック
  ↓
view/                # 描画層
```

**依存ルール：**
- ✅ **許可**: `defs → data.types` （仕様定義が基本型を使うのは自然）
- ❌ **禁止**: `defs → data.runtime` （仕様が実行時状態に依存してはならない）
- ✅ **許可**: `data.runtime → defs` （実行時状態が仕様を参照）
- ✅ **許可**: `logic → defs`, `logic → data.runtime`
- ❌ **禁止**: `logic → view` の強結合

**補足：**
- `assets/` ローダ層は `defs` と `view` の間に位置し、画像・音声などの実体を管理
- Surface や重いリソースは `defs` ではなく `assets` または `view` 層で保持

## 現状の確認（2026-01-06時点）

✅ **実装済み：**
- `defs/` が仕様定義層として機能（`character.py`, `motion.py` など）
- `data/types/` に基本型を配置（`Position`, `Velocity` など）
- `data/runtime/` に実行時状態を配置（`entity.py`）
- `defs → data.runtime` の逆依存は発生していない

⚠️ **今後の改善候補：**
- アセットローダ層（`assets/` または `view/` 内）の明確化
- Pygame Surface の管理方針の統一
- `defs/` 内のデータクラスへの `frozen=True` 適用検討

## 具体例

- `defs/character.py`
  - ✅ OK: `max_hp`, `speed`, `motion` のフレーム構成、当たり判定情報。
  - ✅ OK: `data.types.Position`, `data.types.Velocity` などの基本型を使用。
  - ❌ NG: `pygame.Surface` や `Layer` 実体の保持。→ アセットキーだけにして、描画時に解決。
  - ❌ NG: `data.runtime.Entity` への依存。

- `data/types/position.py`
  - ✅ OK: 座標を表す単純な値オブジェクト。
  - ✅ OK: `defs/` から参照される。

- `data/runtime/entity.py`
  - ✅ OK: 現在位置、現在モーションインデックス、入力可否、加速度等。
  - ✅ OK: `self.__character__` に `Character` (from `defs/`) を参照（読み取り専用として扱う）。
  - ❌ NG: `defs/` 内のクラスがこれを参照すること。

## 追加時チェックリスト
- [ ] これは実行時に変わる状態か？ → 変わるなら `data/runtime/`。
- [ ] それはゲームの設計（定義）であり、不変か？ → 不変なら `defs/`（`frozen dataclass` を検討）。
- [ ] 基本的な値型か？ → `data/types/` に配置。
- [ ] Pygame の Surface や画像/音の「実体」を保持していないか？ → 実体は `assets/`/`view/` に寄せ、`defs/` にはキー/パスのみ。
- [ ] 依存方向は守れているか？
  - `defs → data.types` は OK
  - `defs → data.runtime` は NG
  - `data.runtime → defs` は OK

## 段階的リファクタ提案（今後の方針）
1. アセットローダ層の明確化
   - `assets/animation_cache.py` などを作り、`get_layer(character, motion)` で `Layer` をロード＆キャッシュ。
   - `defs/` からは Surface の実体を除去し、アセットキーのみを保持。
2. `defs/` 内のクラスの不変性強化
   - 可能な箇所で `@dataclass(frozen=True)` を適用。
3. ステージ情報の整理
   - `stage/` も同様の原則に従い、定義と実行時状態を分離。

これにより、`defs` は純粋な仕様定義、`data/runtime` は実行状態、`data/types` は基本型、`assets/view` は描画資源に責務が明確に分離されます。
