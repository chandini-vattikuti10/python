''' 1. Create a list comprehension that generates the squares of all even numbers from 1 to 20.'''
# l=[x**2 for x in range(1,21) if x%2==0]
# print(l)

''' 2. Use list comprehension to filter out all words in a given list of strings that are shorter than 5 characters.'''
s=['apple','banana','kiwi','guava','ant']
l=[x.upper() for x in s if len(x)>=5]
print(l)

''' 3. Write a list comprehension that generates a list of tuples, 
where each tuple contains a number from 1 to 10 and its corresponding double value.'''
l=[(x,x*2) for x in range(1,11)]
print(l)