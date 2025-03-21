import math

def main():
    side_ab : float = float(input("Enter the Length of Side AB "))
    side_ac : float = float(input("Enter the Length of Side BC "))
    
    bc : float = math.sqrt(side_ab**2 + side_ac**2)
    print(f"The length of BC (the hypotenuse) is: {bc:.3f}")
if __name__ == '__main__':
    main()