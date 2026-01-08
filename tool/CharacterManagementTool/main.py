#!/usr/bin/env python3
import os, sys, time
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import time
import CharacterInfo
import ActionState
import HitBox
from frame import CharacterInfoFrame, ActionStateInfoFrame
import json

class PaletteAnimatorApp:
    def __init__(self, master):
        # 16色のパレットカラー
        self.palette: list[str] = [
            "#000000", "#800000", "#008000", "#808000",
            "#000080", "#800080", "#008080", "#c0c0c0",
            "#808080", "#ff0000", "#00ff00", "#ffff00",
            "#0000ff", "#ff00ff", "#00ffff", "#ffffff"
        ]

        # キャラクター情報を初期化
        self.character = self.create_new_character()

        self.master = master
        self.master.title("Palette Animator")

        # ---------------------------------------------------------------------------
        # メニューバー
        # ---------------------------------------------------------------------------
        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar)

        # メニューバーにファイルメニューを追加
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New Character", command=self.create_new_character_json)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="save Character", command=self.save_character_json)
        self.menu_bar.add_command(label="Exit", command=self.master.quit)

        # ---------------------------------------------------------------------------
        # タブ作成
        # ---------------------------------------------------------------------------
        self.tab_control = tk.ttk.Notebook(self.master)
        self.tab_control.pack(expand=1, fill="both")

        # ---------------------------------------------------------------------------
        #
        # キャラクター基本情報タブ
        #
        # ---------------------------------------------------------------------------
        self.character_info_tab = tk.Frame(self.tab_control)
        self.tab_control.add(self.character_info_tab, text="Character Info")

        # ---------------------------------------------------------------------------
        # キャラクター情報フレーム
        # ---------------------------------------------------------------------------
        self.character_info_frame = CharacterInfoFrame.CharacterInfoFrame(self.character_info_tab, self.character)
        self.character_info_frame.set_character_info(self.character)

        # ---------------------------------------------------------------------------
        #
        # アニメーション、ステート、ヒットボックス調整タブ
        #
        # ---------------------------------------------------------------------------
        self.animation_tab = tk.Frame(self.tab_control)
        self.tab_control.add(self.animation_tab, text="Animation")

        # ---------------------------------------------------------------------------
        # アクションステート、キャンパスフレーム
        # ---------------------------------------------------------------------------
        self.action_state_canvas_frame = tk.Frame(self.animation_tab)
        self.action_state_canvas_frame.pack()

        # ---------------------------------------------------------------------------
        # アクションステートリスト
        # ---------------------------------------------------------------------------
        self.action_state_list = tk.Frame(self.action_state_canvas_frame)
        self.action_state_list.pack(side="left")
        self.action_state_list_box = tk.Listbox(self.action_state_list, selectmode="single")
        self.action_state_list_box.pack()
        self.import_action_state_list()

        # 新規作成ボタン
        self.create_button = tk.Button(self.action_state_list, text="Create", command=self.create_new_character)
        self.create_button.pack()

        # ロードボタン

        # ---------------------------------------------------------------------------
        # アクションステート情報フレーム
        # ---------------------------------------------------------------------------
        self.action_state_info_frame = tk.Frame(self.action_state_canvas_frame)
        self.action_state_info_frame.pack(side="left")

        self.action_state_info = ActionStateInfoFrame.ActionStateInfoFrame(self.action_state_info_frame, self.character.action_state[0])
        self.action_state_info.set_action_state_info(self.character.action_state[0])


        # ---------------------------------------------------------------------------
        # キャンパスフレーム
        # ---------------------------------------------------------------------------
        self.canvas_frame = tk.Frame(self.action_state_canvas_frame)
        self.canvas_frame.pack(side="left")

        # キャンパス
        self.canvas = tk.Canvas(self.canvas_frame, width=128, height=128)
        self.canvas.pack()

        # 画像を作成
        self.frames = [self.create_frame(color) for color in self.palette]

        # 画像を表示
        self.canvas.create_image(0, 0, image=self.frames[0], anchor="nw")

        # フレーム前ボタン
        self.prev_frame_button = tk.Button(self.canvas_frame, text="Prev Frame", command=self.prev_frame)
        self.prev_frame_button.pack(side="left")

        # フレーム次ボタン
        self.next_frame_button = tk.Button(self.canvas_frame, text="Next Frame", command=self.next_frame)
        self.next_frame_button.pack(side="right")

        # パレット一覧
        self.display_palette(self.palette)
        self.palette_slider = tk.Scale(self.canvas_frame, orient="horizontal", from_=0, to=15, command=self.select_color)
        self.palette_slider.pack()

        # ---------------------------------------------------------------------------
        # ヒットボックステーブル
        # ---------------------------------------------------------------------------
        self.hitbox_frame = tk.Frame(self.animation_tab)
        self.hitbox_frame.pack()

        # ヒットボックス設定表
        self.hitbox_table = ttk.Treeview(self.hitbox_frame, columns=("ID", "Type", "Left Top", "Right Bottom"), show="headings")
        self.hitbox_table.heading("ID", text="ID")
        self.hitbox_table.heading("Type", text="Type")
        self.hitbox_table.heading("Left Top", text="Left Top")
        self.hitbox_table.heading("Right Bottom", text="Right Bottom")
        self.hitbox_table.pack()

    def prev_frame(self):
        pass

    def next_frame(self):
        pass

    def generate_header(self):
        pass

    def display_palette(self, palette_colors):
        pass

    def create_frame(self, color):
        image = Image.new("RGB", (256, 256), (0, 0, 0))
        return ImageTk.PhotoImage(image)

    def start_stop_animation(self):
        if self.animating:
            self.stop_animation()
        else:
            self.start_animation()

    def start_animation(self):
        self.animating = True
        fps = self.fps_slider.get()
        delay = 1 / fps
        frame_index = 0
        while self.animating:
            self.canvas.create_image(0, 0, image=self.frames[frame_index], anchor="nw")
            self.master.update()
            time.sleep(delay)
            frame_index = (frame_index + 1) % 16

    def stop_animation(self):
        self.animating = False

    def select_color(self):
        color_index = self.palette_slider.get()
        color = self.palette[color_index]
        print("Selected color:", color)

    def create_new_character(self):
        # キャラクター情報を作成
        character = CharacterInfo.CharacterInfo(
            character_id=0,
            name="New Character",
            hp=100,
            stan_gauge=100,
            forward_walk_mortion=None,
            backword_walk_mortion=None,
            forward_dash_mortion=None,
            backword_dash_mortion=None,
            action_state=[]
        )

        # アクションステート情報を作成
        action_state = ActionState.ActionState(
            action_state_id=0,
            name="New State",
            command="",
            occurrence_frame=0,
            duration_frame=0,
            end_frame=0,
            is_loop=False,
            down_attack_type=0,
            cancel_state_id_list=[],
            hit_box_list=[],
            use_gauge=False
        )

        # ヒットボックス情報を作成
        hit_box = HitBox.HitBox(
            hitBoxId=0,
            leftTop=(0, 0),
            rightBottom=(0, 0),
            damage=0,
            stanValue=0,
            hitBack=0,
            abNormalStateId=0
        )

        action_state.hit_box_list.append(hit_box)
        character.action_state.append(action_state)

        return character

    def create_new_character_json(self):
        self.character = self.create_new_character()


    def create_new_action_state(self):
        self.character.actionState.append(ActionState.ActionState(
            actionStateId=0,
            actionStateName="New State",
            command="",
            occurrenceFrame=0,
            durationFrame=0,
            endFrame=0,
            isLoop=False,
            downAttackType=0,
            cancelStateIdLIst=[],
            hitBoxList=[],
            useGauge=False
        ))
        self.import_action_state_list()

    def import_action_state_list(self):
        self.action_state_list_box.delete(0, tk.END)
        for action_state in self.character.action_state:
            self.action_state_list_box.insert(tk.END, action_state.name)

    def load_character_json(self):
        pass

    def load_hitbox_json(self):
        pass

    def save_hitbox_json(self):
        pass

    def save_character_json(self):
        self.character.to_json()

        # キャラクター情報をJSON形式で保存
        # スペースは＿に変換
        character_json = self.character.to_json()
        saveFileDir = "./jsons/" + self.character.name.replace(" ", "_") + ".json"
        with open(saveFileDir, "w") as f:
            json.dump(character_json, f, indent=4)

def main():
    root = tk.Tk()
    app = PaletteAnimatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
