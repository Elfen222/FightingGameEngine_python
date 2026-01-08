import HitBox

class ActionState:
    def __init__(self, action_state_id, name, command, occurrence_frame, duration_frame, end_frame, is_loop, down_attack_type, cancel_state_id_list, hit_box_list, use_gauge):
        self.action_state_id = action_state_id
        self.name = name
        self.command = command
        self.occurrence_frame = occurrence_frame
        self.duration_frame = duration_frame
        self.end_frame = end_frame
        self.is_loop = is_loop
        self.down_attack_type = down_attack_type
        self.cancel_state_id_list = cancel_state_id_list
        self.hit_box_list = hit_box_list
        self.use_gauge = use_gauge

    def to_json(self):
        return {
            "id": self.action_state_id,
            "name": self.name,
            "command": self.command,
            "occurrenceFrame": self.occurrence_frame,
            "durationFrame": self.duration_frame,
            "endFrame": self.end_frame,
            "isLoop": self.is_loop,
            "downAttackType": self.down_attack_type,
            "cancelStateIdList": self.cancel_state_id_list,
            "hitBoxList": [hit_box.to_json() for hit_box in self.hit_box_list],
            "useGauge": self.use_gauge
        }
