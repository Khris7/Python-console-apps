import random

def get_user_choice():
    choice = input("Choose Rock, Paper, or Scissors: ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        choice = input("Invalid choice. Please choose Rock, Paper, or Scissors: ").lower()
    return choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"

def play_game():
    print(" Welcome to Rock, Paper, Scissors!")
    user_wins = 0
    computer_wins = 0
    round_number = 1

    while round_number <= 3:
        print(f"\n--- Round {round_number} ---")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice.capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}")

        result = determine_winner(user_choice, computer_choice)

        if result == "user":
            print(" You win this round!")
            user_wins += 1
        elif result == "computer":
            print(" Computer wins this round!")
            computer_wins += 1
        else:
            print(" It's a tie!")

        
        if user_wins == 2:
            print("\n You won the game!")
            return
        elif computer_wins == 2:
            print("\n Computer won the game!")
            return

        round_number += 1

    print("\n Game Over!")
    if user_wins > computer_wins:
        print(" You won the game!")
    elif computer_wins > user_wins:
        print(" Computer won the game!")
    else:
        print(" It's a tie!")

if __name__ == "__main__":
    play_game()
    
