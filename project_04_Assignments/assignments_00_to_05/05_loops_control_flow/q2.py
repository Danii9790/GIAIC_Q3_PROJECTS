# Write a program to print terms in the Fibonacci sequence up to a maximum value.
# Write a program that displays the terms in the Fibonacci sequence, starting with Fib(0) and continuing as long as the terms are less than 10,000 (you should store this value as a constant!).
MAX_VALUE:int=10000
def main():
    current_term=0
    next_term=1
    while current_term<=MAX_VALUE:
        print(current_term)
        term_after_next=current_term+next_term
        current_term=next_term
        next_term=term_after_next

if __name__=='__main__':
    main()