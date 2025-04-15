# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.
INCHES_PER_FEET=12

def main():
    feet:float=float(input("Enter a number of Feet :  "))
    inches=feet*INCHES_PER_FEET
    print(f"{feet} Feets is eqaual to {inches} Inches")

if __name__=='__main__':
    main()