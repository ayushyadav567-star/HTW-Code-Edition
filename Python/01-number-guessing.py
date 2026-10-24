"""Guess the secret number in three attempts."""

secret_number = 7
attempts_allowed = 3

print("Guess the secret number from 1 to 10.")

for attempt in range(1, attempts_allowed):
    guess = int(input(f"Attempt {attempt}/{attempts_allowed}: "))

    if guess == secret_number:
        print("Correct! You guessed the number.")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
else:
    print(f"Out of attempts! The number was {secret_number}.")
