# Assignment : 09 => Abstrct Method 
# from abc import ABC,abstractmethod
# # Abstrct class
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# # Inheriting abstruct class
# class Rectangle(Shape):
#     def __init__(self,length,witdth):
#         self.length=length
#         self.width=witdth
#     def area(self):  # Implementing abstruct method if the name of function is different to abstract method then Error occurs because abstrct class area if defined use area is permenant.
#         return self.length * self.width

# r=Rectangle(5,4)
# print("Area of Rectangle : ",r.area())

# Practice Again

from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.width * self.length
    
result=Rectangle(5,6)
print("Area of Rectangle : ",result.area())



        


         
        
