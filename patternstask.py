'''Create your name using patterns in python'''
"""CHANDINI"""
for row in range(1,6):
    for col in range(1,6):
        if col==1 or row==1 or row==5:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
print()
'''H'''
for row in range(1,6):
    for col in range(1,6):
        if col==1 or row==3 or col==5:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
print()
'''A'''
for row in range(1,6):
    for col in range(1,6):
        if col==1 or row==1 or col==5 or row==3:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
print()
'''N'''
for row in range(1,6):
    for col in range(1,6):
        if col==1 or col==row or col==5 :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
print()
'''D'''
for row in range(1,6):
    for col in range(1,6):
        if col==1 or row==1 or col==5 or row==5:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
print()
'''I'''
for row in range(1,6):
    for col in range(1,6):
        if row==1 or col==3 or row==5:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
print()
'''N'''
for row in range(1,6):
    for col in range(1,6):
        if col==1 or col==5 or col==row :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
print()
'''I'''
for row in range(1,6):
    for col in range(1,6):
        if row==1 or col==3 or row==5:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
print()
