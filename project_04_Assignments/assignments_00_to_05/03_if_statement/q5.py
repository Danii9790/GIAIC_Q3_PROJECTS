# Print 10 random numbers in the range 1 to 100.
import random
def main():
    for _ in range(1,10):
        numbers=random.randint(1,100)
        
        print(numbers)

if __name__=='__main__':
    main()