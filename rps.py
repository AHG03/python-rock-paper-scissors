import random

choices = ["r", "p", "s"]
emojis = {"r":"💎", "p":"📃", "s":"✂"}

def get_user_choice():
    while True:
        user_choice = input("Rock, Paper or Scissor? (r/p/s): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice")

while True:
    user_choice = get_user_choice()

    computer_choice = random.choice(choices)

    print(f"you chose {emojis[user_choice]}")
    print(f"computer chose {emojis[computer_choice]}")

    if user_choice == computer_choice:
        print("Draw")
    elif (
        (user_choice == "r" and computer_choice == "s") or
        (user_choice == "s" and computer_choice == "p") or
        (user_choice == "p" and computer_choice == "r")):
        print("you win")
    else:
        print("you lose")

    should_continue = input("Continue? (y/n): ").lower()
    if should_continue == "n":
        break