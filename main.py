import tkinter as tk
from gui.date_selector import DateSelectorGUI

from db.db import Base, engine, get_db
from db.task import Task
from gui.multiple_task import MultipleTasksGUI
from models.task_model import TaskModel

# --- Creates GUI and initializes database ---

root = tk.Tk()

Base.metadata.create_all(bind=engine)


date_selector = DateSelectorGUI(root)


tasks = [TaskModel(), TaskModel()]
my_tasks = MultipleTasksGUI(root, tasks)

date_selector.pack()
my_tasks.pack()

add_btn = tk.Button(root, text="New", command=lambda: my_tasks.add_new_task())
add_btn.pack()


root.mainloop()
