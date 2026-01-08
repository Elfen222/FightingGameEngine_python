from state.battle_state import BattleState
from state.character_select_state import CharacterSelectState

route: dict[str, type] = {
    'CharacterSelectState': CharacterSelectState,
    'BattleState': BattleState
}