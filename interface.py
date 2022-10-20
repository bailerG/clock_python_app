from tkinter import *
from tkinter.ttk import *

import main


class ClockUi:

    def __init__(self, the_window):
        self._alarm_time = None
        self._winsound = None
        self._platform = None
        self._alarm_status_label = None
        self._set_alarm_button = None
        self._alarm_instructions_label = None
        self._get_alarm_time_entry = None
        self._alarm_tab = None
        self._date_label = None
        self._time_label = None
        self._clock_tab = None
        self._tabs_control = None

        self._the_window = the_window
        self._the_window.title("Clock")
        self._the_window.geometry('1300x550')
        self.tabs()
        self.clock_tab()
        self.alarm_tab()

    def tabs(self):
        self._tabs_control = Notebook(self._the_window)
        self._tabs_control.pack(expand=1, fill="both")

    def clock_tab(self):
        self._clock_tab = Frame(self._tabs_control)
        self._tabs_control.add(self._clock_tab, text="Clock")
        self._time_label = Label(self._clock_tab, font='calibri 190 bold', foreground='black')
        self._time_label.pack(anchor='center')
        self._date_label = Label(self._clock_tab, font='calibri 40 bold', foreground='black')
        self._date_label.pack(anchor='s')
        self.update_clock()

    def update_clock(self):
        self._time_label.config(text=main.Clock().get_time())
        self._date_label.config(text=main.Clock().get_date())
        self._time_label.after(1000, self.update_clock)

    def alarm_tab(self):
        self._alarm_tab = Frame(self._tabs_control)
        self._tabs_control.add(self._alarm_tab, text="Alarm")
        self._get_alarm_time_entry = Entry(self._alarm_tab, font='calibri 15 bold')
        self._get_alarm_time_entry.pack(anchor='center')
        self._alarm_instructions_label = Label(self._alarm_tab, font='calibri 10 bold',
                                               text="Enter Alarm Time. Eg -> 01:30 PM, 01 -> Hour, 30 -> Minutes")
        self._alarm_instructions_label.pack(anchor='s')
        self._set_alarm_button = Button(self._alarm_tab, text="Set Alarm", command=self.alarm_set)
        self._set_alarm_button.pack(anchor='s')
        self._alarm_status_label = Label(self._alarm_tab, font='calibri 15 bold')
        self._alarm_status_label.pack(anchor='s')

    def alarm_set(self):
        self._alarm_time = self._get_alarm_time_entry.get()
        main.Clock().alarm(self._alarm_time)


app = Tk()
my_clock = ClockUi(app)
app.mainloop()
