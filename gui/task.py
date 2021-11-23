from tkinter import *

from tkinter import Button, Checkbutton, Entry, Frame, IntVar, Label
from db.db import get_db

from gui.listeners import ProgressChangeListner, TaskSubtasksStateChangeListener
from models.task_model import TaskModel


class TaskGUI(Frame, TaskSubtasksStateChangeListener, ProgressChangeListner):
    def __init__(self, parent, task_model: TaskModel):
        super().__init__(parent)

        self.task_model = task_model
        self.task_model.attach_subtasks_change_listener(self)
        self.task_model.attach_progress_change_listener(self)
        self.title_entry = Entry(self)
        self.title_entry.insert(0, task_model.title)

        self.add_subtask_btn = Button(
            self, text="˘", command=lambda: self.add_subtask()
        )

        self.delete_btn = Button(self, text="X", command=lambda: self.delete_task())

        self.subtask_list = Frame(self)
        self.subtask_list.config(borderwidth=12)

        self.title_entry.grid(row=1, column=1)
        self.add_subtask_btn.grid(row=1, column=2)
        self.delete_btn.grid(row=1, column=3)
        self.subtask_list.grid(row=2, column=1, columnspan=3)

        self.progress_label = None
        self.checkbox = None
        self.create_checkbox_or_progress_label()

    def delete_task(self):
        self.task_model.destroy()

        if not self.task_model.parent:
            self.pack_forget()

    def add_subtask(self):
        self.task_model.add_subtask(TaskModel(self.task_model))

    def create_checkbox_or_progress_label(self):
        if self.task_model.subtasks:
            self.progress_label = Label(self, text="0/100")
            self.progress_label.grid(row=1, column=4)
            self.update_progress()
        else:
            checked = IntVar()
            self.checkbox = Checkbutton(
                self,
                variable=checked,
                command=lambda: self.task_model.set_completion(checked.get() * 100),
            )
            self.checkbox.grid(row=1, column=4)

    def on_subtask_state_change(self):
        # remove deleted subtasks
        for subtask in self.subtask_list.grid_slaves():
            if subtask.task_model not in self.task_model.subtasks:
                subtask.grid_forget()

        # add added subtasks
        for subtask in self.task_model.subtasks:
            if subtask not in [
                subtask.task_model for subtask in self.subtask_list.grid_slaves()
            ]:
                subtask_gui = TaskGUI(self.subtask_list, subtask)
                subtask_gui.grid(row=self.subtask_list.size()[1], column=1)

        self.create_checkbox_or_progress_label()

    def on_progress_change(self):
        if self.task_model.completion == 100:
            self.config(bg="green")
        else:
            self.config(bg="grey")
        self.update_progress()

    def update_progress(self):
        if self.progress_label:
            self.progress_label.config(text=f"{self.task_model.completion}%")
