import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Rolling Simulator!")
    while True:
        input("Press Enter to roll the dice...")
        result = roll_dice()
        print("You rolled:", result)
        play_again = input("Roll again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if _name_ == "_main_":
    main()