import tkinter as tk
from tkinter import ttk

class AbstractFrame:
    def __init__(self, parent_frame):
        self.frame = ttk.Frame(parent_frame)
        self.frame.pack()
        self.objects = []

    def pack(self):
        for obj in self.objects:
            obj.pack()

class WidgetObject:
    def __init__(self, parent_frame, name, obj_type, addtional_info=None, position=tk.TOP):
        self.name = name
        self.obj_type = obj_type
        self.position = position

        self.label = None
        self.obj = None
        if obj_type == "Entry":
            self.label = ttk.Label(parent_frame, text=name)
            self.obj = ttk.Entry(parent_frame)
        elif obj_type == "Label":
            self.obj = ttk.Label(parent_frame, text=name)
        elif obj_type == "Button":
            self.obj = ttk.Button(parent_frame, text=name, command=addtional_info["command"])
        elif obj_type == "Combobox":
            self.label = ttk.Label(parent_frame, text=name)
            self.obj = ttk.Combobox(parent_frame, values=addtional_info["values"])
        elif obj_type == "CheckButton":
            self.label = ttk.Label(parent_frame, text=name)
            self.obj = ttk.Checkbutton(parent_frame)
        elif obj_type == "Frame":
            self.obj = ttk.Frame(parent_frame)
        elif obj_type == "Notebook":
            self.obj = ttk.Notebook(parent_frame)
        elif obj_type == "Progressbar":
            self.label = ttk.Label(parent_frame, text=name)
            self.obj = ttk.Progressbar(parent_frame)
        elif obj_type == "Scale":
            self.label = ttk.Label(parent_frame, text=name)
            self.obj = ttk.Scale(parent_frame)
        elif obj_type == "Scrollbar":
            self.obj = ttk.Scrollbar(parent_frame)
        elif obj_type == "Treeview":
            self.obj = ttk.Treeview(parent_frame, columns=self.additionalInfo["columns"], show=self.additionalInfo["show"])
        elif obj_type == "Canvas":
            self.label = ttk.Label(parent_frame, text=name)
            self.obj = tk.Canvas(parent_frame, width=100, height=100)
        else:
            raise ValueError("Invalid object type")

    def pack(self):
        # ラベルとオブジェクトをパック
        if self.label is not None:
            self.label.pack(side = self.position)
        self.obj.pack(side = self.position)

