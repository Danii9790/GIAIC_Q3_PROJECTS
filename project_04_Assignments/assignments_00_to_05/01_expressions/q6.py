# Simulate rolling two dice, and prints results of each roll as well as the total.
import random
def rolling_dice():
    die1:int=random.randint(1,6)
    die2:int=random.randint(1,6)
    total=die1+die2
    print(f"First Die : {die1}")
    print(f"Second Die : {die2}")
    print(f"Total : {total}")
    
def main():
    

    for i in range(2):
        print(f"Rolling die {i +1}")
        rolling_dice()

if __name__=='__main__':
    main()
