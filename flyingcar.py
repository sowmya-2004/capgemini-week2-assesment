class Aeroplane:
    def __init__(self):
        print("Aeroplane class")
    def Move(self):
        print("move in the air")
class Car:
    def __init__(self):
        print("Car class")
    def Move(self):
        print("car moves on the road")
class FlyingCar(Car,Aeroplane):
    def __init__(self):
        print("flying car class")
    def Move(self):
        print("flyingcar can move on road and air")

f=FlyingCar()
f.Move()
