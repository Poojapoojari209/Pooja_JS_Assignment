def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function
closure = outer_function(10)
print(closure(5))
print(closure(23))


def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter
counter1 = make_counter()
print(counter1())
print(counter1())


def pre(p):
    def add(t):
        return p + " " + t
    return add
h = pre("Hello")
print(h("world"))
print(h("python"))


# Decorator
def decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

@decorator 
def greet():
    print("Hello, World!")
greet()


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



def log_function_call(func):
    """
    A decorator that logs the name of the function being called.
    """
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished executing: {func.__name__}")
        return result
    return wrapper

@log_function_call
def greet(name):
    """
    A simple function that greets a person.
    """
    return f"Hello, {name}!"

@log_function_call
def add_numbers(a, b):
    """
    A function that adds two numbers.
    """
    return a + b

# Calling the decorated functions
print(greet("Alice"))
print(add_numbers(5, 7))