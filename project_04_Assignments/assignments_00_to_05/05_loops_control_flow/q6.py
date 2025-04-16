# Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.

def main():
    while True:
        user_input:int=int(input("Enter a number : "))
        num=user_input *2
        print(f"Double value : {num}")

        if num>=100:
            break

if __name__=='__main__':
    main()