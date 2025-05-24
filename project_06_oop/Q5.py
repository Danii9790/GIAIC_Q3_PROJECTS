# Assignment : 05 => Static Variables and Static Method
class MathUtils:
    @staticmethod #Without this decorater function is work properly but this is not a good practice 
    def add(a,b):
        return a + b

# Call static method directly using class name
print(MathUtils.add(3,7)) 