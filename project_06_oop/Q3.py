# Assignment : 03 => Public Variables and Method

class Car:
    def __init__(self,brand):
        self.brand=brand  #Public variable 

    def start(self):  #Public Method
        print(f"{self.brand} car is starting...")
# Create Object
my_car=Car("Toyata")
# Access Public variable
print(my_car.brand)
# Call Public Method 
my_car.start()