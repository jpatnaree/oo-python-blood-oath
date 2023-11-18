from .bloodoath import BloodOath

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
        if isinstance(new_age, str):
            self._age = new_age
        else:
            raise Exception('new_age must be a string')
        
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
        return BloodOath(self, cult)
    
    @classmethod
    def of_a_certain_age(cls, int):
        return [f for f in Follower.all if f.age >= int]