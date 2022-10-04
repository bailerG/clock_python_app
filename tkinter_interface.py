from tkinter import *
from tkinter.ttk import *
import clock_app

# Creates the app window:
window = Tk()
window.title("Clock")
window.geometry('1300x550')

# Adds the tabs for the user to select on the interface:
tabs_control = Notebook(window)
clock_tab = Frame(tabs_control)
alarm_tab = Frame(tabs_control)
stopwatch_tab = Frame(tabs_control)
timer_tab = Frame(tabs_control)
tabs_control.add(clock_tab, text="Clock")
tabs_control.add(alarm_tab, text="Alarm")
tabs_control.add(stopwatch_tab, text='Stopwatch')
tabs_control.add(timer_tab, text='Timer')
tabs_control.pack(expand = 1, fill ="both")

# Adds the looks on the clock tab:
time_label = Label(clock_tab, font = 'calibri 40 bold', foreground = 'black')
time_label.pack(anchor='center')
date_label = Label(clock_tab, font = 'calibri 40 bold', foreground = 'black')
date_label.pack(anchor='s')


def update_ui():
    time_label.config(text = clock_app.clock().execute())
    # date_label.config(text= date)
    time_label.after(1000, update_ui())
    



window.mainloop()