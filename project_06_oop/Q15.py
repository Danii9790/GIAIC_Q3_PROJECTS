"""
Assignment:
Create four classes:

A with a method show(),

B and C that inherit from A and override show(),

D that inherits from both B and C.

Create an object of D and call show() to observe MRO.


"""

class A:
    def show(self):
        print("A")
class B(A):
    def show(self):
        print("B")
class C(A):
    def show(self):
        print("C")
class D(B,C):
    pass
d=D()
d.show()

# Another Example:
class Staff:
    def role(self):
        print("General Staff Duties")
class Teacher(Staff):
    def role(self):
        print("Teaching Students")
class Administrartor(Staff):
    def role(self):
        print("Managing School Adminstrartion")
        
class Principle(Teacher,Administrartor): # output is (Teacher Role) beacause Teacher in parameter pass in first.
    pass

p = Principle()
p.role()