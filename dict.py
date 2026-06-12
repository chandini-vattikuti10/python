'''Create a Dictionary class with methods to add, remove, and search for key-value pairs.'''

# class Dictionary:
#     def __init__(self):
#         self.data = {}

#     def add(self, key, value):
#         self.data[key] = value
#         print(f"{key} added successfully.")

#     def remove(self, key):
#         if key in self.data:
#             del self.data[key]
#             print(f"{key} removed successfully.")
#         else:
#             print("Key not found.")

#     def search(self, key):
#         if key in self.data:
#             return self.data[key]
#         return "Key not found."

# d = Dictionary()

# d.add("name", "Chandini")
# d.add("age", 22)

# print(d.search("name"))

# d.remove("age")

# print(d.search("age"))

'''Implement a method to update existing key-value pairs in the dictionary.'''
# class Dictionary:
#     def __init__(self):
#         self.data = {}

#     def add(self, key, value):
#         self.data[key] = value

#     def remove(self, key):
#         if key in self.data:
#             del self.data[key]

#     def search(self, key):
#         return self.data.get(key, "Key not found")

#     def update(self, key, value):
#         if key in self.data:
#             self.data[key] = value
#             print(f"{key} updated successfully.")
#         else:
#             print("Key not found.")

# d = Dictionary()

# d.add("name", "Chandini")
# d.add("age", 22)

# d.update("age", 23)

# print(d.search("age"))


'''Develop a method to display all key-value pairs in the dictionary, sorted alphabetically by key.'''
# class Dictionary:
#     def __init__(self):
#         self.data = {}

#     def add(self, key, value):
#         self.data[key] = value

#     def remove(self, key):
#         if key in self.data:
#             del self.data[key]

#     def search(self, key):
#         return self.data.get(key, "Key not found")

#     def update(self, key, value):
#         if key in self.data:
#             self.data[key] = value

#     def display(self):
#         for key in sorted(self.data):
#             print(f"{key}: {self.data[key]}")

# d = Dictionary()

# d.add("banana", 20)
# d.add("apple", 10)
# d.add("orange", 30)

# d.display()
