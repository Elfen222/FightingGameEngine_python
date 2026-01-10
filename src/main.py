#!/usr/bin/env python3
import pygame
import sys

from config import config
from data.runtime.entity import Entity
from data.types.position import Position
from keyInput import KeyInput
from constants import const, stage_list
from state.state_manager import StateManager
from state.battle_state import BattleState
# import ipdb; ipdb.set_trace()

# 初期化
# TODO: 画面サイズやステージの設定を外部ファイルから読み込むようにする
const.get_asset_dir()
pygame.init()

screen: pygame.Surface = pygame.display.set_mode(config.window_size, flags=0)
pygame.display.set_caption("格闘ゲームエンジン")

# 背景の読み込み
Stage = stage_list.STAGE_LIST['SeaStage']

# エンティティの呼び出し
EntityList: list[Entity] = []
entity = Entity('TestCharacter', True)
entity.set_position(Position(Stage.get_width() // 2, Stage.get_height() - Stage.get_floor_height()))
EntityList.append(entity)

# ステート管理の初期化
state_manager: StateManager = StateManager()
state_manager.push_state(BattleState(), {
    "entity": EntityList,
    "stage": Stage,
    "screen": screen
})

keyInput = KeyInput()

# メインループ
clock = pygame.time.Clock()
running:     bool = True
frame_idx:   int = 0
frame_timer: int = 0
while running:
    dt: int = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    state_manager.handle_events(pygame.event.get())
    state_manager.update(dt)
    state_manager.draw()

    pygame.display.flip()

# 終了処理
pygame.event.clear()
pygame.display.quit()
pygame.quit()
sys.exit()
