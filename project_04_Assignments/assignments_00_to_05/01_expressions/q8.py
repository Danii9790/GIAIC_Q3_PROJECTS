# Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!

SENTENCE="Code in Place is fun. I learned to program and used Python to make my"
def main():
    adjective:str=input("Enter a type adjective : ")
    noun:str=input("Enter a type noun : ")
    verb:str=input("Enter a type verb : ")

    print(f"{SENTENCE} {adjective} {noun} {verb}")
if __name__=='__main__':
    main()
