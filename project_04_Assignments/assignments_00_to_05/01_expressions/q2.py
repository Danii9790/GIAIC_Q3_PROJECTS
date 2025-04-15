# Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:
# E = m * c**2 and speed of light -- C = 299792458 m/s.

C:int=29979 # Speed of light
def main():
    mass_in_kg:float=float(input("Enter a mass in kg : "))
    energy_in_joule:float=mass_in_kg*(C**2)

    # Display the result
    print(f"Kg mass is {mass_in_kg} kg = Engry {energy_in_joule} Joule of energy! ")

if __name__=='__main__':
    main() 
