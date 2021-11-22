import tkinter as tk

from db.db import Base, engine, get_db
from db.task import Task
from task import TaskGUI

# --- Creates GUI and initializes database ---

root = tk.Tk()

with get_db() as db:
    db.add(Task(title="Test..."))
    db.commit()
    task = db.query(Task).first()
    my_labal = TaskGUI(root, task)
my_labal.pack()

Base.metadata.create_all(bind=engine)

root.mainloop()
