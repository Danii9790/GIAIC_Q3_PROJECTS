# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

def main():
    num1:int=int(input("Enter a num1 : "))
    num2:int=int(input("Enter a num2 : "))
    division=num1/num2
    remainder=num1%num2
    print(f"Division of Numbers is : {division}")
    print(f"Remainder of Numbers is : {remainder}")
if __name__=='__main__':
    main()
