import tkinter as tk
from tkinter import ttk
from tkinter.constants import BOTH
from ttkthemes import ThemedStyle
from gui.date_selector import DateSelectorGUI

from db.db import Base, engine
from gui.multiple_task import MultipleTasksGUI
from models.task_model import TaskModel

# --- Creates GUI and initializes database ---

root = tk.Tk()


s = ThemedStyle(root)
s.theme_use("ubuntu")

root.geometry("640x480")


Base.metadata.create_all(bind=engine)


date_selector = DateSelectorGUI(root)


tasks = [TaskModel(), TaskModel()]
my_tasks = MultipleTasksGUI(root, tasks)

date_selector.pack()
my_tasks.pack(fill=BOTH)

add_btn = ttk.Button(root, text="New", command=lambda: my_tasks.add_new_task())
add_btn.pack(side="bottom")


root.mainloop()
