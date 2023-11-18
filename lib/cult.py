from bloodoath import BloodOath
from statistics import mean

class Cult:
    
    all = []

    minimum_age = 15

    def __init__(self, name, location, founding_year, slogan):
        self.name = name
        self.location = location
        if isinstance(founding_year, int):
            self.founding_year = founding_year
        self.slogan = slogan
        Cult.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name
        else: 
            raise Exception('new_name must be a string')
        
    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, new_location):
        if isinstance(new_location, str):
            self._location = new_location
        else: 
            raise Exception('new_name must be a string')

    @property
    def slogan(self):
        return self._slogan
    
    @slogan.setter
    def slogan(self, new_slogan):
        if isinstance(new_slogan, str):
            self._slogan = new_slogan
        else: 
            raise Exception('new_slogan must be a string')
        
    @property
    def founding_year(self):
        return self._founding_year
    
    @founding_year.setter
    def founding_year(self, new_founding_year):
        if not hasattr(self, "_founding_year"):
            self._founding_year = new_founding_year
        else:
            raise Exception('founding_year cannot be changed')
        
    
    def recruit_follower(self, follower):
        return BloodOath(self, follower)
    
    def cult_population(self):
        return len([b.follower for b in BloodOath.all if b.cult == self])
    
    @classmethod
    def find_by_name(cls, name):
        return [c for c in Cult.all if c.name == name]
    
    @classmethod
    def find_by_location(cls, locaiton):
        return [c for c in Cult.all if c.location == locaiton]
    
    @classmethod
    def find_by_founding_year(self, founding_year):
        return [c for c in Cult.all if c.founding_year == founding_year]
    
    def recruit_follower(self, follower):
        if not follower.age < Cult.minimum_age:
            BloodOath(self, follower)
        else:
            print(f'Wait until you are {Cult.minimum_age} years old, and we will gladly welcome you to our family')
        
    def average_age(self):
        follower_all_age = [b.age for b in BloodOath.all if b.cult == self]
        return mean(follower_all_age)
    
    def my_followers_mottos(self):
        return [b.life_motto for b in BloodOath.all if b.cult == self]
    


