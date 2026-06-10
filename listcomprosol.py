'''1.	Write a list comprehension to generate numbers from 0 to 9.'''
# num=[x for x in range(10)]
# print(num)

'''2.	Generate a list of squares of numbers from 1 to 10.'''
# square=[x**2 for x in range(1,11)]
# print(square)

''' 3.	Create a list of even numbers from 1 to 20.'''
# num=[x for x in range(1,20) if x%2==0]
# print(num)

''' 4.	Extract each character from the string "python" using list comprehension.'''
# s='python'
# l=[x for x in s]
# print(l)

''' 5.	Convert all characters of "python" to uppercase using list comprehension.'''
# s='python'
# u=[x.upper() for x in s]
# print(u)

''' 6.	Generate all numbers between 1 and 20 that are multiples of 3 or 5.'''
# num=[x for x in range(1,21) if x%3==0 and x%5==0]
# print(num)

''' 7.	Create a list of squares of odd numbers between 1 and 15.'''
# n=[x for x in range(1,15) if x%2!=0]
# print(n)

''' 8.	Generate all numbers between 50 and 100 that end with digit 5.'''
# num=[x for x in range(50,100) if x%10==5]
# print(num)

''' 9.	Reverse each word in the list ["apple", "banana", "cherry"].'''
# l=['apple','banana','cherry']
# s=[x[::-1] for x in l]
# print(s)

''' 10.	Remove all zeros from the list [10, 0, 20, 30, 0, 40].'''
# l=[10, 0, 20, 30, 0, 40]
# s=[x for x in l if x!=0]
# print(s)

''' 11.	Create all pairwise sums of [1,2,3] and [10,20,30] using list comprehension.'''
# p=[1,2,3]
# q=[10,20,30]
# r=[x+y for x,y in zip(p,q)]
# print(r)

''' 12.	Generate a 3×3 matrix using nested list comprehension.'''
# matrix = [[j for j in range(1, 4)] for i in range(3)]
# print(matrix)

''' 13.	Flatten the list [[1,2,3],[4,5],[6]] using list comprehension.'''
# l=[[1,2,3],[4,5],[6]]
# r=[y for x in l for y in x]
# print(r)

''' 14.	Generate a list of squares for even numbers and cubes for odd numbers from 1–10.'''
# r=[x**2 if x%2==0 else x**3 for x in range(1,10)]
# print(r)

''' 15.	Create a multiplication table (1–3 × 1–3) using nested list comprehension.'''
# r=[x*y for x in range(1,4) for y in range(1,4)]
# print(r)

''' 16.	Extract vowels from the string "Python".'''
# s='python'
# r=[x for x in s if x in 'aeiou']
# print(r)

''' 17.	Generate a list of ASCII values for the string "ABC".'''
# s="ABC"
# r=[ord(x) for x in s]
# print(r)

''' 18.	Generate uppercase alphabets A–Z using list comprehension.'''
# r=[chr(x) for x in range(65,91)]
# print(r)

''' 19.	Capitalize every word in "hello world python".'''
# s="hello world python"
# r=[x.upper() for x in s.split()]
# print(r)

''' 20.	Print "Even" or "Odd" for numbers 1–10 using list comprehension.'''
# r=['even' if x%2==0 else 'odd' for x in range(1,11)]
# print(r)

''' 21.	Find the length of each word in ["Ajay","Python","Django"].'''
# l=["Ajay","Python","Django"]
# r=[len(x) for x in l]
# print(r)

''' 22.	Extract file extensions from ["data.csv","report.pdf","image.png"].'''
# l=["data.csv","report.pdf","image.png"]
# r=[x.split('.')[-1] for x in l]
# print(r)

''' 23.	Create a dictionary where keys are numbers 1–5 and values are their squares.'''
# r={x:x**2 for x in range(1,6)}
# print(r)

''' 24.	Map characters of "ABC" to their ASCII values using dictionary comprehension.'''
# s="ABC"
# r={x:ord(x) for x in s}
# print(r)

''' 25.	Combine ['a','b','c'] and [1,2,3] into a dictionary using comprehension.'''
# p=['a','b','c']
# q=[1,2,3]
# r={x:y for x,y in zip(p,q)}
# print(r)

''' 26.	Generate all prime numbers between 1 and 100 using list comprehension.'''
# primes = [x for x in range(2, 101)
#           if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]
# print(primes)

''' 27.	Create all possible pairs (x, y) from [1,2,3] and [3,1,4] where x ≠ y.'''
# p=[1,2,3]
# q=[3,1,4]
# r=[(x,y) for x in p for y in q if x!=y]
# print(r)

''' 28.	Generate palindrome numbers between 1 and 100.'''
# r=[x for x in range(1,100) if str(x)==str(x)[::-1]]
# print(r)

''' 29.	Add elements from two lists [1,2,3] and [10,20,30] using list comprehension.'''
# p=[1,2,3]
# q=[10,20,30]
# r=[x+y for x,y in zip(p,q)]
# print(r)

''' 30.	Extract all student names from [{'name':'Ajay','marks':80},{'name':'Riya','marks':90}].'''
# l=[{'name':'Ajay','marks':80},{'name':'Riya','marks':90}]
# r=[x['name'] for x in l]
# print(r)

''' 31.	Generate all palindromic numbers between 1 and 1000.'''
# r=[x for x in range(1,1000) if str(x)==str(x)[::-1]]
# print(r)

''' 32.	Get all words starting with 'a' from ['apple','ant','banana','ball'].'''
# l=['apple','ant','banana','ball']
# r=[x for x in l if x[0]=='a']
# print(r)

''' 33.	Generate numbers between 1 and 20 that are divisible by 2 or 3.'''
# r=[x for x in range(1,20) if x%2==0 and x%3==0]
# print(r)

''' 34.	Generate all coordinate pairs [x, y] where x and y range from 0 to 2.'''
# r=[[x,y] for x in range(3) for y in range(3)]
# print(r)
