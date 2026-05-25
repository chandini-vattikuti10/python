# Create a Python function that takes a string as input 
# and returns the string with all vowels removed. 
# Use the replace() method or a list comprehension to achieve
# this.

def remove_vowels(str):
    vowels='aeiouAEIOU'
    result=''.join([x for x in str if x not in vowels])
    return result
text=input("enter string:")
print(remove_vowels(text))

# Write a Python program that prompts the user to enter their full name and then prints out a greeting message with the name capitalized using the upper() or title() method.
def greet(name):
    res=name.upper()
    return res
text=input("enter your name: ")
print(greet(text)+ " "+ "Welcome")

full_name = input("Enter your full name: ")
print("Hello,", full_name.title() + "! Welcome!")

# Develop a simple Python script that takes a sentence as input, splits it into words using the split() method, and then prints out each word on a new line, along with its length calculated using the len() function.
sentence = input("Enter a sentence: ")
words = sentence.split()
for word in words:
    print(word, "-", len(word))