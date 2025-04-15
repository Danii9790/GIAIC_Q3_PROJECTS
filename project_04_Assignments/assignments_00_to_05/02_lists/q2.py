# Write a program that doubles each element in a list of numbers. For example, if you start with this list:
def main():
    numbers:list[int]=[1,2,3,4,5]
    for i in range(len(numbers)):
        index_of_numbers=numbers[i]
        numbers[i]=index_of_numbers*2
    print(numbers)
if __name__=='__main__':
    main()