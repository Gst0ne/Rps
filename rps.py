import random
from typing import List

allowed: List[str] = ["rock", "paper", "scissors"]


def main():
    user_wins: int = 0
    computer_wins: int = 0

    def rock(user):
        if user == "rock":
            return "tie"
        elif user == "paper":
            return "win"
        else:
            return "lose"

    def paper(user):
        if user == "paper":
            return "tie"
        elif user == "scissors":
            return "win"
        else:
            return "lose"

    def scissors(user):
        if user == "scissors":
            return "tie"
        elif user == "rock":
            return "win"
        else:
            return "lose"

    while True:
        user_input = input("Enter your input:\n")   #Gets Input from the user
        if user_input not in allowed:
            print(
                f"Invalid Input!\nYour input must be one of these: {', '.join(allowed)}")
            continue

        computer_value = random.choice((rock, paper, scissors))
        print(
            f"The computer generated value was '{computer_value.__name__.capitalize()}'.")

        if computer_value(user_input) == "win":
            user_wins += 1
            print(f"You have {user_wins} win{'s' if user_wins > 1 else ''}.")
        elif computer_value(user_input) == "lose":
            computer_wins += 1
            print(
                f"Computer has {computer_wins} win{'s' if computer_wins > 1 else ''}")
        else:
            print("It's a tie.")
        if user_wins + computer_wins == 5:
            winner: str = "Computer wins." if computer_wins > user_wins else "Congrats! User wins."
            print(winner)
            break         # Game Ends


if __name__ == "__main__":
    main()
