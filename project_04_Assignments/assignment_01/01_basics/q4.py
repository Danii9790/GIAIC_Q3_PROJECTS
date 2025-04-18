# Guess My Number
import random
def main():
    print("Guess My Number")
    print("I am thinking of a number between 1 and 99.")
    user_input:int=int(input("Enter a number : "))
    numbers=random.randint(1,99)
    while user_input !=numbers:
        if user_input < numbers:
            print("Your guess is too low.")
        else:
            print("Your guess is too high")
        print()
        user_input:int=int(input("Enter a new guessing number."))
    print(f"the number is {user_input} your guess is correct. ")
if __name__=='__main__':
    main()
    
