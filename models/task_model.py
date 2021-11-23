from gui.listeners import ProgressChangeListner, TaskSubtasksStateChangeListener


class TaskModel:
    def __init__(self, parent=None):
        self.title = ""
        self.subtasks = []
        self.parent = parent

        self.completion = 0

        self.substasks_state_listenters = []
        self.progress_change_listeners = []

    def add_subtask(self, task):
        self.subtasks.append(task)
        self.update_progress_based_on_subtasks()
        self.notify_subtasks_change()

    def destroy(self):
        if self.parent:
            self.parent.remove_subtask(self)

    def set_completion(self, progress: int):
        self.completion = progress
        if self.parent:
            self.parent.update_progress_based_on_subtasks()
        self.notify_progress_change()

    def update_progress_based_on_subtasks(self):
        new_progress = 0
        for subtask in self.subtasks:
            new_progress += subtask.completion
        self.completion = new_progress // len(self.subtasks)
        if self.parent:
            self.parent.update_progress_based_on_subtasks()
        self.notify_progress_change()

    def remove_subtask(self, task):
        self.subtasks.remove(task)
        self.update_progress_based_on_subtasks()
        self.notify_subtasks_change()

    def notify_subtasks_change(self):
        for l in self.substasks_state_listenters:
            l.on_subtask_state_change()

    def attach_subtasks_change_listener(self, l: TaskSubtasksStateChangeListener):
        self.substasks_state_listenters.append(l)

    def notify_progress_change(self):
        for l in self.progress_change_listeners:
            l.on_progress_change()

    def attach_progress_change_listener(self, l: ProgressChangeListner):
        self.progress_change_listeners.append(l)
