# Two numbers are generated from 1 to 100 (inclusive on both ends): one for you and one for a computer, who will be your opponent. You can see your number, but not the computer's!
# You make a guess, saying your number is either higher than or lower than the computer's number
import random
NUM_ROUNDS=5
def main():
    print("Welcome to the High-Low Game!")
    print("------------------------------")

    score=0

    # paly multiple rounds
    for i in range(NUM_ROUNDS):
        print(f"Rounds: {i+1}")
        computer_number=random.randint(1,100)
        my_num=random.randint(1,100)
        print(f"Your number is {my_num}.")
        # choise
        choise=input("Do you think your number is higher or lower than the computer's?: ")
        while choise!="higher" and choise!="lower":
            choise=input("Please enter either higher or lower: ")

        higher_and_correct =choise=="higher"and my_num>computer_number
        lower_and_correct=choise=="lower"and my_num<computer_number

        if higher_and_correct or lower_and_correct :
            print(f"you are right ! the computer number was : {computer_number}.")
            score+=1
        else:
            print(f"Aww,that's incorrect.the computer's number was : {computer_number}")
        
        print(f"your score is : {score}")
        print()

    print(f"Your final score is : {score}")

    if score == NUM_ROUNDS:
        print("Wow! you are playing perfectly")
    elif score >NUM_ROUNDS : #2
        print("Good job ! you are played well.")
    else:
        print("Better luck next time.")
if __name__=='__main__':
    main()
