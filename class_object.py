class Dog:
    species = "Canis familiaris"  # Class attribute

    def __init__(self, name, age):
        self.name = name  
        self.age = age    

    def bark(self):
        print(f"{self.name} says Woof!")

# Creating objects (instances) of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

# Accessing attributes and calling methods
print(f"{dog1.name} is a {dog1.species} and is {dog1.age} years old.")
dog1.bark()

print(f"{dog2.name} is a {dog2.species} and is {dog2.age} years old.")
dog2.bark()



class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# creating object
s1 = Student("anitha", 23)

print(s1.name)
print(s1.age)


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def details(self):
        return f"Brand: {self.brand}, Model: {self.model}"

c1 = Car("Honda", "City")
print(c1.details())


class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name + " is barking!")

d1 = Dog("Tommy")
d2 = Dog("Bruno")

d1.bark()
d2.bark()
