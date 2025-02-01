class Animal:
    def __init__(self):
        print("Animal class")
    def speak(self):
        print("animals do different sounds")
class Dog(Animal):
    def __init__(self):
        print("dog class")
    def speak(self):
        print("dog barks")
class Cat(Animal):
    def __init__(self):
        print("cat class")
    def speak(slef):
        #calling parent class method
        super().speak()
        print("cat walks")

c=Cat()
c.speak()
d=Dog()
d.speak()