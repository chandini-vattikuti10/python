# Create a dictionary called student_info with keys for name, age, and grade, and then add a new key-value pair for school.
# student_info={'name':'chandini','age':16,'grade':'A'}
# student_info.update({"school":"Sri Sadguru Vidhaylam"})
# student_info['school']='Sri Sadguru Vidhaylam'
# print(student_info)


# Write a function get_student_name that takes a dictionary as input and returns the value associated with the name key.
# def get_student_name(dict):
#     return dict["name"]

# d={'name':'chandini','age':21,'place':'rjy'}
# print(get_student_name(d))

# Use a dictionary to store the prices of items in a store, and then write a function calculate_total that takes a list of item names as input and returns the total cost of those items.

store = {
    "apple": 30,
    "banana": 10,
    "milk": 50,
    "bread": 40,
    "eggs": 60
}

def calculate_total(items):
    total = 0
    for item in items:
        total += store[item]
    return total
shopping_list = ["apple", "milk", "bread"]
print(calculate_total(shopping_list))

