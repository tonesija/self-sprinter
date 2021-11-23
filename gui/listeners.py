from datetime import date


class DateChangeListener:
    """Listener that will listen to date changes. Date selector GUI component
    will register them."""

    def on_date_change(self, date: date):
        """Triggers when a date is changed.

        Args:
            date (date): new date.
        """

        pass


class ProgressChangeListner:
    """Listener that will listen to a task's progress change. Task model registers them."""

    def on_progress_change(self):
        """Triggers when a task's progress changes."""

        pass


class TaskSubtasksStateChangeListener:
    def on_subtask_state_change(self):
        pass
