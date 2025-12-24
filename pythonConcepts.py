# String methods
text = "Hello World"
print(text.upper())
print(text.lower())
print(text.capitalize())

text_with_spaces = "  Hello Python  "
print(text_with_spaces.strip())   # Output: Hello Python

sentence = "I love Python programming."
print(sentence.replace("Python", "Java")) # Output: I love Java programming.
print(sentence.find("Python"))            # Output: 7
print(sentence.startswith("I love"))      # Output: True
print(sentence.endswith("."))             # Output: True

data = "apple,banana,mango"
fruits = data.split(",")
print(fruits)  #['apple', 'banana', 'mango']

words = ["Hello", "World"]
joinstring = " ".join(words)
print(joinstring) #Hello World

# conditional and loop statement
temperature = 25
if temperature > 30:
    print("It's hot outside.")
else:
    print("It's not too hot.")


score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for i in range(5):  # Iterates from 0 to 4
    print(f"Iteration {i+1}")

count = 0
while count < 3:
    print(f"Count is: {count}")
    count += 1  

# Function
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3))       # Output: 6
print(sum_all(10, 20, 30, 40)) # Output: 100

def display_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

display_info(name="Eve", age=30, city="New York")
# Output:
# name: Eve
# age: 30
# city: New York