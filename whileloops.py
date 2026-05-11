# Implement a while loop to print numbers from 1 to 10, incrementing by 1 each time.

import random
s = 1
while s <= 10:
    print(s)
    s += 1

# Write a while loop to calculate the factorial of a given number, using a conditional statement to terminate the loop when the calculation is complete.

num = int(input())
fact = 1
i = 1
while i <= num:
    fact *= i
    i += 1
print('factorial', fact)

# Create a simple guessing game using a while loop, where the user
# has to guess a randomly generated number between 1 and 100,
# with hints provided after each guess until the correct number is guessed.


# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

guess = None

print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Keep looping until the user guesses correctly
while guess != secret_number:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("🎉 Congratulations! You guessed the correct number!")
