# Assignment : 06 => Constructor and Destructor
# Constructor (__init__)
class Laptop:
    def __init__(self,brand,ram):
        self.brand_name=brand
        self.ram=ram
        print(f"Laptop Created : {self.brand_name} ,{self.ram}GB RAM")

my_laptop=Laptop("Dell",16)

# Destructor  (__del__)
class File:
    def __init__(self,filename):
        self.filename=filename
        print(f"Opening File : {self.filename}")
    
    def __del__(self): #del is usd
        print(f"Closing file : {self.filename}")
my_file=File("Notes.txt")
del my_file

# Another Example of Constructor and Destructor
# ✅ Constructor runs at object creation. Destructor runs when object is deleted.
class Logger:
    def __init__(self):
        print("Logger Created.")
    def __del__(self):
        print("Logger Destroyed")

log = Logger()
del log