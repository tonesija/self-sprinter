import tkinter as tk
from typing import List

from db.task import Task
from gui.task import TaskGUI


class MultipleTasksGUI(tk.Frame):
    def __init__(self, parent, tasks: List[Task]):
        super().__init__(parent)

        self.tasks = [TaskGUI(self, task) for task in tasks]
        for task in self.tasks:
            task.pack()
