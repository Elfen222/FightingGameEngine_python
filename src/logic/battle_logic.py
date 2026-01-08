from copy import deepcopy
from keyInput import KeyInput
from data.types.input_history import InputHistory
from data.runtime.entity import Entity
from defs.character import Character
from defs.motion import MotionKind
from defs.stage import Stage
from collaborator.battle_collaborator import BattleCollaborator


class BattleLogic:
    def __init__(self, entity_list: list[Entity], stage: Stage) -> None:
        self.__entity_list = entity_list
        self.__stage = stage
        self.__left_move_flg: bool = False
        self.__right_move_flg: bool = False

        self.__input_history: list[InputHistory] = []

    def calc(self, key_input: KeyInput) -> BattleCollaborator:
        # 入力履歴の保存
        if (len(self.__input_history) == 0 or
                self.__input_history[-1].keyInput != key_input):
            self.__input_history.append(InputHistory(deepcopy(key_input), 1))
            if len(self.__input_history) >= 20:
                self.__input_history.pop(0)
        elif self.__input_history[-1].frameCount < 99:
            self.__input_history[-1].frameCount += 1

        # 入力処理
        for entity in self.__entity_list:
            # TODO:将来的にどう動かすかは要検討
            # 1.入力履歴からコマンド判定を行う
            # 2.コマンドが成立する場合、モーションを変更させ、それに応じてキャラクターの状態を変更させる。
            self.__update_motion(entity)
            motion = entity.get_now_motion()
            entity.get_position().x += motion.get_velocity(entity.get_state_frame_idx()).x
            entity.get_position().y += motion.get_velocity(entity.get_state_frame_idx()).y

        return BattleCollaborator(
            # ディープコピーにする必要はあまりないが、安全策として
            deepcopy(self.__entity_list),
            deepcopy(self.__input_history),
        )

    # コマンド判定用の関数群
    def __update_motion(self, entity: Entity) -> None:
        character: Character = entity.get_character()
        command_dict = character.get_command_dict()
        holdable_dict = character.get_holdable_dict()

        motion_kind: MotionKind
        if entity.is_controllable() is False:
            motion_kind = entity.get_motion_kind()
        else:
            motion_kind = self.__judge_command(command_dict, holdable_dict)
        entity.update_state(motion_kind)

    def __judge_command(self, command_dict: dict[MotionKind, list[int]],
                        holdable_dict: dict[MotionKind, bool]) -> MotionKind:
        """コマンド判定を行う"""

        judged_flg: bool = False
        for motion_kind in command_dict.keys():
            for require_key in command_dict[motion_kind]:
                # TODO: 一旦末尾から取得するように。猶予判定は後々実装。
                # これ連続技の判定とかどうすりゃええねん
                key_input: KeyInput = self.__input_history[-1].keyInput
                if key_input.is_pressed(require_key) and holdable_dict[motion_kind]:
                    judged_flg = True
                    break
                elif key_input.is_pressed(require_key) and self.__input_history[-1].frameCount == 1:
                    judged_flg = True
                    break
                else:
                    continue
            if judged_flg:
                return motion_kind

        return "STAND"

    def __fix_position_over__(self, entity: Entity) -> None:
        """
        ポジションを修正する
        """
        floor_height = self.__stage.get_height() - self.__stage.get_floor_height()
        if entity.get_position().x < 0:
            entity.get_position().x = 0
        if entity.get_position().x > self.__stage.get_width():
            entity.get_position().x = self.__stage.get_width()
        if entity.get_position().y < 0:
            entity.get_position().y = 0
        if entity.get_position().y > floor_height:
            entity.get_position().y = floor_height
            entity.__accelaration = 0
