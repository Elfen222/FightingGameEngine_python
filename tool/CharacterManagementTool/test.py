import tkinter as tk
from tkinter import ttk

# Initialize the main window
root = tk.Tk()
root.title("Character Editor")
root.geometry("600x400")

# Create a notebook widget
notebook = ttk.Notebook(root)
info_frame = ttk.Frame(notebook)
state_frame = ttk.Frame(notebook)
notebook.add(info_frame, text="Info")
notebook.add(state_frame, text="State")
notebook.pack(expand=1, fill="both")

# Info Frame Elements
name_label = ttk.Label(info_frame, text="Name")
name_label.grid(row=0, column=0, sticky='W')
name_entry = ttk.Entry(info_frame)
name_entry.grid(row=0, column=1, sticky='W')

hp_label = ttk.Label(info_frame, text="HP")
hp_label.grid(row=1, column=0, sticky='W')
hp_entry = ttk.Entry(info_frame)
hp_entry.grid(row=1, column=1, sticky='W')

stun_label = ttk.Label(info_frame, text="Stun")
stun_label.grid(row=2, column=0, sticky='W')
stun_entry = ttk.Entry(info_frame)
stun_entry.grid(row=2, column=1, sticky='W')

# Animation Section
canvas = tk.Canvas(info_frame, width=100, height=100)
canvas.grid(row=0, column=2, rowspan=3)
left_button = ttk.Button(info_frame, text="<")
left_button.grid(row=3, column=2, sticky='W')
right_button = ttk.Button(info_frame, text=">")
right_button.grid(row=3, column=3, sticky='E')

# Control Buttons
start_button = ttk.Button(info_frame, text="Start")
start_button.grid(row=4, column=2, sticky='W')
stop_button = ttk.Button(info_frame, text="Stop")
stop_button.grid(row=4, column=3, sticky='E')

# Hitbox Table
table = ttk.Treeview(info_frame, columns=("ID", "Type", "Left Top", "Right Bottom"), show="headings")
table.heading("ID", text="ID")
table.heading("Type", text="Type")
table.heading("Left Top", text="Left Top")
table.heading("Right Bottom", text="Right Bottom")
table.grid(row=5, column=0, columnspan=4, sticky='W')

# Start the application
root.mainloop()

