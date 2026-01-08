import tkinter as tk
from tkinter import ttk

from frame import AbstractFrame as fr

class ActionStateInfoFrame(fr.AbstractFrame):
    def __init__(self, parent_frame, action_state):
        super().__init__(parent_frame)

        # ID
        self.objects.append(fr.WidgetObject(parent_frame, "ID", "Entry"))

        # ステート名
        self.objects.append(fr.WidgetObject(parent_frame, "State Name", "Entry"))

        # コマンド
        self.objects.append(fr.WidgetObject(parent_frame, "Command", "Combobox", {"values": ["A", "B", "C"]}))

        # 発生フレーム
        self.objects.append(fr.WidgetObject(parent_frame, "Start Frame", "Entry"))

        # 持続フレーム
        self.objects.append(fr.WidgetObject(parent_frame, "Duration Frame", "Entry"))

        # 終了フレーム
        self.objects.append(fr.WidgetObject(parent_frame, "End Frame", "Entry"))

        # ループフレーム
        self.objects.append(fr.WidgetObject(parent_frame, "Loop Frame", "CheckButton"))

        # ダウン攻撃タイプ
        self.objects.append(fr.WidgetObject(parent_frame, "Down Attack Type", "Combobox", {"values": ["A", "B", "C"]}))

        # ゲージ使用量
        self.objects.append(fr.WidgetObject(parent_frame, "Gauge Usage", "Entry"))

        # セーブボタン
        self.objects.append(fr.WidgetObject(parent_frame, "Save", "Button", {"command": lambda:self.update_to_action_state_info(action_state)}))

        super().pack()

    def set_action_state_info(self, action_state):
        self.objects[0].obj.insert(0, action_state.action_state_id)
        self.objects[1].obj.insert(0, action_state.name)
        self.objects[2].obj.insert(0, action_state.command)
        self.objects[3].obj.insert(0, action_state.occurrence_frame)
        self.objects[4].obj.insert(0, action_state.duration_frame)
        self.objects[5].obj.insert(0, action_state.end_frame)
        self.objects[6].obj.variable = action_state.is_loop
        self.objects[7].obj.insert(0, action_state.down_attack_type)
        self.objects[8].obj.insert(0, action_state.use_gauge)

    def update_to_action_state_info(self, action_state):
        action_state.id = self.objects[0].obj.get()
        action_state.name = self.objects[1].obj.get()
        action_state.command = self.objects[2].obj.get()
        action_state.occurrence_frame = self.objects[3].obj.get()
        action_state.duration_frame = self.objects[4].obj.get()
        action_state.end_frame = self.objects[5].obj.get()
        action_state.is_loop = self.objects[6].obj.variable
        action_state.down_attack_type = self.objects[7].obj.get()
        action_state.use_gauge = self.objects[8].obj.get()
        print(action_state.to_json())
