class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def show(self):
        print(f"name is {self.name}, rollno is {self.rollno}")

students=[]
n=int(input("enter no.of students"))
for i in range(n):
    name=input(f"enter the name of student {i+1} ")
    rollno=input("enter the author of book")
    details=Student(name,rollno)
    students.append(details)
for x in students:
    x.show()

# wanted=input("enter wanted student details")
# for x in students:
#     if x.name==wanted:
#         print(x)