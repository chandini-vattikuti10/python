'''3. Design a main program that imports and utilizes the functions from both basic_operations and advanced_operations modules
to perform calculations based on user input, demonstrating how modules can be used to structure a larger application.'''

import basic_operations as basic
import advanced_operations as adv

print("===== Calculator Using Modules =====")

while True:
    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Exponentiation")
    print("7. Modulo")
    print("8. Exit")

    choice = int(input("Enter your choice (1-8): "))

    if choice == 1:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", basic.addition(a, b))

    elif choice == 2:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", basic.subtraction(a, b))

    elif choice == 3:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", basic.multiplication(a, b))

    elif choice == 4:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", basic.division(a, b))

    elif choice == 5:
        num = float(input("Enter a number: "))
        print("Result:", adv.square_root(num))

    elif choice == 6:
        base = float(input("Enter base: "))
        power = float(input("Enter power: "))
        print("Result:", adv.exponentiation(base, power))

    elif choice == 7:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", adv.modulo(a, b))

    elif choice == 8:
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")
