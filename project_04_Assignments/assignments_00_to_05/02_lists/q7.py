# Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.

def main():
    empty_list:list=[]

    val:str=input("Enter a value : ")
    while val:
        empty_list.append(val)
        val:str=input("Enter a value : ")
    print(f"Here's the list : {empty_list}")

if __name__=='__main__':
    main()