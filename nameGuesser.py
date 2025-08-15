import random
import time

print("\n-- NUMBER GUESSER --\n")
print("This is a console program where you guess a number generated randomly.")
print("Choose the difficulty range:\n")
print("1 → 1 to 10")
print("2 → 1 to 50")
print("3 → 1 to 100")
print("4 → 1 to 1000\n")

# Ask for difficulty choice
userChoice = int(input("Enter your choice (1-4): "))

# Decide the range based on user choice
if userChoice == 1:
    secret_number = random.randint(1, 10)
    max_range = 10
elif userChoice == 2:
    secret_number = random.randint(1, 50)
    max_range = 50
elif userChoice == 3:
    secret_number = random.randint(1, 100)
    max_range = 100
elif userChoice == 4:
    secret_number = random.randint(1, 1000)
    max_range = 1000
else:
    print("Invalid choice! Defaulting to 1-10.")
    secret_number = random.randint(1, 10)
    max_range = 10

# Guessing loop
print(f"\nI have chosen a number between 1 and {max_range}. Try to guess it!")

while True:
    guess = int(input("Your guess: "))
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"🎉 Correct! The number was {secret_number}. You win!")
        print("Closing..")
        break
