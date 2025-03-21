import random

def main():
    random_number = random.randint(1, 100)
    
    print("I am thinking of a number between 1 and 100...")
    
    while True:
        user_input = input("Enter a number (or type 'hint' for a clue or 'c' to exist): ")
        
        if user_input.lower() == "c":
            print("Goodbye!")
            break

        if user_input.lower() == "hint":
            print(f"Hint: The number is {random_number}")
            continue
        
        try:
            guess = int(user_input)
        except ValueError:
            print("Please enter a valid number or 'hint'.")
            continue
        
        if guess < random_number:
            print("Your guess is too low.")
        elif guess > random_number:
            print("Your guess is too high.")
        else:
            print(f"Congrats! The number was: {random_number}")
            break

if __name__ == "__main__":
    main()
