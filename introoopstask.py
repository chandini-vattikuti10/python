'''Create a Vehicle class with attributes like color, speed, and type, and 
implement methods to display vehicle information and calculate the time it takes to travel a certain distance.'''

# class vehicle:
#     def __init__(self):
#         self.name='Audi'
#         self.color='black'
#         self.speed=130
#         self.type='xy12'
#     def vehicle_info(self):
#         print("vehicle Information:")
#         print('name: ',self.name)
#         print('color: ',self.color)
#         print('speed: ',self.speed)
#         print('type: ',self.type)
#     def distance(self):
#         distance=int(input('enter distance: '))
#         time=distance/self.speed
#         print(f'time taken to travel a certain distance: {time:.2f} hours')
        
# obj=vehicle()
# obj.vehicle_info()
# obj.distance()


'''Design an Employee class with attributes such as name, age, and salary, 
and include methods to display employee details and calculate the employee's bonus based on their salary.'''


# class employee:
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
#     def employee_details(self):
#         print("===========================================")
#         print("Employee Details")
#         print("Employee Name:",self.name)
#         print("Employee age: ",self.age)
#         print("employee salary: ",self.salary)
#     def bonus(self):
#         if self.salary<=20000:
#             bonus=self.salary*0.05
#             print("Bonus credited: ",bonus)
#         elif self.salary<=50000:
#             bonus=self.salary*0.1
#             print("Bonus credited: ",bonus)
#         else:
#             bonus=self.salary*0.5
#             print("Bonus credited: ",bonus)
# obj=employee('uma',35,15000)
# obj1=employee('kavya',29,50000)
# obj2=employee('krishna',30,65000)
# obj3=employee('padma',35,20000)
# obj.employee_details()
# obj.bonus()
# obj1.employee_details()
# obj1.bonus()
# obj2.employee_details()
# obj2.bonus()
# obj3.employee_details()
# obj3.bonus()


'''Develop a BankAccount class with attributes like account number, account holder's name, and balance, 
and implement methods to deposit and withdraw money, displaying the updated balance after each transaction.'''
# class BankAccount:
#     def __init__(self):
#         self.account_number=87654324567865
#         self.acc_holder_name='srinivas'
#         self.balance=100000
#         print("Account number: ",self.account_number)
#         print("Account holderr name: ",self.acc_holder_name)
#         print("Balance: ",self.balance)
#     def deposit(self):
#         money_deposited=int(input("Enter money to be deposited: "))
#         self.balance+=money_deposited
#         print("Updated balance:",self.balance)
#     def withdraw(self):
#         withdrawl=int(input("Emter amount to be withdrawed: "))
#         self.balance-=withdrawl
#         print("updated balance: ",self.balance)
# obj=BankAccount()
# obj.deposit()
# obj.withdraw()
