import tkinter as tk
from typing import List
from db.db import get_db

from gui.task import TaskGUI
from models.task_model import TaskModel


class MultipleTasksGUI(tk.Frame):
    def __init__(self, parent, tasks: List[TaskModel]):
        super().__init__(parent)

        self.tasks = [TaskGUI(self, task) for task in tasks]
        for task in self.tasks:
            task.grid(row=len(self.grid_slaves()) + 1, column=1)

    def add_new_task(self):
        new_task_gui = TaskGUI(self, TaskModel())
        self.tasks.append(new_task_gui)
        new_task_gui.grid(row=len(self.grid_slaves()) + 1, column=1)
