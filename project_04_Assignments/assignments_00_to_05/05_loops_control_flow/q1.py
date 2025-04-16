import random
def main():
    print("Guess My Number ")
    number=random.randint(1,99)
    print("I am thinking of a number between 1 and 99.")
    user_input:int=int(input("Enter a Guess number : "))
    while user_input !=number:

        if user_input<number:
            print("Your guess is to low.")
        else:
            print("Your guess is to high.")
        print()
        user_input:int=int(input("Enter a new Guess number : "))
    print(f"Congrats! the number was : {user_input}")
if __name__=='__main__':
    main()