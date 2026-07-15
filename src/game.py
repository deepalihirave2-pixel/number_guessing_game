import random

def play_game():
    print("=========================================")
    print("       WELCOME TO THE GUESSING GAME!     ")
    print("=========================================")
    print("I have selected a random number between 1 and 100.\n")

    # Generate the secret number
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            # Get user input
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Check the guess against the secret number
            if guess < secret_number:
                print("Too low! Try again. 👇")
            elif guess > secret_number:
                print("Too high! Try again. 👆")
            else:
                print("\n🎉 CONGRATULATIONS! 🎉")
                print(f"You guessed the correct number ({secret_number}) in {attempts} attempts!")
                break
        except ValueError:
            print("Invalid input! Please enter a valid whole number.")