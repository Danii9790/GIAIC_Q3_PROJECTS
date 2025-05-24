# Assignment : 07 => Access Modifiers

class Employee:
    def __init__(self,name,salary,ssn):
        self.name=name         #Public variable
        self._salary=salary    #Protected variable
        self.__ssn=ssn         #Private variable
# Best practice to make a function and call this function to access the private variable 
    def get_ssn(self):
        return self.__ssn
emp=Employee("Hassan",50000,"800Usdt")
print(f"Employee Name : {emp.name}")
print(f"Employee Salary : {emp._salary}")
# Use a Name Mangling for access the private variable but not a good practice use in case of Debugging/testing
print(f"Employee snn use Name Mangling : {emp._Employee__ssn}")
# Call the function
print(f"Employee snn use function method : {emp.get_ssn()}") # ✅ Safe way to access private variables
