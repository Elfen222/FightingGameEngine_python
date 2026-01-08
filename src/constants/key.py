import pygame

# キー情報
UP:     int = 1
DOWN:   int = 2
LEFT:   int = 4
RIGHT:  int = 8
LOW_P:  int = 16
MID_P:  int = 32
HIGH_P: int = 64
LOW_K:  int = 128
MID_K:  int = 256
HIGH_K: int = 512
START: int = 1024

# 入力マッピング
# コマンド設定ファイル等で使用するためのマッピング
INPUT_MAP: dict[str, int] = {
    "jump":       UP,
    "crouch":     DOWN,
    "left":       LEFT,
    "right":      RIGHT,
    "low_punch":  LOW_P,
    "mid_punch":  MID_P,
    "high_punch": HIGH_P,
    "low_kick":   LOW_K,
    "mid_kick":   MID_K,
    "high_kick":  HIGH_K,
    "start":      START
}

# キーマッピング
# キーボードのキー名からpygameのキーコードへのマッピング
KEY_MAP: dict[str, int] = {
    "UP": pygame.K_UP, "DOWN": pygame.K_DOWN,
    "LEFT": pygame.K_LEFT, "RIGHT": pygame.K_RIGHT,
    "Q": pygame.K_q, "W": pygame.K_w, "E": pygame.K_e, "R": pygame.K_r,
    "T": pygame.K_t, "Y": pygame.K_y, "U": pygame.K_u, "I": pygame.K_i,
    "O": pygame.K_o, "P": pygame.K_p, "A": pygame.K_a, "S": pygame.K_s,
    "D": pygame.K_d, "F": pygame.K_f, "G": pygame.K_g, "H": pygame.K_h,
    "J": pygame.K_j, "K": pygame.K_k, "L": pygame.K_l, "Z": pygame.K_z,
    "X": pygame.K_x, "C": pygame.K_c, "V": pygame.K_v, "B": pygame.K_b,
    "N": pygame.K_n, "M": pygame.K_m, "SPACE": pygame.K_SPACE,
    ';': pygame.K_SEMICOLON, "'": pygame.K_QUOTE,
    '[': pygame.K_LEFTBRACKET, ']': pygame.K_RIGHTBRACKET,
    ',': pygame.K_COMMA, '.': pygame.K_PERIOD,
    '/': pygame.K_SLASH, '\\': pygame.K_BACKSLASH,
    '-': pygame.K_MINUS, '=': pygame.K_EQUALS,
    '0': pygame.K_0, '1': pygame.K_1, '2': pygame.K_2, '3': pygame.K_3,
    '4': pygame.K_4, '5': pygame.K_5, '6': pygame.K_6, '7': pygame.K_7,
    '8': pygame.K_8, '9': pygame.K_9,
    'F1': pygame.K_F1, 'F2': pygame.K_F2, 'F3': pygame.K_F3, 'F4': pygame.K_F4,
    'F5': pygame.K_F5, 'F6': pygame.K_F6, 'F7': pygame.K_F7, 'F8': pygame.K_F8,
    'F9': pygame.K_F9, 'F10': pygame.K_F10, 'F11': pygame.K_F11, 'F12': pygame.K_F12,
    'F13': pygame.K_F13, 'F14': pygame.K_F14, 'F15': pygame.K_F15,
    'ESCAPE': pygame.K_ESCAPE, 'RETURN': pygame.K_RETURN,
    'BACKSPACE': pygame.K_BACKSPACE, 'TAB': pygame.K_TAB,
    'CAPSLOCK': pygame.K_CAPSLOCK, 'NUMLOCK': pygame.K_NUMLOCK,
    'SCROLLLOCK': pygame.K_SCROLLLOCK, 'PRINTSCREEN': pygame.K_PRINTSCREEN,
    'PAUSE': pygame.K_PAUSE, 'INSERT': pygame.K_INSERT,
    'HOME': pygame.K_HOME, 'END': pygame.K_END,
    'PAGEUP': pygame.K_PAGEUP, 'PAGEDOWN': pygame.K_PAGEDOWN,
    'LEFTSHIFT': pygame.K_LSHIFT, 'RIGHTSHIFT': pygame.K_RSHIFT,
    'LEFTCTRL': pygame.K_LCTRL, 'RIGHTCTRL': pygame.K_RCTRL,
    'LEFTALT': pygame.K_LALT, 'RIGHTALT': pygame.K_RALT,
    'LEFTMETA': pygame.K_LMETA, 'RIGHTMETA': pygame.K_RMETA,
    'LEFTSUPER': pygame.K_LSUPER, 'RIGHTSUPER': pygame.K_RSUPER,
}
