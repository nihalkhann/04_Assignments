import random

Num_Sides = 6

def roll_dice():
    die1 :int = random.randint(1, Num_Sides)
    die2 :int = random.randint(1, Num_Sides)
    total :int = die1 + die2

    print(f"Total of two dice is {total}!!!")
def main():
    die1:int = 10
    print(f"die1 is main() Starts as :{die1}")
    roll_dice()
    roll_dice()
    roll_dice()
    print(f"die1 is main() Starts as :{die1}")

if __name__ == "__main__":
    main()
    