import tkinter as tk
from tkinter import ttk

from frame import AbstractFrame as fr

class ActionStateListFrame(fr.AbstractFrame):
    def __init__(self, parent_frame):
        super().__init__(parent_frame)

        # ステートリスト

        super().pack()

    def set_state_list(self, action_states):
        for action_state in action_states:
            self.state_list.insert("", "end", values=(action_state.id, action_state.name))
