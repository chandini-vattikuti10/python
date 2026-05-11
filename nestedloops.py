# Create a simple program that uses nested loops to print a 5x5 grid of numbers, with each row and column numbered from 1 to 5.
# for x in range(1,6):
#     for y in range(1,6):
#         print(y, end=' ')
#     print()


# Write a nested loop program to calculate and display the multiplication table for numbers 1 through 5.
# for x in range(1,6):
#     for y in range(1,11):
#         print(x,'x',y,'=',x*y)
#     print()


# Develop a program that uses nested loops to generate and print all possible combinations of two dice rolls, with each die having 6 possible outcomes.
# for x in range(1,7):
#     for y in range(1,7):
#         print(x,y)
#     print()


# c=64
# for x in range(4):
#     for y in range(5):
#         c+=1
#         print(chr(c),end=' ')
#     print()

# c=64
# for x in range(1,6):
#     for y in range(1,x+1):
#         print(chr(c+y),end=' ')
#     print()


# for n in range(100,500):
#     s=str(n)
#     l=len(s)
#     tem=0
#     for x in s:
#         tem+=int(x)**l
#     if n==tem:
#         print(n)


# for n in range(5, 100):
#     sum = 0
#     for x in range(1, n):
#         if n % x == 0:
#             sum += x
#     if sum == n:
#         print('perfect number=', n)


# n=[10,11,12]
# for x in n:
#     count=0
#     for y in range(1,x):
#         if x%y==0:
#             count+=1
#     if count==1:
#         print('prime',x)

# for x in range(10,20):
#         for y in range(1):
#             if x%2==0:
#                 print(x)

# s=-1
# while s>=-10:
#     print(s)
#     s-=1

s = 20
while s <= 30:
    # if s%2!=0:
    print(s)
    s += 2
