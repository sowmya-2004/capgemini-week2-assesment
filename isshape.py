from abc import ABC,abstractmethod
class ISshape(ABC):
    @abstractmethod
    def calculate_area():
        pass
class Rectangle(ISshape):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def calculate_area(self):
        print(f"area is {self.a*self.b}")
class Circle(ISshape):
    def __init__(self,a):
        self.a=a
    def calculate_area(self):
        print(f"area is {3.14*self.a*self.a}")

obj=Circle(10)
obj.calculate_area()
obj2=Rectangle(10,5)
obj2.calculate_area()

