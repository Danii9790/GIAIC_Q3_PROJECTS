# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

def get_user_numbers():
    user_numbers = []
    while True:
        user_input = input("Enter a number (press Enter to stop): ")
        if user_input == "":
            break

        # Convert the user input to an integer and add it to the list
        num = int(user_input)
        user_numbers.append(num)
    return user_numbers

def count_nums(num_1st):
    num_dict: dict = {}
    for num in num_1st:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    return num_dict

def print_counts(num_dict):
    for num in num_dict:
        print(f"{num} appears {num_dict[num]} times.")

def main():
    user_number = get_user_numbers()
    num_dict = count_nums(user_number)
    print_counts(num_dict)  # you were printing the dict raw before

if __name__ == '__main__':
    main()

