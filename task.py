from tkinter import Entry

from db.task import Task


class TaskGUI(Entry):
    def __init__(self, parent, task_db: Task = None):
        super().__init__(parent)

        self.task_db = task_db
        super().insert(0, task_db.title)
