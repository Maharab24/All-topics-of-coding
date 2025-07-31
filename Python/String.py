str1= "This is a string"
str2 = 'This is another string'
str3 = """This is a multi-line string"""
str4 = '''This is also a multi-line string'''

# Always use double quotes for strings

#escape characters in strings
#show how to use escape characters in strings
str5 = "This is a string with a newline character\nand a tab character\tand a backslash \\"
print(str5)


#concatenation of strings
# You can concatenate strings using the + operator
str6 = str1 + " " + str2
print("Concatenated string:", str6)
# You can also use the join() method to concatenate strings
str7 = " ".join([str1, str2, str3])
print("Joined string:", str7)
# You can repeat strings using the * operator
str8 = str1 * 3
print("Repeated string:", str8)
# String formatting in Python
# You can format strings using the format() method or f-strings (Python 3.6+)
formatted_str = "{} is a string".format(str1)
print("Formatted string:", formatted_str)
# Using f-strings
name = "Alice"
f_string = f"Hello, {name}!"
print("F-string:", f_string)



# len() function to get the length of a string
print("Length of str1:", len(str1))  # Output: 16

# String indexing and slicing
# You can access individual characters in a string using indexing
print("First character of str1:", str1[0])  # Output: T
print("Last character of str1:", str1[-1])  # Output: g
print("Substring of str1 (from index 5 to 10):", str1[5:10])  # Output: is a
# You can also slice strings to get a substring
print("Substring of str1 (from index 5 to the end):", str1[5:])  # Output: is a string
print("Substring of str1 (up to index 10):", str1[:10])  # Output: This is a string
print("Substring of str1 (every second character):", str1[::2])  # Output: Ti s a trng
print("Substring of str1 (reversed):", str1[::-1])  # Output: gnirts a si sihT


# negative indexing
print("Last character of str1 using negative indexing:", str1[-1])  # Output: g
print("Substring of str1 using negative indexing (from index -10 to -5):", str1[-10:-5])  # Output: is a string
print("Substring of str1 using negative indexing (from index -5 to the end):", str1[-5:])  # Output: string
print("Substring of str1 using negative indexing (up to index -5):", str1[:-5])  # Output: This is a string
print("Substring of str1 using negative indexing (every second character):", str1[-1::-2])  # Output: gni s a sihT
print("Substring of str1 using negative indexing (reversed):", str1[::-1])  # Output: gnirts a si sihT
print("Substring of str1 using negative indexing (every third character in reverse):", str1[-1::-3])  # Output: g a iT
print("Substring of str1 using negative indexing (every fourth character in reverse):", str1[-1::-4])  # Output: g s iT
print("Substring of str1 using negative indexing (every fifth character in reverse):", str1[-1::-5])  # Output: g a T


# String Functions
# Python provides several built-in functions for string manipulation

Str9 = "hello, World!"
Str9.endswith("World!")  # True, because str9 ends with "World!"
Str9.capitalize()  # "Hello, world!", capitalizes the first character
# capitalize() does not change the rest of the string . it creates a new string and does not modify the original string
# to modify the original string, you need to assign the result back to the variable
Str9 = Str9.capitalize()  # Now Str9 is "Hello, world!"



Str9.startswith("hello")  # True, because str9 starts with "hello"
Str9.find("World")  # 7, returns the index of the first occurrence of "World"



Str9.replace("World", "Python")  # "hello, Python!", replaces "World" with "Python"
Str9.upper()  # "HELLO, WORLD!", converts the string to uppercase
Str9.lower()  # "hello, world!", converts the string tolowercase
Str9.title()  # "Hello, World!", converts the first character of each word to uppercase



#Practice problems

# WAP to input user's name and print its length

user_name = input("Enter your name: ")
print("Length of your name is:", len(user_name))



# WAP to find the occurence of $ character in a string
sample_string = "Hello $World! $Python is great. $"
occurrences = sample_string.count("$")
print("The '$' character occurs", occurrences, "times in the string.")


