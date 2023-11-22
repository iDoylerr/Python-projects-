import random

# Function to get user's choice
def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return get_user_choice()  # Retry getting user's choice
    return user_choice

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    if (
        (user_choice == 'rock: and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Main game loop
while True:
    # Get user's choice
    user_choice = get_user_choice()

    # Computer's choice is always "scissors"
    computer_choice = "scissors"

    # Display user and computer choices
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    result = determine_winner(user_choice, computer_choice)
    print(result)

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != 'yes':
        break
