# List Operations
# Create a list
my_list = [10, 20, 30, 40, 50]

# Add an element to the end
my_list.append(60)
print(f"List after append: {my_list}")

# Insert an element at a specific index
my_list.insert(1, 15)
print(f"List after insert: {my_list}")

# Remove an element by value
my_list.remove(30)
print(f"List after remove: {my_list}")

# Remove an element by index and get its value
popped_element = my_list.pop(2)
print(f"Popped element: {popped_element}, List after pop: {my_list}")

# Sort the list
my_list.sort()
print(f"Sorted list: {my_list}")

# Reverse the list
my_list.reverse()
print(f"Reversed list: {my_list}")

# Check if an element is in the list
print(f"Is 40 in the list? {40 in my_list}")

# Create a new list from a slice of an existing list
sub_list = my_list[1:4]
print(f"Sub-list: {sub_list}")

# Extend a list with another list
another_list = [70, 80]
my_list.extend(another_list)
print(f"List after extend: {my_list}")