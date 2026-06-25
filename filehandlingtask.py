'''1. Create a Python program that writes a list of numbers to a text file named "numbers.txt".'''

# numbers = [10, 20, 30, 40, 50]

# with open("numbers.txt", "w") as file:
#     for num in numbers:
#         file.write(str(num) + "\n")

# print("Numbers written to numbers.txt successfully.")

'''2. Develop a function to read the contents of the "numbers.txt" file and calculate the sum of all numbers in the file.'''

# def calculate_sum():
#     total = 0

#     with open("numbers.txt", "r") as file:
#         for line in file:
#             total += int(line.strip())

#     return total

# print("Sum of numbers =", calculate_sum())


'''3. Write a program that copies the contents of the "numbers.txt" file to a new file named "numbers_copy.txt".'''

# with open("numbers.txt", "r") as source:
#     content = source.read()

# with open("numbers_copy.txt", "w") as destination:
#     destination.write(content)

# print("Contents copied successfully to numbers_copy.txt.")