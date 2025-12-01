# Defining a Function:
def greet():
    print("Hello, world!")

# Calling a Function:
greet() 

#  Functions with Parameters:
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice") #  "Hello, Alice!"
greet_person("Bob")   #  "Hello, Bob!"

# Functions with Return Values:
def add_numbers(a, b):
    sum_result = a + b
    return sum_result

result = add_numbers(5, 3)
print(f"The sum is: {result}") # "The sum is: 8"

# Even or Odd Checker
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

num1 = 16
num2 = 7

print(f"{num1} is {check_even_odd(num1)}") # Output: 16 is Even
print(f"{num2} is {check_even_odd(num2)}") # Output: 7 is Odd

# Function with Parameters:
def greet_person(name):
    """This function greets a specific person."""
    print(f"Hello, {name}! Nice to meet you.")

# Calling the function with an argument
greet_person("Alice")
greet_person("Bob")

# Function with Parameters and a Return Value:
def add_numbers(a, b):
    """This function adds two numbers and returns their sum."""
    sum_result = a + b
    return sum_result

# Calling the function and storing the return value
result = add_numbers(10, 5)
print(f"The sum is: {result}")

another_result = add_numbers(7, 3)
print(f"Another sum is: {another_result}")

#  Function with Parameters and a Return Value:
def add_numbers(a, b):
    """This function adds two numbers and returns their sum."""
    sum_result = a + b
    return sum_result

# Calling the function and storing the return value
result = add_numbers(10, 5)
print(f"The sum is: {result}")

another_result = add_numbers(7, 3)
print(f"Another sum is: {another_result}")

# Function with Default Parameter Values:
def say_hello(name="Guest"):
    """This function greets with a default name if none is provided."""
    print(f"Hello, {name}!")

# Calling with and without an argument
say_hello("Charlie")
say_hello() # Uses the default value "Guest"