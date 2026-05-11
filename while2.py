# Write a while loop that prints the numbers from 1 to 10, incrementing by 1 each time.
# s=1
# while s<=10:
#     print(s)
#     s+=1

# Create a while loop that asks the user for input 
# until they enter a specific word (e.g., "exit"), at which point the loop ends.

# while True:
#     word = input("Enter a word (type 'exit' to stop): ")

#     if word == "exit":
#         print("Loop ended.")
#         break

#     print("You entered:", word)

# Develop a simple guessing game where the user has to 
# guess a randomly generated number between 1 and 100, 
# using a while loop to repeatedly ask for guesses until the correct number is guessed.

import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

print("Welcome to the Guessing Game!")
print("Guess a number between 1 and 100")

guess = 0

# Continue looping until the correct guess
while guess != secret_number:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too low! Try again.")

    elif guess > secret_number:
        print("Too high! Try again.")

    else:
        print("Congratulations! You guessed the correct number.")