# fill out the add_three_copies(...) function which takes a list and some data and then adds three copies of the data to the list. 
def add_three_copies(myList,data):
    for i in range(3):
        myList.append(data)

def main():
    message:str=input("Enter a message to copy : ")
    myList:list=[]
    print(f"List before : {myList}")
    add_three_copies(myList,message)
    print(f"List After : {myList}")

if __name__=='__main__':
    main()
