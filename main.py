import tkinter as tk
from gui.date_selector import DateSelectorGUI

from db.db import Base, engine, get_db
from db.task import Task
from gui.multiple_task import MultipleTasksGUI
from gui.task import TaskGUI

# --- Creates GUI and initializes database ---

root = tk.Tk()

date_selector = DateSelectorGUI(root)

add_btn = tk.Button(root, text="New", command=lambda: print("heey"))

with get_db() as db:
    db.add(Task(title="Test..."))
    db.add(Task(title="Test 2"))
    db.commit()
    tasks = db.query(Task).all()
    my_tasks = MultipleTasksGUI(root, tasks)

date_selector.pack()
my_tasks.pack()
add_btn.pack()

Base.metadata.create_all(bind=engine)

root.mainloop()
