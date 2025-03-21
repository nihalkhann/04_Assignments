import random

dice_sides = 6

def main():
    die1 :int = random.randint(1, dice_sides)
    die2 :int = random.randint(1, dice_sides)
    
    total :int = die1 + die2


    
    print(f"Dice have {dice_sides} sides each.")
    print(f"First die {die1}")
    print(f"Second die {die2}")
    print(f"Total of the two dice is {total}")

if __name__ == '__main__':
    main()