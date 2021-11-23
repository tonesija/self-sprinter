import tkinter as tk

import datetime
from datetime import date

from gui.listeners import DateChangeListener


class DateSelectorGUI(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.date_label = tk.Label(self, text=date.today())
        self.left_btn = tk.Button(
            self,
            text="Previous",
            command=lambda: self.change_selected_date(-1),
        )
        self.right_btn = tk.Button(
            self,
            text="Next",
            command=lambda: self.change_selected_date(1),
            state=tk.DISABLED,
        )

        self.date_label.grid(row=1, column=2)
        self.left_btn.grid(row=1, column=1)
        self.right_btn.grid(row=1, column=3)

        self.date_change_listeners = []
        self.notify_date_changed()

    def change_selected_date(self, for_days: int):
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
        for l in self.date_change_listeners:
            l.on_date_change(date(self.date_label["text"]))

    def attach_date_changed_listener(self, l: DateChangeListener):
        self.date_change_listeners.append(l)
