mport random

def guessing_game():
    print("Welcome to the Guessing Game!")
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Guess the number (between 1 and 100): "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} correctly in {attempts} attempts!")
            break

def main():
    play_again = 'yes'
    while play_again.lower() == 'yes':
        guessing_game()
        play_again = input("Do you want to play again? (yes/no): ")

    print("Thanks for playing!")

if _name_ == "_main_":
    main()