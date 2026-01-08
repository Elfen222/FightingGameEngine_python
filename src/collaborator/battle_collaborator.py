from data.runtime.entity import Entity
from data.types.input_history import InputHistory
from dataclasses import dataclass


@dataclass
class BattleCollaborator:
    entity_list: list[Entity]
    input_history: list[InputHistory]
