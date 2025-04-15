# There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits were available and how much one of each fruit costs.

def main():
    fruits:dict={"apple":400,"mango":300,"banana":150,"watermelon":200}
    total_cost=0
    for fruits_name in fruits:
        price=fruits[fruits_name]
        buy_quantity=int(input(f"How many {fruits_name} you want to buy? "))
        total_cost+=(price*buy_quantity)

    print(f"Your total is {total_cost} .")
if __name__=='__main__':
    main()