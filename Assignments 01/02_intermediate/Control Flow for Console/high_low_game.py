import random

NUM_ROUNDS = 5

def high_low_game():
    
    print("--------------------------------")
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    score = 0

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")

        user_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        print(f"Your number is {user_number}")

        while True:
            user_guess = input("Do you think your number is higher or lower than the computer's? (h/l): ").strip().lower()
            if user_guess in ["h", "l"]:
                break
            print("Invalid input. Please enter 'h' for higher or 'l' for lower.")

        if (user_guess == "h" and user_number > computer_number) or \
           (user_guess == "l" and user_number < computer_number):
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")


        print("--------------------------------")  
        print(f"Your score is now {score}")
        print("--------------------------------")  

    print("Thanks for playing!")
    if score == NUM_ROUNDS:
        print("Congratulations! You WON!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job! You did well.")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    high_low_game()