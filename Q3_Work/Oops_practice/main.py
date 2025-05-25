# Practice Again Ooops 
# Use (Self)

# class Person:
#     def __init__(self,name):

#         self.name = name #Public attributwe, Instance Variable
#         self.state = "Idle"
#     def running(self):
#         self.state = "Running"
#         print(f"{self.name} is now Running.")
#     def walking(self):
#         self.state = "Walking"
#         print(f"{self.state} is now Walking.")
#     def sleeping(self):
#         self.state = "Sleeping"
#         print(f"{self.state} is now sleeping.")
#     def show_state(self):
#         print(f"{self.name} is currently in {self.state} state.")

# person1 = Person("Ali")
# person1.show_state()

# person1.running()
# person1.show_state()

# person1.walking()
# person1.show_state()

# person1.sleeping()
# person1.show_state()


# Use Constructor 
# class Person:
#     def __init__(self,name,age,address):
#         self.name = name
#         self.age = age
#         self.address = address
#     def show_detail(self):
#         print(f"Name {self.name} ,Age : {self.age} , Address : {self.address}.")

# p1=Person("Daniyal",21,"Golimar Nawabshah,Sindh")
# p1.show_detail()

# # Use Destructor
# class Car:
    
#     def __init__(self,model,brand):
#         self.model = model
#         self.brand = brand

#     def __del__(self):
#         print(f"The {self.model} ,{self.brand} car is destroyed.")

# c1 = Car(2022,"Civic")  
# # Print statment run if the (del c1) is not initilize or pass
# del c1


# Access Modifiers:
# Protected
class Father:
    def __init__(self):
        self._secret_location = "Under the old oak tree"  # Protected attribute

    def _where_i_hide_the_gold(self):
        print(f"The Money is place at : {self._secret_location}.")
class Son(Father): #  Inheritance
    pass
son=Son()
son._where_i_hide_the_gold()

# Not recommended but still accessible 
class Relatives:
    def __init__(self):
        self.father = Father()
    def try_access_secret(self):
        # Both are Technically work but discouraged
        print(self.father._secret_location)
        print(self.father._where_i_hide_the_gold()) 
print("-----Relatives access----")        
realtive=Relatives()
realtive.try_access_secret()
