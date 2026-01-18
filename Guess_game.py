import random
secret_number = random.randint(1, 10)
chances = 3
print("Welcome to the Guessing Game!")
print("I have chosen a number between 1 and 10.")
print("You have 3 chances to guess it.\n")

for attempt in range(1, chances + 1):
    guess = int(input(f"Attempt {attempt}: Enter your guess: "))

    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

    if attempt == chances:
        print("Sorry! You've used all your chances.")
        print(f"The correct number was: {secret_number}")
