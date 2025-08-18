# To map with real world scenarios, we started using objects in code.
# This is called object oriented programming.

#For function --> redundancy decrease and reuseablity increase.



#Class is a blueprint for creating objects.


#Imagine like A class room is a class and all students of the class romm is objects.



#Creating class
class Student:
    name = "opi"


#Imagine like a class is noting without students. So, for represent class , object must needed.
#Creating object (Another name is instance)

s1= Student()
print(s1.name)

class Car:
    color = "blue"
    brand = "mercedes"

car1= Car()

print(car1.brand)




#Constructor

#All classes have a function called __init__() , which is always executed when the class is being initiated.

# __init__ runs when the object is created.

# self refers to this object.

# self.name and self.age store the data.

class Person:
    #default constructors
    def __init__(self):
        pass

    #parameterized constructors
    def __init__(self, Fullname, MyAge):
        self.name = Fullname  # attribute
        self.age = MyAge    # attribute

# Create object with data
p1 = Person("Opi", 21)

print(p1.name)  # Opi
print(p1.age)   # 21


#Class & Instancec Attributes

"""
Class Attributes:
    Definition: Shared by all objects of the class

    Where defined: Inside class, outside any method

    Accessed with: ClassName.attribute or object.attribute

    Stored in : Class" memory

Instance Attribute:
    Definition: Unique for each object

    Where defined: Inside __init__() (or other instance methods)

    Accessed with: Always object.attribute

    Stored in : Each object's memory
"""

class Student:
    # Class attribute (shared)
    school_name = "Dhaka University"

    def __init__(self, name, roll):
        # Instance attributes (unique per object)
        self.name = name
        self.roll = roll

# Create two students
s1 = Student("Opi", 101)
s2 = Student("Rafi", 102)

# Access attributes
print(s1.name)         # Opi (instance attribute)
print(s2.name)         # Rafi
print(s1.school_name)  # Dhaka University (class attribute)
print(s2.school_name)  # Dhaka University (shared)

# Changing instance attribute affects only that object
s1.name = "Maharab"
print(s1.name)  # Maharab
print(s2.name)  # Rafi

# Changing class attribute affects all objects
Student.school_name = "BUET"
print(s1.school_name)  # BUET
print(s2.school_name)  # BUET

# If class att. and obj att. are same then and call the att. then obj att. come fast.

# Methods
# Methods are functions that belong to objects.


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):  # Instance method
        print(self.name + " has " + str(self.marks) + " marks.")

    def welcome(self):
        return self.marks

s1 = Student("Opi", 90)
s1.display()

print(s1.welcome())



#Static Methods

# Methods that don't use the self parameter (Work at class level)


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod  #decorator
    def hello():
        print("Hello")

    def display(self):  # Instance method
        print(self.name + " has " + str(self.marks) + " marks.")

    def welcome(self):
        return self.marks


"""
What is decorator?
--> Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it. 
    """



