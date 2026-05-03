# greet function
'''def greet():
    return "Hey!Good Morning!"
print(greet())'''

'''def greet(name):
    print("hello",name)
greet('chandini')'''

'''def add(a,b):
    return a+b
print(add(3,4))'''

# square of a number
'''def square(a):
    return a**2
print(square(4))'''

'''def is_even(n):
    return n%2==0
print(is_even(4))
print(is_even(7))'''
# max of two numbers
'''def find_max(a,b):
    return max(a,b)
print(find_max(10,5))
print(find_max(3,8))'''

'''def find_max(a,b):
    if a>b:
        return a
    else:
        return b
print(find_max(10,5))
print(find_max(3,8))'''
# find max of three
'''def find_max_of_three(a,b,c):
    if a>b and a>c:
        return a
    elif b>c:
        return b
    else:
        return c
print(find_max_of_three(3,6,2))'''

# grade marks
'''def grade(marks):
    if marks>=90:
        return "A"
    elif marks>=75:
        return "B"
    elif marks>=50:
        return "C"
    else:
        return "D"
print(grade(92))
print(grade(76))
print(grade(40))'''

'''def predict_pass(marks):
    if marks>=50:
        print('pass')
    else:
        print("Fail")
predict_pass(60)
predict_pass(30)'''

'''def predict_pass(marks):
    if marks>=50:
        return 'pass'
    else:
        return "Fail"
print(predict_pass(60))
print(predict_pass(30))'''

'''def predict_pass(marks):
    if marks>=50:
        return "pass"
    else:
        return "Fail"
def predict_bulk(marks_list):
    result=[]
    for marks in marks_list:
        result.append(predict_pass(marks))
    return result
    
print(predict_bulk([90, 40, 65]))'''

'''def predict_pass(marks):
    if marks>=75:
        return "distinction"
    elif marks>=50:
        return "pass"
    else:
        return "fail"
def predict_bulk(marks_in_list):
    result=[]
    for marks in marks_in_list:
        result.append(predict_pass(marks))
    return result
print(predict_bulk([80,45,60]))'''


'''1. def sum_list(numbers):
    sum=0
    for x in numbers:
        sum+=x
    return sum
print(sum_list([1,2,3,4]))'''

'''2. def count_even(numbers):
    count=0
    for x in numbers:
        if x%2==0:
            count+=1
    return count
print(count_even([1,2,4,7]))'''

'''3. def find_min(numbers):
    min=numbers[0]
    for x in numbers:
        if x<min:
            min=x
    return min
print(find_min([4,2,1,3]))'''

'''4. def reverse_list(list):
    temp=[]
    for num in list:
        temp=[num]+temp
    return temp
print(reverse_list([1,2,3,4,5]))'''

'''5. def count_pass(lst_marks):
    count=0
    for marks in lst_marks:
        if marks>=50:
            count+=1
    return count
print(count_pass([56,78,90,23,43]))'''


'''6. def pass_marks(marks):
    if marks>=90:
        return "A"
    elif marks>=75:
        return "B"
    elif marks>=50:
        return "C"
    else:
        return "fail"
def grades_bulk(lst_marks):
    result=[]
    for marks in lst_marks:
        result.append(pass_marks(marks))
    return result
print(grades_bulk([89,56,43,57,80,78]))'''

'''7. def remove_duplicates(lst):
    temp=[]
    for x in lst:
        if x not in temp:
            temp.append(x)
    return temp
print(remove_duplicates([1,2,1,3,2,3,1,3,4,2,3]))'''


'''8. def second_largest_number(lst):      #[67,89,76,34]
    largest=lst[0]                    #67
    second=lst[0]                       #67
    for num in lst:  #67 89
        if num > largest: #89>67 x
            second=largest  
            largest=num
        elif num >second and num != largest:
            second=num
    return second
print(second_largest_number([67,89,76,34]))'''


'''def leap_year(years):
    for i in range(1900,2001):
        if i%4==0:
            return "leap"
        else:
            return "non leap"
print(leap_year(i))
'''

'''for i in range(1900,2001):
    if i%4==0:
        print(i)'''

'''n=int(input())    #9
sum=0
s=n**2       #81
while s>0:
    digit=s%10 
    sum=sum+digit     #81%10=1
    s=s//10           #81//10= 1
print(sum)'''
