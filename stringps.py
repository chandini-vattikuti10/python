# Create a new Python script and 
# write a function that takes a string as input, 
# converts it to uppercase, and returns the result.

def string_to_uppercase(str):
    return str.upper()
text="my self chandini"
print(string_to_uppercase(text))

# Write another function that takes a string as input, 
# removes all leading and trailing whitespace characters, 
# and returns the result.

def remove_whitespace(str):
    return str.strip('')
text=' my name is chandini '
print(remove_whitespace(text))


# Develop a function that takes a string as input, 
# checks if it starts with the substring "hello", and 
# returns True if it does, otherwise returns False.

def starts_with_hello(str):
    return str.startswith('hello')
text="hello my name is chandini"
print(starts_with_hello(text))