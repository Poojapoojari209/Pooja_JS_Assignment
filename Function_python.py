#Easy
# Function to add two numbers
def add(a, b):
    return a + b

print(add(5, 3))   # Output: 8


#  Function to greet a person
def greet(name):
    return "Hello, " + name

print(greet("Pooja")) #Hello, Pooja


# Function to check even or odd
def check_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even(10))  # Output: Even


#  Medium Level
# Function to find factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))  # Output: 120


# Function to count vowels in a string
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Hello World")) #3


# Function to find maximum number in a list
def find_max(numbers):
    max_value = numbers[0]
    for n in numbers:
        if n > max_value:
            max_value = n
    return max_value

print(find_max([10, 5, 89, 32])) #89


# Advanced Level
# Function with default and keyword arguments
def employee_details(name, role="Developer", location="India"):
    return f"Name: {name}, Role: {role}, Location: {location}"

print(employee_details("Pooja"))
print(employee_details("Karan", role="Manager"))

# output
# Name: Pooja, Role: Developer, Location: India
# Name: Karan, Role: Manager, Location: India


# Function returning another function (Higher-order function)
def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

times3 = multiplier(3)
print(times3(10))   # Output: 30


# Lambda with filter (Advanced functional programming)
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)  # Output: [2, 4, 6]


# closures
def outer_function(message):
    # message is a variable from the enclosing scope
    def inner_function():
        print(f"Hello, {message}!")
    return inner_function

# Create a closure
greet_ali = outer_function("Ali")
greet_bob = outer_function("Bob")

# Call the closures
greet_ali() # Output: Hello, Ali
greet_bob() # Output: Hello, Bob


# Decorators
def decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

@decorator # Applying the decorator to a function
def greet():
    print("Hello, World!")
greet()

# output
# Before calling the function.
# Hello, World!
# After calling the function.