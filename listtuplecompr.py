'''Create a list comprehension that generates a list of squares of all even numbers between 1 and 20 (inclusive).'''
# l=[x**2 for x in range(1,20) if x%2==0]
# print(l)
'''Write a tuple comprehension that generates a tuple containing the names of people who are over 30 years old 
from a given list of dictionaries, where each dictionary represents a person with keys 'name' and 'age'.'''

# d=[{'name':'ram','age':34},
#    {'name':'sai','age':38},
#    {'name':'shrasti','age':29},
#    {'name':'srinu','age':40}]
# t=tuple(x['name'] for x in d if x['age']>30)
# print(t)

'''Develop a list comprehension that filters out all the strings that are shorter than 5 characters from a given list of strings 
and converts the remaining strings to uppercase.'''
s=['apple','banana','kiwi','guava','ant']
# l=[x.upper() for x in s if len(x)>=5]
# print(l)