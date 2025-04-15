# Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also __ ?
# (the blank should be filled in with the user-inputted animal, of course).

def main():
    user=input("Enter your favorite animal name : ")
    print(f"My favorite animal name is {user}.")
    print(f"My favorite animal is also {user}.")

if __name__=='__main__':
    main()