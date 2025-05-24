# Assignment : 08 => Super () Function

class Person():
    def  __init__(self,name):
        self.name=name
class Teacher (Person):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject=subject
    def location(self):
        return f"{self.name} teaches {self.subject} in School."
t1=Teacher("Sara","Math")
print(t1.location())        