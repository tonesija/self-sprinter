import tkinter as tk

import datetime
from datetime import date

from gui.listeners import DateChangeListener


class DateSelectorGUI(tk.Frame):
    """GUI element that consists of a selected date label and buttons
    to change the selected date."""

    def __init__(self, parent):
        """Constructs a date selector widget.

        Args:
            parent (widget): parent widget.
        """

        super().__init__(parent)

        self.date_label = tk.Label(self, text=date.today())
        self.left_btn = tk.Button(
            self,
            text="<<",
            command=lambda: self.change_selected_date(-1),
        )
        self.right_btn = tk.Button(
            self,
            text=">>",
            command=lambda: self.change_selected_date(1),
            state=tk.DISABLED,
        )

        self.date_label.grid(row=1, column=2)
        self.left_btn.grid(row=1, column=1)
        self.right_btn.grid(row=1, column=3)

        self.date_change_listeners = []
        self.notify_date_changed()

    def change_selected_date(self, for_days: int):
        """Change the date display label by the number of days.
        If the new date is the same as today, disable the next button.

        Args:
            for_days (int): number of days
        """

        selected_date = datetime.datetime.strptime(
            self.date_label["text"], "%Y-%m-%d"
        ).date()

        new_date = selected_date + datetime.timedelta(days=for_days)
        self.date_label.config(text=new_date)

        if new_date == date.today():
            self.right_btn.config(state=tk.DISABLED)
        else:
            self.right_btn.config(state=tk.ACTIVE)

        self.notify_date_changed()

    def notify_date_changed(self):
        """Notify the date changed listeners of a date change."""

        for l in self.date_change_listeners:
            l.on_date_change(date(self.date_label["text"]))

    def attach_date_changed_listener(self, l: DateChangeListener):
        """Attach a date change listener.

        Args:
            l (DateChangeListener)
        """

        self.date_change_listeners.append(l)
