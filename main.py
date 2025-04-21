import random

number = random.randint(1, 10)
guess = None
attempts = 0

print("Guess the number between 1 and 10")

while guess != number:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
    except ValueError:
        print("Please enter a valid number.")
