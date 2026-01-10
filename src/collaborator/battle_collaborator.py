from data.runtime.entity import Entity
from data.types.input_history import InputHistory
from dataclasses import dataclass


@dataclass(frozen=True)
class BattleCollaborator:
    entity_list: tuple[Entity, ...]
    input_history: tuple[InputHistory, ...]
