# Assignment : 02 => using cls
# jaise self object ko refer karta hai, waise hi cls class ko refer karta hai.
# cls @classmethod ke andar use hota hai. self means "this object" , cls means "this class"

class Counter:
    count= 0
    def __init__ (self):
        Counter.count +=1

    @classmethod
    def show_class(cls):
        print(f"Total {cls.count}")

c1=Counter()
c2=Counter()
c3=Counter()

Counter.show_class()

# Another Example :
class Student:
    school_name="Old school"
    def __init__(self,name):
        self.school_name=name  # The name of variable is same in constructor and classmethod(cls) . if the variable name is different the function work same before and after change.
    @classmethod
    def change_school(cls,new_school):
        cls.school_name=new_school

print("Before : ",Student.school_name)
Student.change_school("New School")
print("After : ",Student.school_name)

        

