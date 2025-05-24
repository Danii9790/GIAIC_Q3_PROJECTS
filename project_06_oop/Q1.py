# Assignment : 01 => Using (Self) us a parameter
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print(f"Name : {self.name} , Marks : {self.marks}.")

result=Student("Daniyal","78")
result.display()
