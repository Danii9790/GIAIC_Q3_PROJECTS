# Write a function that takes a list of numbers and returns the sum of those numbers.
def add_numbers(numbers)->int:
    total:int=0
    for number in numbers:
        total +=number
    return total
def main():
    numbers:list[int]=[1,2,3,4,5]
    sum_of_numbers=add_numbers(numbers)

    print(sum_of_numbers)

if __name__=='__main__':
    main()