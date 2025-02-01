class Employee:
    def __init__(self,name,id,dept):
        self.name=name
        self.id=id
        self.dept=dept
    def show(self):
        print(f"name is {self.name}, id is {self.id}, department is {self.dept}")

obj=Employee("sowmya","66F2","CSM")
obj.show()