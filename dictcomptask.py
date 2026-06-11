'''Count Length of Words
Given a list of words:
words = ["apple", "banana", "kiwi"]
Create a dictionary with words as keys and their lengths as values
Expected Output:
{'apple': 5, 'banana': 6, 'kiwi': 4}'''
# words = ["apple", "banana", "kiwi"]
# r={x:len(x) for x in words}
# print(r)

''' Filter Dictionary - Keep Items with Value Greater than 10
Given dictionary:
d = {'a': 5, 'b': 15, 'c': 25, 'd': 7}
Create a new dictionary only with items where value > 10
Expected Output:
{'b': 15, 'c': 25}'''
# d = {'a': 5, 'b': 15, 'c': 25, 'd': 7}
# r={x:y for x,y in d.items() if y>10}
# print(r)

''' Nested Dictionary of Squares
Create a dictionary from numbers 1 to 3, where each key has a dictionary with its square and cube
Expected Output:
{
  1: {'square': 1, 'cube': 1},
  2: {'square': 4, 'cube': 8},
  3: {'square': 9, 'cube': 27}
}'''
# d={x:{'square':x**2,'cube':x**3} for x in range(1,4)}
# print(d)

''' ASCII Mapping for Lowercase Letters
Map each lowercase letter 'a' to 'z' to its ASCII value
Expected Output:
{'a': 97, 'b': 98, ..., 'z': 122}'''
# d={chr(x):x for x in range(97,123)}
# print(d)


''' Create Reverse Word Dictionary
Given list of words:
words = ["cat", "dog", "bat"]
Create a dictionary with words as keys and their reversed strings as values
Expected Output:
{'cat': 'tac', 'dog': 'god', 'bat': 'tab'}'''
# words = ["cat", "dog", "bat"]
# d={x:x[::-1] for x in words}
# print(d)

'''Uppercase Keys
Given list:
letters = ['a', 'b', 'c']
Create a dictionary with uppercase letters as keys and their ASCII values as values
Expected Output:
{'A': 65, 'B': 66, 'C': 67}'''
# letters = ['a', 'b', 'c']
# d={x.upper():ord(x.upper()) for x in letters}
# print(d)


'''a=[0,1,2,3,4,5,6,7,8,9]
                {'even': [0, 2, 4, 6, 8], 'odd': [1, 3, 5, 7, 9]}'''

# a=[0,1,2,3,4,5,6,7,8,9]
# d={
#     'even':[x for x in a if x%2==0] ,
#    'odd':[x for x in a if x%2!=0]
#    }
# print(d)


'''Dictionary with keys as numbers 1 to 5, values as list of factors
Example:
{1: [1], 2: [1,2], 3: [1,3], 4: [1,2,4], 5: [1,5]}'''
# d={x:[y for y in range(1,x+1) if x%y==0] for x in range(1,6)}
# print(d)

'''Create a dictionary from a list of words, keys as words, values as word lengths, but only for words longer than 3 characters
List: ["hi", "hello", "world", "is", "great"]'''
List= ["hi", "hello", "world", "is", "great"]
# d={x:len(x) for x in List if len(x)>3}
# print(d)

'''Given a dictionary with names and ages, create a dictionary of names of people age > 18
people = {'John': 15, 'Alice': 25, 'Bob': 19}'''
people = {'John': 15, 'Alice': 25, 'Bob': 19}
# d={x:y for x,y in people.items() if y>18}
# print(d)

'''{2: 'prime', 3: 'prime', 4: 'notprime', 5: 'prime', 6: 'notprime'}'''
# result = {
#     n: 'prime' if len([i for i in range(1, n + 1) if n % i == 0]) == 2 else 'notprime'
#     for n in range(2, 7)
# }
# print(result)


