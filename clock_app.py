import datetime

class clock:
    def __init__(self):
        self.date_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S/%p")
        self.date, self.time1 = self.date_time.split()
        self.time2, self.time3 = self.time1.split('/')
        self.hour, self.minutes, self.seconds =  self.time2.split(':')
        # self.format_hour()
        
    
    def format_hour(self):
        if int(self.hour) > 12 and int(self.hour) < 24:
                    self.time = str(int(self.hour) - 12) + ':' + self.minutes + ':' + self.seconds + ' ' + self.time3
                    return self.time
        else:
                self.time = self.time2 + ' ' + self.time3
                return self.time
                
                
    def execute(self):
        while True:
            self.format_hour()
            return self.format_hour()
        
    
# agora = clock()
# agora.execute()