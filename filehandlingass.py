'''1. Create a Python program that writes user input to a file named user_input.txt, 
allowing the user to save their input by typing "SAVE" and exit the program by typing "EXIT".'''


# lines = []

# while True:
#     text = input("Enter text (SAVE to save, EXIT to quit): ")

#     if text.upper() == "SAVE":
#         with open("user_input.txt", "w") as file:
#             for line in lines:
#                 file.write(line + "\n")
#         print("Data saved successfully.")

#     elif text.upper() == "EXIT":
#         print("Program exited.")
#         break

#     else:
#         lines.append(text)

'''2. Develop a function that reads the contents of a file named example.txt and counts the occurrences of each word, 
printing out the word frequencies.'''

# def word_frequency():
#     with open("example.txt", "r") as file:
#         text = file.read().lower()

#     words = text.split()

#     frequency = {}

#     for word in words:
#         frequency[word] = frequency.get(word, 0) + 1

#     print("Word Frequencies:")
#     for word, count in frequency.items():
#         print(word, ":", count)

# word_frequency()

'''3. Write a script that creates a backup of a specified file by appending "_backup" to the original filename, 
copying the original file's content into the new backup file, and then modifies the first line of the original file 
to include the timestamp of when the backup was created.'''

# import os
# from datetime import datetime

# filename = input("Enter the filename: ")

# name, extension = os.path.splitext(filename)
# backup_file = name + "_backup" + extension

# with open(filename, "r") as source:
#     content = source.read()

# with open(backup_file, "w") as destination:
#     destination.write(content)

# timestamp = "Backup created on: " + str(datetime.now()) + "\n"

# with open(filename, "r") as file:
#     original_content = file.readlines()

# with open(filename, "w") as file:
#     file.write(timestamp)
#     file.writelines(original_content)

# print("Backup created successfully.")
# print("Backup File:", backup_file)
