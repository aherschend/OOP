class Car:

    def __init__(self,model,make,speed):
        self.__year_model = model
        self.__make = make
        self.__speed = 0

    def set_year__model(self,model):
        self.__year_model = model

    def set_make(self,make):
        self.__make = make
    
    def set_speed(self,speed):
        self.__speed = 0

    #get the returns

    def get_year_model(self):
        return self.__year_model

    def get_make(self):
        return self.__make

    def get_speed(self):
        return self.__speed

    #get the methods for accelarate and slow down

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -=5

    def get_speed(self):
        return self.__speed 

