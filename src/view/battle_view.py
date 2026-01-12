import pygame
from collaborator.battle_collaborator import BattleCollaborator
from constants import const
from view.abstract_view import AbstractView
from data.types.position import Position
from data.types.input_history import InputHistory
from data.types.camera import Camera
from data.runtime.entity import Entity
from defs.stage import Stage
from assets.layer import Layer
from assets.animation_cache import AnimationCache

from icecream import ic

class BattleView(AbstractView):
    def __init__(self,
                 stage: Stage,
                 screen: pygame.Surface
                 ) -> None:
        super().__init__(screen)
        self.__stage = stage
        self.__dt = 0
        self.__font = pygame.font.SysFont(None, 15)

    def update(self, dt: int, collaborator: BattleCollaborator) -> None:
        """
        更新処理
        """
        self.__dt = dt
        self.__collaborator = collaborator

    def draw(self) -> None:
        """
        描画処理
        """
        entity_list: tuple[Entity, ...] = self.__collaborator.entity_list
        input_history: tuple[InputHistory, ...] = self.__collaborator.input_history

        super().draw()

        # TODO: bilt先をカメラ位置に応じて調整する
        # 背景を描画
        stage_layer_list: list[Layer] = list(map(lambda x:
                                                 AnimationCache.get_stage_layer(self.__stage.get_stage_name(), x),
                                                 self.__stage.get_image_file_name_list()))
        world = pygame.Surface(self.__stage.get_stage_size())
        world.fill((0, 0, 0))
        for stage_layer in stage_layer_list:
            world.blit(stage_layer.frames[0], (0, 0))

        # エンティティを描画
        for entity in entity_list:
            character_folder = entity.get_character().get_character_folder()
            motion_kind = entity.get_motion_kind()
            layer = AnimationCache.get_character_layer(character_folder, motion_kind)

            motion = entity.get_now_motion()
            if 1 <= len(layer.frames):
                frame_idx = entity.get_state_frame_idx()
                layer_frame_idx = motion.get_now_layer_index(frame_idx)
                #if entity.get_motion_kind() == "STAND_LOW_PUNCH":
                #    ic("{}, {}".format(frame_idx, layer_frame_idx))

                rect = layer.frames[0].get_rect()

                world.blit(layer.frames[layer_frame_idx],
                            (entity.get_position().x - rect.width // 2,
                             entity.get_position().y - layer.get_height()))

        # TODO: カメラコントローラクラスを別途実装する。
        # カメラの位置を下記に応じて調整する。
        # 1. エンティティの位置
        # 2. ステージの端
        # 3. 超必殺技の演出時
        # 4. KO時
        entity_pos = entity_list[0].get_position()
        camera_position: Position = Position(
            min(max(0, entity_pos.x), self.__stage.get_width() // 2),
            min(max(0, entity_pos.y), self.__stage.get_height() // 2)
        )
        camera = Camera(camera_position, 320, 200)
        ic(camera.position.to_tuple())
        ic(camera)
        cut = world.subsurface(camera.to_rect())
        scaled = pygame.transform.scale(cut, (const.DEFAULT_SCREEN_WIDTH, const.DEFAULT_SCREEN_HEIGHT))
        self._screen.blit(scaled, (0, 0))

        # 入力履歴を描画
        # TODO: デバッグ用。別メソッドに切り出す。
        y: int = 0
        for i in input_history:
            history = self.__font.render(f"{i.keyInput.to_str()}: {str(i.frameCount)}", True, (0, 0, 0))
            self._screen.blit(history, (0, y))
            y += 20

