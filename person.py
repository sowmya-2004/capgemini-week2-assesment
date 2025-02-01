class Person:
    def __init__(self,name):
        self.name=name
    def details(self):
        print(f"name is {self.name}")
class Employee(Person):
    def __init__(self,name,work,dept):
        super().__init__(name)
        self.work=work
        self.dept=dept
    def details(self):
        #calling parent class
        super().details()
        print(f"name is {self.name}, work is {self.work}, department is {self.dept}")
class Manager(Employee):
    def __init__(self,name,work,dept,team):
        super(). __init__(name,work,dept)
        self.team=team

    def details(self):
        #calling parent class
        super().details()
        print(f"name is {self.name}, work is {self.work}, department is {self.dept} and team is {self.team}")
    
    def approve_leave(self,days):
        if(days<=7):
          print("leave approved")
        else:
            print("leave not approved")
m=Manager("sowmya","developer","Development","A")
m.details()
m.approve_leave(6)
m.approve_leave(10)