class Vehicle:
    def __init__(self):
        print("vehicle class")
class Car(Vehicle):
    def __init__(self):
        print("car is derived from vehcile")
    def showcar(self,color):
        print(f"car color is {color}")
class Bike(Vehicle):
    def __init__(self):
        print("Bike is derived from vehcile")
class ElectricCar(Car):
    def __init__(self):
        print("electric vechicle is derived from car")

e=ElectricCar()
e.showcar("blue")
c=Car()
b=Bike()