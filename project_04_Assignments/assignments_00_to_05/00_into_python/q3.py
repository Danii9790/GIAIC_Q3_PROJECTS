# Write a program which prompts the user for a temperature in Fahrenheit and convert in Celsius.
def main():
    fahrenheit:float=float(input("Enter a temperature in fahrenheit : "))
    celsius=(fahrenheit - 32)*5/9
    print(f"\nTemperature : {fahrenheit} F = {celsius:.2f}C")

if __name__=='__main__':
    main()

