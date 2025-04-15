"""Ask the user for a number and print its square (the product of the number times itself).

Here's a sample run of the program (user input is in bold italics):"""
def main():
    user:int=int(input("Enter a number : "))
    square=user*user
    print(f"Square of {user} is {square}")

if __name__=='__main__':
    main()