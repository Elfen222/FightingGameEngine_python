import os

# 画面サイズ
DEFAULT_SCREEN_WIDTH:  int = 640
DEFAULT_SCREEN_HEIGHT: int = 400

# ディレクトリ
ASSETS_DIR:     str = 'assets'
STAGES_DIR:     str = 'stages'
CHARACTERS_DIR: str = 'characters'
STAGES:     list[str] = []
CHARACTERS: list[str] = []

print(f'ASSETS_DIR: {ASSETS_DIR}')
print(f'STAGES_DIR: {STAGES_DIR}')
print(f'CHARACTERS_DIR: {CHARACTERS_DIR}')


def get_asset_dir():
    """
    アセットのディレクトリを取得し、
    ステージ、キャラクターのリストを更新する。
    """
    # assetsディレクトリのパスを取得
    assets_dir: str = os.path.join(
                        os.path.dirname(__file__), '../', ASSETS_DIR)
    print(f'assets_dir: {assets_dir}')

    # stagesディレクトリのパスを取得
    stages_dir: str = os.path.join(assets_dir, STAGES_DIR)
    print(f'stages_dir: {stages_dir}')

    # charactersディレクトリのパスを取得
    characters_dir: str = os.path.join(assets_dir, CHARACTERS_DIR)
    print(f'characters_dir: {characters_dir}')

    # stages内に存在するフォルダ名をSTAGESに格納
    STAGES[:] = [name for name in os.listdir(stages_dir)
                 if os.path.isdir(os.path.join(stages_dir, name))]
    CHARACTERS[:] = [name for name in os.listdir(characters_dir)
                     if os.path.isdir(os.path.join(characters_dir, name))]

    print(STAGES)
    print(CHARACTERS)
