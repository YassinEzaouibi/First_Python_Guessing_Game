import random

# Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)
guessed_correctly = False
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while not guessed_correctly:
    try:
        user_guess = int(input("Guess a number: "))
        attempts += 1

        if user_guess == number_to_guess:
            print(f"Congratulations! You guessed it right in {attempts} attempts!")
            guessed_correctly = True
        elif user_guess < number_to_guess:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    except ValueError:
        print("Invalid input! Please enter a number.")
