# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:
def main():
    num1:int=int(input("Enter your first number : "))
    num2:int=int(input("Enter your Second number : "))
    sum=num1+num2
    print(f"the sum of {num1} and {num2} is {sum}.")
if __name__=='__main__':
    main()