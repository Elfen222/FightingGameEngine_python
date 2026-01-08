import tkinter as tk
from tkinter import ttk

from frame import AbstractFrame as fr

class CharacterInfoFrame(fr.AbstractFrame):
    def __init__(self, parent_frame, character):
        super().__init__(parent_frame)

        # キャラクターID
        self.objects.append(fr.WidgetObject(parent_frame, "Character ID", "Entry"))

        # キャラクター名
        self.objects.append(fr.WidgetObject(parent_frame, "Character Name", "Entry"))

        # 最大HP
        self.objects.append(fr.WidgetObject(parent_frame, "HP", "Entry"))

        # 最大スタンゲージ
        self.objects.append(fr.WidgetObject(parent_frame, "Stan Gauge", "Entry"))

        # 歩行情報
        #self.objects["WALK"] = tk.Frame(self.frame)

        # セーブボタン
        self.objects.append(fr.WidgetObject(parent_frame, "Save", "Button", {"command": lambda:self.update_to_character_info(character)}))

        super().pack()

    def set_character_info(self, character):
        self.objects[0].obj.insert(0, character.character_id)
        self.objects[1].obj.insert(0, character.name)
        self.objects[2].obj.insert(0, character.hp)
        self.objects[3].obj.insert(0, character.stan_gauge)

    def update_to_character_info(self, character):
        character.character_id = self.objects[0].obj.get()
        character.name = self.objects[1].obj.get()
        character.hp = self.objects[2].obj.get()
        character.stan_gauge = self.objects[3].obj.get()
        print(character.to_json())
