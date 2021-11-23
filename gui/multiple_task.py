import tkinter as tk
from typing import List
from db.db import get_db

from db.task import Task
from gui.task import TaskGUI


class MultipleTasksGUI(tk.Frame):
    def __init__(self, parent, tasks: List[Task]):
        super().__init__(parent)

        self.tasks = [TaskGUI(self, task) for task in tasks]
        for task in self.tasks:
            task.pack()

    def add_new_task(self):
        with get_db() as db:
            new_task_gui = TaskGUI(self, Task.create_and_save_new_task(db))
            self.tasks.append(new_task_gui)
            new_task_gui.pack()
