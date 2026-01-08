import ActionState

class CharacterInfo:
    def __init__(self, character_id, name, hp, stan_gauge, forward_walk_mortion, backword_walk_mortion, forward_dash_mortion, backword_dash_mortion, action_state):
        self.character_id = character_id
        self.name = name
        self.hp = hp
        self.stan_gauge = stan_gauge
        self.forward_walk_mortion = forward_walk_mortion
        self.backward_walk_mortion = backword_walk_mortion
        self.forward_dash_mortion = forward_dash_mortion
        self.backward_dash_mortion = backword_dash_mortion
        self.action_state = action_state

    def to_json(self):
        return {
            "id": self.character_id,
            "name": self.name,
            "maxHp": self.hp,
            "maxStanGauge": self.stan_gauge,
            "forwardWalkMortion": self.forward_walk_mortion,
            "backwordWalkMortion": self.backward_walk_mortion,
            "forwardDashMortion": self.forward_dash_mortion,
            "backwordDashMortion": self.backward_dash_mortion,
            "actionState": [action.to_json() for action in self.action_state]
        }
