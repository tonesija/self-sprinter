from tkinter import Button, Entry, Frame
from db.db import get_db

from db.task import Task


class TaskGUI(Frame):
    def __init__(self, parent, task_db: Task = None):
        super().__init__(parent)

        self.task_db = task_db
        self.title_entry = Entry(self)
        self.title_entry.insert(0, task_db.title)

        self.progress_entry = Entry(self)
        self.progress_entry.insert(0, f"{self.task_db.progress}/100")

        self.delete_btn = Button(self, text="X", command=lambda: self.delete_task())

        self.title_entry.grid(row=1, column=1)
        self.progress_entry.grid(row=1, column=2)
        self.delete_btn.grid(row=1, column=3)

    def delete_task(self):
        with get_db() as db:
            self.task_db.delete(db)
        self.pack_forget()
