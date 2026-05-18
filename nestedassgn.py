# Create a program that uses nested loops to 
# print a square of asterisks (*) 
# where the size of the square is determined by user input.

n=int(input("Enter size: "))
for x in range(1,n+1):
    for y in range(1,n+1):
        print("*",end='')
    print()

# Develop a program that utilizes nested loops 
# to find all pairs of numbers in a given list 
# that add up to a target sum provided by the user.

n=int(input("enter targeted sum:"))
l=[1,2,3,4,5,6]
for x in l:
    for y in l:
        if x+y==n:
            print(x,y)


# Write a program that employs nested loops to 
# generate and print Pascal's Triangle up to a number of rows 
# specified by the user.

n = int(input("Enter the number of rows: "))
for i in range(n):
    num = 1
    
    for j in range(n - i - 1):
        print(" ", end=" ")
    
    for j in range(i + 1):
        print(num, end="   ")
        num = num * (i - j) // (j + 1)
    
    print()

