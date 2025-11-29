# Creating a Dictionary:

my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(f"Created dictionary: {my_dict}")

# Using the dict() constructor
another_dict = dict(country="USA", population=330_000_000)
print(f"Another dictionary: {another_dict}")

# Accessing Values:
my_dict = {"name": "Alice", "age": 30, "city": "New York"}

# Accessing by key (returns an error if key not found)
name = my_dict["name"]
print(f"Name: {name}")

# Using get() method (returns None or a default value if key not found)
age = my_dict.get("age")
print(f"Age: {age}")
job = my_dict.get("job", "Unemployed") # Default value
print(f"Job: {job}")

#  Adding and Updating Items:
my_dict = {"name": "Alice", "age": 30}

# Adding a new key-value pair
my_dict["city"] = "London"
print(f"Dictionary after adding city: {my_dict}")

# Updating an existing value
my_dict["age"] = 31
print(f"Dictionary after updating age: {my_dict}")

# Removing Items:

my_dict = {"name": "Alice", "age": 30, "city": "London"}

# Using del keyword to remove by key
del my_dict["city"]
print(f"Dictionary after deleting city: {my_dict}")

# Using pop() method to remove by key and return the value
age_removed = my_dict.pop("age")
print(f"Removed age: {age_removed}, Dictionary: {my_dict}")

# Using popitem() to remove and return an last inserted key-value pair
key, value = my_dict.popitem()
print(f"Removed item: {key}: {value}, Dictionary: {my_dict}")

# Using clear() to remove all items
my_dict = {"name": "Alice", "age": 30}
my_dict.clear()
print(f"Dictionary after clearing: {my_dict}")

my_dict = {"name": "Alice", "age": 30, "city": "New York"}

# Getting all keys
keys = my_dict.keys()
print(f"Keys: {list(keys)}")

# Getting all values
values = my_dict.values()
print(f"Values: {list(values)}")

# Getting all items (key-value pairs)
items = my_dict.items()
print(f"Items: {list(items)}")

# Checking for key existence
has_name = "name" in my_dict
print(f"Does dictionary have 'name' key? {has_name}")

# Merging dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict1.update(dict2) # Merges dict2 into dict1
print(f"Merged dictionary: {dict1}")


# output

# Created dictionary: {'name': 'Alice', 'age': 30, 'city': 'New York'}
# Another dictionary: {'country': 'USA', 'population': 330000000}
# Name: Alice
# Age: 30
# Job: Unemployed
# Dictionary after adding city: {'name': 'Alice', 'age': 30, 'city': 'London'}
# Dictionary after updating age: {'name': 'Alice', 'age': 31, 'city': 'London'}
# Dictionary after deleting city: {'name': 'Alice', 'age': 30}
# Removed age: 30, Dictionary: {'name': 'Alice'}
# Removed item: name: Alice, Dictionary: {}
# Dictionary after clearing: {}
# Keys: ['name', 'age', 'city']
# Values: ['Alice', 30, 'New York']
# Items: [('name', 'Alice'), ('age', 30), ('city', 'New York')]
# Does dictionary have 'name' key? True
# Merged dictionary: {'a': 1, 'b': 3, 'c': 4}
