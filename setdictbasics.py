# Create a Set called colors and add the following colors: "Red", "Green", "Blue", and "Yellow". Then, remove "Green" from the Set and print the remaining colors.
colors={'Red','Green','Blue','Yellow'}
colors.remove("Green")
print(colors)

# Create a Dictionary called person with the following keys: "name", "age", and "city". Assign your name, age, and city to the corresponding values. Then, print the value of the "name" key.
person={'name':'Chandini','age':21,'city':'Rajahmundry'}
print(person['name'])

# Create a new Set called numbers and add the numbers 1, 2, 2, 3, 4, 4, 5. Then, convert the Set to a list and print the list, demonstrating that Sets automatically eliminate duplicate values.
numbers={1, 2, 2, 3, 4, 4, 5}
l=list(numbers)
print(l)
