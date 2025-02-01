from abc import ABC, abstractmethod

class IVehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(IVehicle):
    def start_engine(self):
        return "Car engine started"

    def stop_engine(self):
        return "Car engine stopped"

class Bike(IVehicle):
    def start_engine(self):
        return "Bike engine started"

    def stop_engine(self):
        return "Bike engine stopped"

class Truck(IVehicle):
    def start_engine(self):
        return "Truck engine started"

    def stop_engine(self):
        return "Truck engine stopped"

car = Car()
bike = Bike()
truck = Truck()

print(car.start_engine())
print(car.stop_engine())

print(bike.start_engine())
print(bike.stop_engine())

print(truck.start_engine())
print(truck.stop_engine())
