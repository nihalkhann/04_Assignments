
c: int = 299792458  #? The speed of light in m/s


def main():
    mass_in_kg:float = float(input("Enter Kilos of Mass: "))

    energy_in_joules:float = mass_in_kg * (c ** 2)

    print("e = m * C^2...")
    print(f"m = {mass_in_kg}kg")
    print(f"C = {c} m/s")
    print(f"Energy in Joules = {energy_in_joules} J")

if __name__ == '__main__':
    main()
    
