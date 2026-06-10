'''1. Square of Numbers
Create a dictionary of numbers and their squares from 1 to 5
Expected Output:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}'''
# d={x:x**2 for x in range(1,5)}
# print(d)

'''2. Filter Even Numbers
Create a dictionary with numbers 1 to 10 as keys and their squares as values, but only for even numbers
Expected Output:
{2: 4, 4: 16, 6: 36, 8: 64, 10: 100}'''
# d={x:x**2 for x in range(1,11) if x%2==0}
# print(d)

'''3. Character Count from String
Given a string "success", create a dictionary of each character and its frequency
Expected Output:
{'s': 3, 'u': 1, 'c': 2, 'e': 1}'''
# s='success'
# d={x:s.count(x) for x in s}
# print(d)

'''4. Create Dictionary from Two Lists
Given two lists:
keys = ['a', 'b', 'c']
values = [1, 2, 3]
Create a dictionary using comprehension
Expected Output:
{'a': 1, 'b': 2, 'c': 3}'''
# keys=['a','b','c']
# values=[1,2,3]
# d={x:y for x,y in zip(keys,values)}
# print(d)

'''5. Invert Keys and Values
Given dictionary:
d = {'x': 10, 'y': 20, 'z': 30}
Create a new dictionary where keys and values are swapped
Expected Output:
{10: 'x', 20: 'y', 30: 'z'}'''
# d = {'x': 10, 'y': 20, 'z': 30}
# r={y:x for x,y in d.items()}
# print(r)

'''6. Conditional Dictionary with Squares > 10
Create a dictionary of numbers 1 to 10 with their squares, but include only those where the square is greater than 10
Expected Output:
{4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}'''
# d={x:x**2 for x in range(1,10) if x**2>10}
# print(d)

'''7. Uppercase Keys
Given list:
letters = ['a', 'b', 'c']
Create a dictionary with uppercase letters as keys and their ASCII values as values
Expected Output:
{'A': 65, 'B': 66, 'C': 67}'''
# letters = ['a', 'b', 'c']
# d={x.upper():ord(x.upper()) for x in letters}
# print(d)

'''8. Dictionary with Odd/Even Labels
Create a dictionary for numbers 1 to 5, where the value is "even" if the number is even, and "odd" if the number is odd
Expected Output:
{1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}'''
# d={x: 'even' if x%2==0 else 'odd' for x in range(1,6)}
# print(d)