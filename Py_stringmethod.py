# Create a string
my_string = "Python Programming is Fun!"

# uppercase
print(f"Uppercase: {my_string.upper()}")

# lowercase
print(f"Lowercase: {my_string.lower()}")

# capitalized
print(f"capitalizrd:{my_string.capitalize()}")

# Replace a substring
new_string = my_string.replace("Fun", "Awesome")
print(f"Replaced: {new_string}")

# Split the string into a list of words
words = my_string.split()
print(f"Words: {words}")

# Join the words back into a string with a different separator
joined_string = "-".join(words)
print(f"Joined: {joined_string}")

# Check if the string starts or ends with a specific substring
print(f"Starts with 'Python': {my_string.startswith('Python')}")
print(f"Ends with 'Fun!': {my_string.endswith('Fun!')}")

