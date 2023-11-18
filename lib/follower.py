from bloodoath import BloodOath
from cult import Cult

class Follower:
    
    all = []

    def __init__(self, name, age, life_motto, cult = None):
        self.name = name
        if isinstance(age, int):
            self.age = age
        self.life_motto = life_motto
        self.cult = cult

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
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        if isinstance(new_age, int):
            self._age = new_age
        else:
            raise Exception('new_age must be an integor')
        
    @property
    def life_motto(self):
        return self._life_motto
    
    @life_motto.setter
    def life_motto(self, new_life_motto):
        if isinstance(new_life_motto, str):
            self._life_motto = new_life_motto
        else:
            raise Exception('new_life_motto must be a string')

    def join_cult(self, cult):
        if self.age >= Cult.minimum_age:
            return BloodOath(self, cult)
        else:
            print(f'Wait a little mor, when you turn {Cult.minimum_age}, you can join them again')
    
    @classmethod
    def of_a_certain_age(cls, int):
        return [f for f in Follower.all if f.age >= int]
    
    def fellow_cult_members(self):
        return list(set([b.follower for b in BloodOath.all if b.cult == self and b.name != self]))
    

    def my_cults_slogans(self):
        return [b.slogan for b in BloodOath.all if b.follower == self]
    
charles = Follower("Charles", 23, "I'm the coolest")
manson = Cult("MANSON", "CA", 1974, "I'm Cool")
print(manson)
c1 = BloodOath(manson, charles, "1993-1-1")
print(c1)