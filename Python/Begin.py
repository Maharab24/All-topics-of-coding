print("Hello world")

print ("This is a Python script.", "It prints a message to the console.")

name = "Opi"
print("My name is", name)
age = 25
print("I am", age, "years old.")


print(type(name))
print(type(age))

#there is a None type in Python
# None is a special constant in Python that represents the absence of a value
a= None
print(type(a))

#All keywords in Python
import keyword
print("Python keywords:")
print(keyword.kwlist)

# Python is a case-sensitive language
# This means that variables with different cases are considered different




# Now going for some basic arithmetic operations
# Arithmetic operations in Python include addition, subtraction, multiplication, division, modulus, and exponentiation

# Print two numbers sum

a = 5
b = 10
sum = a + b
print("The sum of", a, "and", b, "is", sum)
# Print two numbers product
product = a * b
print("The product of", a, "and", b, "is", product)
# Print two numbers difference
difference = a - b
print("The difference of", a, "and", b, "is", difference)
# Print two numbers quotient
quotient = a / b
print("The quotient of", a, "and", b, "is", quotient)
# Print two numbers modulus
modulus = a % b
print("The modulus of", a, "and", b, "is", modulus)




# Print two numbers exponentiation
exponentiation = a ** b
print("The exponentiation of", a, "to the power of", b, "is", exponentiation)

# Exponentiation is the operation of raising one number to the power of another
# In Python, the exponentiation operator is **

# The exponentiation operator is used to raise a number to a power
# For example, 2 ** 3 is equal to 8, because 2 raised to the power of 3 is 8
# The exponentiation operator can also be used with negative numbers
# For example, 2 ** -3 is equal to 0.125, because 2 raised to the power of -3 is 1/8
# The exponentiation operator can also be used with floating point numbers
# For example, 2.5 ** 2 is equal to 6.25, because 2.5 raised to the power of 2 is 6.25


#Relational operators in Python

a = 5
b = 10

print(a==b)  #False, because 5 is not equal to 10
print(a!=b)  #True, because 5 is not equal to 10
print(a<b)   #True, because 5 is less than 10
print(a>b)   #False, because 5 is not greater than 10
print(a<=b)  #True, because 5 is less than or equal to
print(a>=b)  #False, because 5 is not greater than or equal to 10
# Relational operators are used to compare two values
# They return a boolean value (True or False) based on the comparison

# Logical operators in Python
a = True
b = False
print(a and b)  #False, because True and False is False
print(a or b)   #True, because True or False is True
print(not a)    #False, because not True is False

# Logical operators are used to combine or negate boolean values
# They return a boolean value (True or False) based on the operation

#Assignment operators in Python
a = 5
b = 10
a += b  # a = a + b
print("After a += b, a is", a)  # a is now 15
a -= b  # a = a - b

print("After a -= b, a is", a)  # a is now 5
a *= b  # a = a * b
print("After a *= b, a is", a)  # a is now 50
a /= b  # a = a / b
print("After a /= b, a is", a)  # a is now 5.0
a %= b  # a = a % b
print("After a %= b, a is", a)  # a is now 5.0
a **= b  # a = a ** b
print("After a **= b, a is", a)  # a is now
# 9765625.0
a //= b  # a = a // b
print("After a //= b, a is", a)  # a is now 976562.0
# Assignment operators are used to assign a value to a variable
# They can also be used to perform an operation and assign the result to a variable
# For example, a += b is equivalent to a = a + b


# Type conversion in Python
# Type conversion is the process of converting one data type to another
# In Python, type conversion can be done using built-in functions like int(), float(), str(), etc.
# For example, to convert a string to an integer, you can use the int() function
num_str = "123"
num_int = int(num_str)
print("The string", num_str, "converted to integer is", num_int)
# To convert an integer to a string, you can use the str() function
num_int = 456
num_str = str(num_int)
print("The integer", num_int, "converted to string is", num_str)
# To convert a float to an integer, you can use the int() function
num_float = 3.14
num_int = int(num_float)
print("The float", num_float, "converted to integer is", num_int)
# To convert an integer to a float, you can use the float() function
num_int = 789
num_float = float(num_int)
print("The integer", num_int, "converted to float is", num_float)
# To convert a float to a string, you can use the str() function
num_float = 2.718
num_str = str(num_float)
print("The float", num_float, "converted to string is", num_str)
# To convert a string to a float, you can use the float() function
num_str = "3.14159"
num_float = float(num_str)
print("The string", num_str, "converted to float is", num_float)
# Type conversion is useful when you need to perform operations on different data types
# or when you need to display data in a specific format
# For example, if you want to add an integer and a float, you need to convert the integer to a float first
# Similarly, if you want to concatenate a string and an integer, you need to convert the integer to a string first



# Take input from user
# In Python, you can take input from the user using the input() function
user_input = input("Enter your name: ")
print("Hello,", user_input) # The input() function reads a line from the input and returns it as a string

#input() alway make the input as string
# If you want to take input as an integer, you can use the int() function
user_age = int(input("Enter your age: "))
print("You are", user_age, "years old")
# If you want to take input as a float, you can use the float() function
user_height = float(input("Enter your height in meters: "))
print("Your height is", user_height, "meters")




