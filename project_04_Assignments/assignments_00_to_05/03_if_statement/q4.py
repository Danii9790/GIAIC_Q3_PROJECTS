# Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.
"""
In amusement parks (ah, the good old pre-pandemic days...), rollercoasters frequently have 
minimum height requirements for safety reasons. Assume for now that the minimum height is 50
"""

MINIMUM_HEIGHT:int=50

def main():
    user:int=int(input("Enter your Height : "))
    if user >=MINIMUM_HEIGHT:
        print(f"Age : {user} \nYou're tall enough to ride!")
    else:
        print(f"Age : {user} \nYou're not tall enough to ride, but maybe next year!")

if __name__=='__main__':
    main()