import datetime
import os
import platform


class Clock:

    def __init__(self):
        self._stopwatch_counter_num = 10800
        self._running = None
        self._alarm_minute = None
        self._alarm_hour = None
        self._seconds = None
        self._minutes = None
        self._hour = None
        self._alarm_time = None
        self._time = None
        self._date = None

    def get_time(self):
        self._time = datetime.datetime.now().strftime("%H:%M:%S")
        self._hour, self._minutes, self._seconds = self._time.split(':')
        return self._time

    def get_date(self):
        self._date = datetime.datetime.now().strftime("%d/%m/%Y")
        return self._date

    def clock_loop(self):
        while True:
            self.get_time()

    def print_time(self):
        self.get_time()
        self.get_date()
        print(self._time, self._date)

    def alarm(self, alarm_time):
        self._alarm_time = alarm_time
        self._alarm_hour, self._alarm_minute = self._alarm_time.split(':')
        self.alarm_loop()

    def alarm_check(self):
        if self._hour == self._alarm_hour and self._minutes == self._alarm_minute:
            self.beep()
            return True
        else:
            return False

    @staticmethod
    def beep():
        for i in range(3):
            if platform.system() == 'Windows':
                winsound.Beep(5000, 1000)
            elif platform.system() == 'Darwin':
                os.system('say Time is Up')
            elif platform.system() == 'Linux':
                os.system('beep -f 5000')

    def alarm_loop(self):
        while self.alarm_check() is False:
            self.get_time()
            self.alarm_check()

    def stopwatch(self, running):
        self._running = running
        while self._running:
            tt = datetime.datetime.fromtimestamp(self._stopwatch_counter_num)
            self._stopwatch_counter_num += 1
            return tt.strftime("%H:%M:%S")

    def reset_stopwatch(self):
        self._stopwatch_counter_num = 10800


# print(Clock().get_stopwatch())
# time.sleep(1)
# print(Clock().get_stopwatch())
# time.sleep(1)
# print(Clock().get_stopwatch())
# time.sleep(1)
# print(Clock().get_stopwatch())
# time.sleep(1)
# print(Clock().get_stopwatch())
# time.sleep(1)
# print(Clock().get_stopwatch())
# time.sleep(1)
# print(Clock().get_stopwatch())
# time.sleep(1)
# print(Clock().get_stopwatch())
