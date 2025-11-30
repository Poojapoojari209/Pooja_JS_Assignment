# For loop

n = 4
for i in range(0, n):
    print(i)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Example: Iterating through a range of numbers
for i in range(5):  # This will print numbers from 0 to 4
    print(i)


# while loop

cnt = 0
while (cnt < 3):
    cnt = cnt + 1
    print("Hello Geek")

# Example: Counting up to a certain number
count = 0
while count < 3:
    print(f"Count is: {count}")
    count += 1 


# User input until a specific value is entered
password = ""
while password != "secret":
    password = input("Enter the password: ")
print("Access granted!")

# Nested loop
from __future__ import print_function
for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()