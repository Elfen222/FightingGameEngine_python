class HitBox:
    def __init__(self, hitBoxId, leftTop, rightBottom, damage, stanValue, hitBack, abNormalStateId):
        self.id = hitBoxId
        self.leftTop = leftTop
        self.rightBottom = rightBottom
        self.damage = damage
        self.stanValue = stanValue
        self.hitBack = hitBack
        self.abNormalStateId = abNormalStateId

    def to_json(self):
        return {
            "id": self.id,
            "leftTop": self.leftTop,
            "rightBottom": self.rightBottom,
            "damage": self.damage,
            "stanValue": self.stanValue,
            "hitBack": self.hitBack,
            "abNormalStateId": self.abNormalStateId
        }
