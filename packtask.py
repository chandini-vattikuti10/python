'''1. Implement a Python function that packs three integers into a tuple and then unpacks this tuple back into separate integer variables, 
verifying that the original values are correctly restored.'''

# def pack_unpack(a, b, c):
#     numbers = (a, b, c)
#     print("Packed Tuple:", numbers)

#     x, y, z = numbers

#     print("Unpacked Values:")
#     print("x =", x)
#     print("y =", y)
#     print("z =", z)

#     if (a, b, c) == (x, y, z):
#         print("Original values are correctly restored.")
#     else:
#         print("Values are not restored correctly.")

# pack_unpack(10, 20, 30)

'''2. Write a Python program that demonstrates the type conversion from string to integer using the int() function, 
from integer to float using the float() function, and from string to float using a combination of these functions.'''

# str_num = "100"
# int_num = int(str_num)

# float_num = float(int_num)

# str_float = "25.75"
# float_value = float(str_float)

# print("Original String:", str_num)
# print("String to Integer:", int_num)

# print("Integer to Float:", float_num)

# print("Original String:", str_float)
# print("String to Float:", float_value)

'''3. Develop a Python function that takes a list of mixed data types (integers, floats, and strings), 
iterates over the list, and applies type conversion to ensure all elements are converted to strings, 
returning the resulting list of uniform data type.'''


# def convert_to_strings(data):
#     result = []

#     for item in data:
#         result.append(str(item))

#     return result

# mixed_list = [10, 20.5, "Python", 45, 3.14, "AI"]

# converted_list = convert_to_strings(mixed_list)

# print("Original List:", mixed_list)
# print("Converted List:", converted_list)

# print("\nData types after conversion:")
# for item in converted_list:
#     print(item, "->", type(item))
