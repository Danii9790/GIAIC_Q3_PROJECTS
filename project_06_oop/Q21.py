"""
Assignment:
Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.

"""

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self): # jo iterable object banata hai.
        return self

    def __next__(self): # (__next__) next number return krta hn 
        if self.current < 0:
            raise StopIteration  # is used if number is less than 0
        value = self.current
        self.current -= 1
        return value

for i in Countdown(3):
    print(i)

