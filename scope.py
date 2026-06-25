'''1. Create a Python program that reads from a file named input.txt and writes the contents to a new file named output.txt.'''

# with open("input.txt", "r") as infile:
#     content = infile.read()

# with open("output.txt", "w") as outfile:
#     outfile.write(content)

# print("Contents copied successfully from input.txt to output.txt.")

'''2. Write a Python function that demonstrates the difference between local and global scopes by declaring a variable inside 
and outside the function.'''

# Global variable
# x = 100

# def display():
#     # Local variable
#     x = 50

#     print("Local Variable:", x)

# display()

# print("Global Variable:", x)


'''3. Create a Python program that uses a loop to write the numbers 1 to 10 to a file named numbers.txt, 
then reads from the file and prints the numbers to the console.'''


# with open("numbers.txt", "w") as file:
#     for i in range(1, 11):
#         file.write(str(i) + "\n")

# print("Numbers in the file:")

# with open("numbers.txt", "r") as file:
#     for line in file:
#         print(line.strip())