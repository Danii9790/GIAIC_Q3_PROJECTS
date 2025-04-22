# MARS Weight Solution
# def main():
#     earth_weight:float=float(input("Enter a weight on Earth : "))
#     mars_weight=earth_weight * 0.378
#     mars_weight=round(mars_weight,2)
#     print(f"The equivalent on Mars : {mars_weight}")


# Planets Weights:
def main():
    gravity_factors={
        "mercury": 0.376,
        "venus": 0.889,
        "mars": 0.378,
        "jupiter": 2.36,
        "saturn": 1.081,
        "uranus": 0.815,
        "neptune": 1.14
    }
    earth_weight:float=float(input("Enter a weight on Earth : "))
    planet=input("Enter a planet : ")
    if planet in gravity_factors:
        planet_weight=round(earth_weight * gravity_factors[planet],2)
        print(f"The equivalent weight on {planet} : {planet_weight} ")
    else:
        print("Invalid planet name.")


if __name__=='__main__':
    main()

