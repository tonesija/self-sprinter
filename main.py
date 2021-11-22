import tkinter as tk

from db.db import Base, engine, get_db
from db.task import Task

root = tk.Tk()

my_labal = tk.Label(root, text="Hello world!")

my_labal.pack()

Base.metadata.create_all(bind=engine)

with get_db() as db:
    db.add(Task(title="Test"))

root.mainloop()
