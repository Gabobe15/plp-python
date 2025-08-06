# Assignment 1: Design Your Own Class! 
class Smartphone:
    def __init__(self, model, storage, ram):
        self.__model = model
        self.__storage = storage
        self.__ram = ram
    
    
    def m_property(self):
        return f"I want to purchase {self.__model} at the end of the month and it should have at least {self.__storage}GB storage and a ram of about {self.__ram}GB."
    

class Samsung(Smartphone):
    pass 

class Iphone(Smartphone):
    pass 

a12 = Samsung("Sumsung", 128, 8)
iphone10promax = Iphone("Iphone", 256, 16)


print(a12.m_property())
print(iphone10promax.m_property())


# Activity 2: Polymorphism Challenge! 🎭
class Animal:
    def eat(self):
        return "I'm eating."

class Dog(Animal):
    def sound(self):
        return "Wooo woo wooo!"

class Person(Animal):
    def sound(self):
        return "blah blah blah!"
    
dog = Dog()
person = Person()

# option one 
for s in [Dog(), Person()]:
    print(s.sound())
# option two

# for s in [dog, person]:
#     print(s.sound())








"""
    Assignment 1: Design Your Own Class! 🏗️
Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
Add attributes and methods to bring the class to life!
Use constructors to initialize each object with unique values.
Add an inheritance layer to explore polymorphism or encapsulation.
    
    """

"""
Activity 2: Polymorphism Challenge! 🎭

Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).
"""