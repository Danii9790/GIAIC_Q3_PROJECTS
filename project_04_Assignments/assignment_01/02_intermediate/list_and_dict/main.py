# def main():
#     fruit_list=['apple', 'banana', 'orange', 'grape', 'pineapple']
#     length_of_list=len(fruit_list)
#     print(length_of_list)
#     fruit_list.append('mango')
#     print(fruit_list)

List:list=['apple',5,'mango',3.99,True]
def access_elements(lst,index):
    try:
        return f"Element at index {index} : {lst[index]}"
    except IndexError:
        return "Error: Index out of range"
# Function to modify the element:
def modify_element(lst,index,new_value):
    try:
        old_value=lst[index]
        lst[index]=new_value
        return f"Replaced '{old_value}'  with '{new_value}' at index {index}"
    except IndexError:
        return "Error: Index out of range."

def slice_list(lst,start,end):
    try:
        sliced=lst[start:end]
        return f"Sliced list : {sliced}"
    except IndexError:
        return "Error: Index out of range"

def main():
    while True:
        print("\nCurrent List:", List)
        print("\nChoose an operation:")
        print("1. Access element")
        print("2. Modify element")
        print("3. Slice list")
        print("4. Quit") 
        choise:int=int(input("Enter your Choise (1-4): "))
        if choise == 1:
            index=int(input("Enter index to access : "))
            print(access_elements(List,index))
        elif choise == 2:
            index=int(input("Enter index to modify : "))
            new_val=input("Enter new value : ")
            print(modify_element(List,index,new_val))
        elif choise == 3:
            start=int(input("Enter start index : "))
            end=int(input("Enter end index : "))
            print(slice_list(List,start,end))
        elif choise == 4:
            print("Thanks for playing the Index game.")
            break
        else:
            print("Invalid choise.please try again.")
        



if __name__=='__main__':
    main()