import datetime
from tkinter import *
from tkinter.ttk import *

class clock:
    def __init__(self):
        self.set_dateHour()


    def set_dateHour(self):
        self.date_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S/%p")
        self.date, self.time1 = self.date_time.split()
        self.time2, self.time3 = self.time1.split('/')
        self.hour, self.minutes, self.seconds =  self.time2.split(':')
    
    
    def format_hour(self):
        if int(self.hour) > 12 and int(self.hour) < 24:
                self.time = str(int(self.hour) - 12) + ':' + self.minutes + ':' + self.seconds + ' ' + self.time3
                return self.time
        else:
                self.time = self.time2 + ' ' + self.time3
                return self.time
                
                
    def get_hour(self):
        return self.format_hour()
        
    def get_date(self):
        return self.date
         
        
# ---------------------------------------------------------------------------------------------------------------------------- #


class clock_ui:
    def __init__(self, the_window):
        self.the_window = the_window
        self.the_window.title("Clock")
        self.the_window.geometry('1300x550')
        self.tabs()
        self.update_ui()
        

# Adds the tabs for the user to select on the interface:
    def tabs(self):
        self.tabs_control = Notebook(self.the_window)
        self.clock_tab = Frame(self.tabs_control)
        self.alarm_tab = Frame(self.tabs_control)
        self.stopwatch_tab = Frame(self.tabs_control)
        self.timer_tab = Frame(self.tabs_control)
        self.tabs_control.add(self.clock_tab, text="Clock")
        self.tabs_control.add(self.alarm_tab, text="Alarm")
        self.tabs_control.add(self.stopwatch_tab, text='Stopwatch')
        self.tabs_control.add(self.timer_tab, text='Timer')
        self.tabs_control.pack(expand = 1, fill ="both")

        # Adds the looks on the clock tab:
        self.time_label = Label(self.clock_tab, font = 'calibri 190 bold', foreground = 'black')
        self.time_label.pack(anchor='center')
        self.date_label = Label(self.clock_tab, font = 'calibri 40 bold', foreground = 'black')
        self.date_label.pack(anchor='s')
        
    def update_ui(self):
        self.time_label.config(text = clock().get_hour())
        self.date_label.config(text = clock().get_date())
        self.time_label.after(1000, self.update_ui)
        
app = Tk()
my_clock = clock_ui(app)
app.mainloop()
    
# agora = clock()
# agora.execute()