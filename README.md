# 格闘ゲームエンジン Python版

バージョン: 0.0.1

## 概要

Pygameを使用した2D格闘ゲームのプロトタイプです。キャラクターモーション、ステージ、入力システムなどの基本的なゲームメカニクスを実装しています。

## 特徴

- キャラクターのモーションシステム（STAND, JUMP, 攻撃など）
- ステージシステムと背景描画
- 入力履歴管理とコマンド入力
- 状態管理システム（State Manager）
- 当たり判定システム
- アニメーションキャッシュ機構

## 必要環境

- Python 3.8以上
- Pygame 2.6.1以上
- その他の依存関係は`src/requirements.txt`を参照

## セットアップ

### 自動セットアップ

```bash
cd src
./init.sh
```

### 手動セットアップ

```bash
cd src
python3 -m venv venv
source venv/bin/activate  # Windowsの場合: venv\Scripts\activate
pip install -r requirements.txt
python3 main.py
```

## プロジェクト構造

```
src/
├── main.py              # エントリーポイント
├── config/              # 設定ファイル
├── constants/           # 定数定義
├── data/
│   ├── types/          # 基本型（Position, Velocity等）
│   └── runtime/        # 実行時状態（Entity等）
├── defs/                # ゲーム仕様定義（Character, Motion等）
├── logic/               # ゲームロジック
├── view/                # 描画層
├── state/               # 状態管理
├── assets/              # アセット（キャラクター、ステージ等）
└── collaborator/        # ヘルパー機能
```

詳細なアーキテクチャについては`src/ARCHITECTURE.md`を参照してください。

## ドキュメント

Sphinxドキュメントをビルドするには：

```bash
cd src
make html
```

ビルドされたドキュメントは`build/html/index.html`から閲覧できます。

## 開発ガイドライン

- コーディング規約、モジュール構成については`src/AGENTS.md`を参照
- 4スペースインデント、型ヒントの使用を推奨
- 関数/変数は`snake_case`、クラスは`PascalCase`
- 定数は大文字で`constants/`に配置

## ライセンス

本プロジェクトはMITライセンスの下で公開されています。詳細は[LICENSE](LICENSE)ファイルを参照してください。

### 使用ライブラリ

本プロジェクトは以下の主要なオープンソースライブラリを使用しています：

- **Pygame** (LGPL v2.1+) - ゲームエンジン
- **Pillow** (HPND License) - 画像処理
- その他のライブラリのライセンスについては各パッケージのドキュメントを参照してください

## 貢献

プルリクエストを歓迎します。大きな変更を行う場合は、まずissueを開いて変更内容を議論してください。

## バージョン履歴

### 0.0.1 (2026-01-08)
- 初期リリース
- 基本的なゲームループとキャラクターシステムの実装
- ステージシステムの実装
- 状態管理システムの実装
