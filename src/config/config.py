import json
import pygame
from constants import const
from constants import key

# ウィンドウサイズ
window_size: tuple[int, int] = (const.DEFAULT_SCREEN_WIDTH, const.DEFAULT_SCREEN_HEIGHT)

# キーコンフィグ
key_config: dict[int, int] = {
    key.UP:     pygame.K_SPACE,
    key.DOWN:   pygame.K_d,
    key.LEFT:   pygame.K_s,
    key.RIGHT:  pygame.K_f,
    key.LOW_P:  pygame.K_u,
    key.MID_P:  pygame.K_i,
    key.HIGH_P: pygame.K_o,
    key.LOW_K:  pygame.K_j,
    key.MID_K:  pygame.K_k,
    key.HIGH_K: pygame.K_l,
    key.START:  pygame.K_RETURN
}

# 設定ファイル読込
config_file = "config.json"
try:
    with open(config_file, "r", encoding="utf-8") as f:
        config_data = json.load(f)

        # キー設定を取得
        key_config_str = config_data.get("key_config", {})
        if len(key_config_str) == {}:
            print("No key configuration found in the config file.")
        else:
            for _input, _key in key_config_str.items():
                if _input in key.INPUT_MAP and _key in key.KEY_MAP:
                    key_config[key.INPUT_MAP[_input]] = (key.KEY_MAP[_key])
                else:
                    print("Invalid key mapping in config file:",
                          f"{_input} -> {_key}")

        # ウィンドウサイズを取得
        window_size = config_data.get( "window_size", (const.DEFAULT_SCREEN_WIDTH, const.DEFAULT_SCREEN_HEIGHT))

except FileNotFoundError:
    print(f"Config file '{config_file}'",
          "not found. Using default settings.")
