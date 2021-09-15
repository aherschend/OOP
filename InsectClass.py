import random

class Insect:
    def __init__(self,w,l):
        self.wings = w
        self.legs = l
        self.flight = 0 

    def flight_length(self):
        self.flight = random.randint(1,10)

    def get_miles(self):
        return self.flight
    
#self - if you have multiple instances of an object, using self makes sure
#we are only interacting with attributes of that instance. 