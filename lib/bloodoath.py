from datetime import datetime

class BloodOath:
 
    all = []
    
    def __init__(self, cult, follower, date):
        self.cult = cult
        self.follower = follower
        if isinstance(date, str):
            self.date = str(datetime.strptime(date, '%Y-%m-%d'))
        BloodOath.all.append(self)

    
