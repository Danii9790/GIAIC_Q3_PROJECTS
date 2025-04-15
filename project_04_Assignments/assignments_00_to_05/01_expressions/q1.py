"""
Program: dicesimulator
----------------------
Simulate rolling two dice, three times.  Prints
the results of each die roll.  This program is used
to show how variable scope works.
"""
import random

def roll_dice():
    die1=random.randint(1,6)
    die2=random.randint(1,6)
    print(f"Rolled Dice : Die 1 = {die1} , Die 2 = {die2}")

def main():
    for i in range(3):
        print(f"Roll : {i + 1}") #(i + 1) 1 is added because the counting start with 1 default counting is 0.
        roll_dice()

if __name__=='__main__':
    main()