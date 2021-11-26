from tkinter import ttk
from tkinter.constants import BOTH, LEFT, RIGHT
from typing import List
from tkinter import Y, RIGHT

from gui.task import TaskGUI
from models.task_model import TaskModel


class MultipleTasksGUI(ttk.Frame):
    def __init__(self, parent, tasks: List[TaskModel]):
        super().__init__(parent)

        self.scrollbar = ttk.Scrollbar(self)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.task_frame = ttk.Frame(self)
        self.task_frame.pack(side=LEFT, fill=BOTH)

        self.tasks = [TaskGUI(self.task_frame, task) for task in tasks]
        for task in self.tasks:
            task.pack()

    def add_new_task(self):
        new_task_gui = TaskGUI(self.task_frame, TaskModel())
        self.tasks.append(new_task_gui)
        new_task_gui.pack()
