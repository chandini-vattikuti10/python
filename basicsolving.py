# 1. Write a program to print numbers from 1 to n.
n=5
for i in range(1,n):
    print(i)

# 2. Write a program to print numbers from m to n. 
m=3
n=7
for i in range(m,n+1):
    print(i)

#3.  Print Numbers from n to 1 in Reverse
n=5
while n>=1:
    print(n)
    n-=1

# 4. Print Numbers from n to m in Reverse
m=6
n=10
while n>=m:
    print(n)
    n-=1

# 5. Sum of n Natural Numbers
n=5
sum=0
for x in range(1,n+1):
    sum+=x
print(sum)

# 6. Factorial of a Number
n=5
n_fact=1
for x in range(1,n+1):
    n_fact*=x
print(n_fact)

# 7. Sum of m to n Numbers
m=3
n=6
sum=0
for x in range(m,n+1):
    sum+=x
print(sum)

# 8. Product of m to n Numbers
m=2
n=4
mul=1
for x in range(m,n+1):
    mul*=x
print(mul)

# 9. Print Factors of a Number
n=6
for x in range(1,n+1):
    if n%x==0:
        print(x)


# 10. Count of Factors
n=6
count=0
for x in range(1,n+1):
    if n%x==0:
        count+=1
print(count)

# 11. Prime Number Check
n=7
count=0
for x in range(1,n+1):
    if n%x==0:
        count+=1
if count==2:
    print('prime number')
else:
    print("non-prime")

# 12. Even Numbers from m to n
m=3
n=10
for x in range(m,n+1):
    if x%2==0:
        print(x)

# 13. Odd Numbers from m to n
m=3
n=10
for x in range(m,n+1):
    if x%2!=0:
        print(x)

# 14. Count of Even and Odd Numbers
m=3
n=7
count_even=0
count_odd=0
for x in range(m,n+1):
    if x%2==0:
        count_even+=1
    else:
        count_odd+=1
print('even:',count_even)
print('odd:',count_odd)

# 15. Reverse a String
s='hello'
print(s[::-1])

# 16. Check for Palindrome String
s='madam'
rev_str=''
for x in s:
    rev_str=x+rev_str
if s==rev_str:
    print('palindrome')
else:
    print('not a palindrome')


# 17. Sum of Digits
n=123
sum=0
while n>0:
    digit=n%10
    sum+=digit
    n//=10
print(sum)


# 18. Product of Digits
n=123
product=1
while n>0:
    digit=n%10
    product*=digit
    n//=10
print(product)

# 19. Armstrong Number Check
n=153
s=str(n)
l=len(s)
k=int(s)
arms=0
while k>0:
    digit=k%10
    arms+=digit**l
    k//=10
if n==arms:
    print('Armstrong number')
else:
    print('not an armstrong number')

# 20. Reverse a Number
n=123
rev=0
while n>0:
    digit=n%10
    rev=rev*10+ digit
    n//=10
print(rev)


# 21. Palindrome Number Check
n=121
temp=n
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit 
    n//=10
if temp==rev:
    print('palindrome')
else:
    print('not a palindrome')

# 22. Count Vowels in String
s='apple'
count=0
for x in 'a','e','i','o','u':
    if x in s:
        count+=1
print(count)

# 23. Count Consonants in String
s='apple'
count=0
for x in 'a','e','i','o','u':
    if x not in s:
        count+=1
print(count)

# 24. Count Vowels and Consonants
s='apple'
count_vowel=0
count_consonats=0
for x in 'a','e','i','o','u':
    if x in s:
        count_vowel+=1
    else:
        count_consonats+=1
print('vowels =',count_vowel)
print('consonants =',count_consonats)


# 25. Perfect Number Check
n=28
sum=0
for x in range(1,n):
    if n%x==0:
        sum+=x
if n==sum:
    print('perfect number')
else:
    print('non perfect number')

# 26. Neon Number Check
n=9
s=n**2
sum=0
while s>0:
    digit=s%10
    sum+=digit
    s//=10
if n==sum:
    print('neon number')
else:
    print('not neon number')

# 27. Strong Number Check
n=145
temp=n
strong=0
while n>0:
    d=n%10
    r=1
    for x in range(1,d+1):
        r*=x
    strong+=r
    n//=10
if strong==temp:
    print('strong number')
else:
    print('not strong number')

# 28. Harshad Number Check
n=18
temp=n
sum=0
while n>0:
    digit=n%10
    sum+=digit
    n//=10
if temp%sum==0:
    print('Harshad number')
else:
    print('not a harshad number')

# 29. Fibonacci Series
n=5
a,b=0,1
for x in range(n):
    print(a,end=" ")
    a,b=b,a+1

# 30. Check for Neon Number (Repeated)
n=9
s=n**2
sum=0
while s>0:
    digit=s%10
    sum+=digit
    s//=10
if n==sum:
    print('neon number')
else:
    print('not neon number')