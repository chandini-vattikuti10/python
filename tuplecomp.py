'''1. Create a tuple of squares of numbers from 1 to 15'''
# t=tuple(x**2 for x in range(1,15))
# print(t)

'''2. Create a tuple of even numbers between 1 and 50'''
# t=tuple(x for x in range(1,50) if x%2==0)
# print(t)

'''3. Create a tuple of odd numbers from 10 to 30'''
# t=tuple(x for x in range(10,30) if x%2!=0)
# print(t)

'''4. Given a string:
s = "python"
Create a tuple containing each character in uppercase'''
# s='python'
# t=tuple(x.upper() for x in s)
# t=tuple(s.upper())
# print(t)

'''5. Create a tuple of numbers divisible by 5 from 1 to 100'''
# t=tuple(x for x in range(1,100) if x%5==0)
# print(t)

'''6. Given a list:
nums = [1, 2, 3, 4, 5]
Create a tuple of cubes of all numbers'''
# nums = [1, 2, 3, 4, 5]
# t=tuple(x**3 for x in nums)
# print(t)

'''7. Given a list:
nums = [10, 15, 20, 25, 30]
Create a tuple of numbers greater than 20'''
# nums = [10, 15, 20, 25, 30]
# t=tuple(x for x in nums if x>20)
# print(t)

'''8. Given a string:
s = "hello world"
Create a tuple of vowels only'''
# s = "hello world"
# t=tuple(x for x in s if x in "aeiou")
# print(t)

'''9. Given a list:
words = ["ai", "python", "chatbot", "ml"]
Create a tuple containing the length of each word'''
# words = ["ai", "python", "chatbot", "ml"]
# t=tuple(len(x) for x in words)
# print(t)

'''10. Create a tuple of numbers from 1 to 20 where:
 If number is even → square it
 If number is odd → cube it'''
# t=tuple(x**2 if x%2==0 else x**3 for x in range(1,20))
# print(t)