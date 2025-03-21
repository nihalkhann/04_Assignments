GRAVITY_MULTIPLIERS  = {
    'mercury': 0.376,
    'venus': 0.889,
    'earth': 1.0,
    'mars': 0.378,
    'jupiter': 2.36,
    'saturn': 1.081,
    'uranus': 0.815,
    'neptune': 1.14, 
}

def calculate_weight(earth_weight,planet): 
    gravity_multiplier =  GRAVITY_MULTIPLIERS.get(planet.lower())

    if gravity_multiplier is None:
        raise ValueError(f"Invalid planet Name {planet}")
    
    planetary_weight = earth_weight * gravity_multiplier
    return round(planetary_weight,2)


def main():
    try:
        print("------------------------------------------------")
        earth_weight = float(input("Enter your weight on Earth (in kg): "))
        if earth_weight <= 0:
            raise ValueError("Weight must be a positive number")
        
        planet = input("Enter the name of a planet:  ").strip()

        planets_weight = calculate_weight(earth_weight, planet)

        print(f"Your weight on {planet.capitalize()} would be: {planets_weight} kg")
   
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
