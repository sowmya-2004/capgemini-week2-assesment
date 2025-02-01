class Shape:
    def __init__(self):
        print("class shape")
    def Area():
        pass
class Square(Shape):
    def __init__(self,a):
        print("class square")
        self.a=a
    def Area(self):
        print(f"area of sqyare is {self.a*self.a}")
class Triangle(Shape):
    def __init__(self,a,b):
        print("class Triangle")
        self.a=a
        self.b=b
    def Area(self):
        print(f"area of triangle is {self.a*self.b}")

t=Triangle(20,2)
t.Area()
s=Square(5)
s.Area()