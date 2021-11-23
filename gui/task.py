from tkinter import Button, Checkbutton, Entry, Frame, IntVar, Label
from db.db import get_db

from db.task import Task
from gui.listeners import ProgressChangeListner


class TaskGUI(Frame):
    def __init__(self, parent, task_db: Task):
        super().__init__(parent)

        self.task_db = task_db
        self.title_entry = Entry(self)
        self.title_entry.insert(0, task_db.title)

        self.delete_btn = Button(self, text="X", command=lambda: self.delete_task())

        self.title_entry.grid(row=1, column=1)
        self.delete_btn.grid(row=1, column=3)

    def delete_task(self):
        with get_db() as db:
            self.task_db.delete(db)
        self.pack_forget()


class TaskAtomicGUI(TaskGUI):
    def __init__(self, parent, task_db: Task):
        super().__init__(parent, task_db)

        self.checked = IntVar()

        self.checkbox = Checkbutton(self, variable=self.checked)

        self.checkbox.grid(row=1, column=2)


class TaskParentGUI(TaskGUI, ProgressChangeListner):
    def __init__(self, parent, task_db: Task):
        super().__init__(parent, task_db)

        self.subtasks = [TaskGUI(self, task) for task in task_db.subtasks]

        self.progress_label = Label(self, text="0/100")

    def on_progress_change(self):
        # TODO recalculate progress
        pass
