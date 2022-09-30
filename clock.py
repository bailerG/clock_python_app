import datetime

class clock:
    def __init__(self):
        pass

    def set_hour(self):
        date_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S/%p")
        date,time1 = date_time.split()
        time2,time3 = time1.split('/')
        hour,minutes,seconds =  time2.split(':')
        
        if int(hour) > 12 and int(hour) < 24:
                    time = str(int(hour) - 12) + ':' + minutes + ':' + seconds + ' ' + time3
        else:
                time = time2 + ' ' + time3
        
        return date, time
    
    def format_hour(self):
        pass
    
agora = clock()