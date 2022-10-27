from tkinter import *
from tkinter.ttk import *

import main


class ClockUi:

    def __init__(self, the_window):
        self._label_update = None
        self._get_stopwatch = main.Clock()
        self._running_stopwatch = None
        self._stopwatch_reset = None
        self._stopwatch_stop = None
        self._stopwatch_start = None
        self._stopwatch_label = None
        self._stopwatch_tab = None
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
        self.stopwatch_tab()

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

    def stopwatch_tab(self):
        self._stopwatch_tab = Frame(self._tabs_control)
        self._tabs_control.add(self._stopwatch_tab, text='Stopwatch')
        self._stopwatch_label = Label(self._stopwatch_tab, font='calibri 40 bold', text='Stopwatch')
        self._stopwatch_label.pack(anchor='center')
        self._stopwatch_start = Button(self._stopwatch_tab, text='Start', command=self.start_stopwatch)
        self._stopwatch_start.pack(anchor='center')
        self._stopwatch_stop = Button(self._stopwatch_tab, text='Stop', state='disabled', command=self.stop_stopwatch)
        self._stopwatch_stop.pack(anchor='center')
        self._stopwatch_reset = Button(self._stopwatch_tab, text='Reset', state='disabled', command=self.reset_stopwatch)
        self._stopwatch_reset.pack(anchor='center')

    def start_stopwatch(self):
        self._stopwatch_start.config(state='disabled')
        self._stopwatch_stop.config(state='enabled')
        self._stopwatch_reset.config(state='enabled')
        self.stopwatch_loop()

    def stop_stopwatch(self):
        self._stopwatch_start.config(state='enabled')
        self._stopwatch_stop.config(state='disabled')
        self._stopwatch_reset.config(state='enabled')
        self._running_stopwatch = self._get_stopwatch.stopwatch(False)
        self._stopwatch_label.after_cancel(self._label_update)

    def stopwatch_loop(self):
        self._stopwatch_label.config(text=self._get_stopwatch.stopwatch(True))
        self._label_update = self._stopwatch_label.after(1000, self.stopwatch_loop)

    def reset_stopwatch(self):
        self.stop_stopwatch()
        self._stopwatch_label.config(text='Stopwatch')
        self._stopwatch_start.config(state='enabled')
        self._stopwatch_stop.config(state='disabled')
        self._stopwatch_reset.config(state='disabled')
        self._get_stopwatch.reset_stopwatch()


app = Tk()
my_clock = ClockUi(app)
app.mainloop()
