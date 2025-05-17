# Practice 21 Assignments in Object-oriented programming (OOP)
# Assignment : 01 => Using (Self) us a parameter
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def display(self):
#         print(f"Name : {self.name} , Marks : {self.marks}.")

# s1=Student("Usman",57)
# s1.display()

# Assignment : 02 => using cls
# jaise self object ko refer karta hai, waise hi cls class ko refer karta hai.
# cls @classmethod ke andar use hota hai. self means "this object"
# cls means "this class"

# class Counter:
#     count = 0
#     def __init__(self):
#         Counter.count +=1
    
#     @classmethod
#     def show_count(cls):
#         print(f"Total Objects created : ",cls.count)
    
# c1=Counter()
# c2=Counter()
# c3=Counter()

# Counter.show_count()
# Another example:
# class Student:
#     school_name="Old School"
#     def __init__(self,name):
#         self.school_name=name
#     @classmethod
#     def changing_school(cls,new_name):
#         cls.school_name=new_name

# print("Before : ",Student.school_name)
# Student.changing_school("New Allied School")
# print("After : ",Student.school_name)
        

# Assignment : 03 => Public Variables and Method

# class Car:
#     def __init__(self,brand):
#         self.brand=brand  #Public variable 

#     def start(self):  #Public Method
#         print(f"{self.brand} car is starting...")
# # Create Object
# my_car=Car("Toyata")
# # Access Public variable
# print(my_car.brand)
# # Call Public Method 
# my_car.start()

# Assignment : 04 => Class Variables and class Methods
# class Bank:
#     bank_name="old bank"
#     @classmethod
#     def changing_bank(cls,new_bank):
#         cls.bank_name=new_bank

# # ✅ Changing a class variable affects all instances.
# b1=Bank()
# b2=Bank()
# Bank.changing_bank("New Bank")
# print(b1.bank_name)
# print(b2.bank_name)


# Assignment : 05 => Static Variables and Static Method
# class MathUtils:
#     @staticmethod #Without this decorater function is work properly but this is not a good practice 
#     def add(a,b):
#         return a + b

# # Call static method directly using class name
# print(MathUtils.add(3,7)) 
        
# Assignment : 06 => Constructor and Destructor
# Constructor (__init__)
# class Laptop:
#     def __init__(self,brand,ram):
#         self.brand_name=brand
#         self.ram=ram
#         print(f"Laptop Created : {self.brand_name} ,{self.ram}GB RAM")

# my_laptop=Laptop("Dell",16)

# # Destructor  (__del__)
# class File:
#     def __init__(self,filename):
#         self.filename=filename
#         print(f"Opening File : {self.filename}")
    
#     def __del__(self): #del is usd
#         print(f"Closing file : {self.filename}")
# my_file=File("Notes.txt")
# del my_file

# Another Example of Constructor and Destructor
# ✅ Constructor runs at object creation. Destructor runs when object is deleted.
# class Logger:
#     def __init__(self):
#         print("Logger Created.")
#     def __del__(self):
#         print("Logger Destroyed")

# log = Logger()
# del log

# Assignment : 07 => Access Modifiers

# class Employee:
#     def __init__(self,name,salary,ssn):
#         self.name=name         #Public variable
#         self._salary=salary    #Protected variable
#         self.__ssn=ssn         #Private variable
# # Best practice to make a function and call this function to access the private variable 
#     def get_ssn(self):
#         return self.__ssn
# emp=Employee("Hassan",50000,"97-804")
# print(f"Employee Name : {emp.name}")
# print(f"Employee Salary : {emp._salary}")
# # Use a Name Mangling for access teh private variable but not a good practice use in case of Debugging/testing
# print(f"Employee snn use Name Mangling : {emp._Employee__ssn}")
# # Call the function
# print(f"Employee snn use function method : {emp.get_ssn()}") # ✅ Safe way to access private variables

# Assignment : 08 => Super () Function

# class Person():
#     def  __init__(self,name):
#         self.name=name
# class Teacher (Person):
#     def __init__(self,name,subject):
#         super().__init__(name)
#         self.subject=subject
#     def location(self):
#         return f"{self.name} teaches {self.subject} in School."
# t1=Teacher("Sara","Math")
# print(t1.location())        

# Assignment : 09 => Abstrct Method 
from abc import ABC,abstractmethod
# Abstrct class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
# Inheriting abstruct class
class Rectangle(Shape):
    def __init__(self,length,witdth):
        self.length=length
        self.width=witdth
    def area(self):  # Implementing abstruct method
        return self.length * self.width

r=Rectangle(5,4)
print("Area of Rectangle : ",r.area())




        
        

         
        
