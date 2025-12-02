# A lambda function to double a number
doubler = lambda x: x * 2
result = doubler(5)
print(f"Doubled value: {result}")


# Use lambda with map to square each number
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(f"Squared numbers: {squared_numbers}")


# Use lambda with map to convert to string
numbers = [5, 10, 15]
string_numbers = list(map(lambda x: str(x), numbers))
print(f"String numbers: {string_numbers}")


# Use lambda with map to add 5 to each number
numbers = [1, 2, 3, 4, 5]
added_numbers = list(map(lambda x: x + 5, numbers))
print(f"Numbers after adding 5: {added_numbers}")


# Use lambda with map to cube each number
numbers = [1, 2, 3, 4, 5]
cubed_numbers = list(map(lambda x: x**3, numbers))
print(f"Cubed numbers: {cubed_numbers}")


# Use lambda with map to check even
numbers = [3, 4, 9, 12, 15]
even_check = list(map(lambda x: x % 2 == 0, numbers))
print(f"Is number even?: {even_check}")



# Use lambda with filter to get only even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")


# Use lambda with filter to get numbers > 10
numbers = [5, 12, 7, 20, 3, 15]
greater_than_10 = list(filter(lambda x: x > 10, numbers))
print(f"Numbers greater than 10: {greater_than_10}")

# Use lambda with filter to get names starting with A
names = ["Arun", "Pooja", "Ajay", "Rahul", "Anita"]
names_start_with_A = list(filter(lambda x: x.startswith("A"), names))
print(f"Names starting with 'A': {names_start_with_A}")



# Use lambda with filter to get long words
words = ["hi", "hello", "no", "yes", "python"]
long_words = list(filter(lambda x: len(x) > 3, words))
print(f"Words with length > 3: {long_words}")


# Use lambda with filter to get positive numbers
numbers = [-5, 10, -2, 7, 0, -1]
positive_numbers = list(filter(lambda x: x > 0, numbers))
print(f"Positive numbers: {positive_numbers}")


# Use lambda with reduce to get sum
from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(f"The sum of numbers in {numbers} is: {sum_of_numbers}")


# The lambda function compares two numbers and returns the larger one.
from functools import reduce
numbers = [10, 5, 20, 15, 8]
max_value = reduce(lambda x, y: x if x > y else y, numbers)
print(f"The maximum value in {numbers} is: {max_value}")


# The lambda function concatenates two strings.
from functools import reduce
words = ["Hello", " ", "World", "!"]
sentence = reduce(lambda x, y: x + y, words)
print(f"The concatenated string from {words} is: '{sentence}'")