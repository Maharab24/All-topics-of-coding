# Python Dictionary
# Dictionaries are used to store data values  in key: value paris
# They are unordered, mutable(changeable) & don't allow duplicate keys

# Example of a dictionary

student = {
    "name": "Alice",
    "age": 20,
    "grade": "A",
    "subjects": ["Math", "Science", "English"],  # list
    "marks": (90, 85, 88),                      # tuple
    "roll_no": 101,                              # int
    12.99 : 93.4
}
print("Student dictionary:", student)
print("Student name:", student["name"])
print("Subjects (list):", student["subjects"])
print("Marks (tuple):", student["marks"])
print("Roll number (int):", student["roll_no"])
print("Floating :", student[12.99])



#Assign in the existing key

student["subjects"] = ["History", "Geography"]   # new list
student["marks"] = (80, 75, 92)                  # new tuple
student["roll_no"] = 202



# Assigning new values to the student dictionary
student["hobbies"] = ["Reading", "Sports"]      # list
student["attendance"] = (95, 98, 100)           # tuple
student["year"] = 2025                          # int

print("Hobbies (list):", student["hobbies"])
print("Attendance (tuple):", student["attendance"])
print("Year (int):", student["year"])



#nested dictionary

# ...existing code...

# Nested dictionary example
student["address"] = {
    "street": "123 Main St",
    "city": "Wonderland",
    "zip": 12345
}

student["parents"] = {
    "father": {"name": "Bob", "phone": "123-456-7890"},
    "mother": {"name": "Carol", "phone": "987-654-3210"}
}

print("Address (nested dict):", student["address"])
print("Father's name:", student["parents"]["father"]["name"])
print("Mother's phone:", student["parents"]["mother"]["phone"])




# Dictionary methods examples
sample = {"a": 1, "b": 2, "c": 3}

print("Original dictionary:", sample)

# 1. clear()
sample.clear()
print("After clear():", sample)

# 2. copy()
sample = {"a": 1, "b": 2, "c": 3}
copy_sample = sample.copy()
print("After copy():", copy_sample)

# 3. fromkeys() creates a new dictionary from a list (or tuple) of keys, and assigns the same value to all those keys.
keys = ("x", "y", "z")
new_dict = dict.fromkeys(keys, 0)
print("fromkeys():", new_dict)  #{'x': 0, 'y': 0, 'z': 0}

# 4. get() method is used to safely access the value of a key in a dictionary.
print("get('a'):", sample.get("a"))
print("get('d', 'Not Found'):", sample.get("d", "Not Found"))

# 5. items()  method returns a view of the dictionary’s key-value pairs as tuples.

print("items():", list(sample.items()))  #items(): [('a', 1), ('b', 2), ('c', 3)]


# 6. keys()  method returns a view object containing all the keys in the dictionary.
print("keys():", list(sample.keys())) #keys(): ['a', 'b', 'c']



# 7. pop()
# Removes the key-value pair from the dictionary.
# Returns the value of the key that was removed.

popped = sample.pop("b")
print("pop('b'):", popped)
print("After pop():", sample)

# 8. popitem()
popped_item = sample.popitem()
print("popitem():", popped_item)
print("After popitem():", sample)

# 9. setdefault()
sample.setdefault("d", 4)
print("setdefault('d', 4):", sample)

# 10. update()
sample.update({"e": 5, "f": 6})
print("update({'e': 5, 'f': 6}):", sample)

# 11. values()
print("values():", list(sample.values()))


#We use methods to avoid error mainly




# Handling errors in dictionary

# 1. Using get() to avoid KeyError
value = student.get("non_existing_key")
print("Using get() for missing key:", value)  # Returns None if key doesn't exist

# 2. Using get() with a default value
value = student.get("non_existing_key", "Default Value")
print("Using get() with default:", value)

# 3. Handling KeyError with try-except
try:
    print(student["non_existing_key"])
except KeyError:
    print("KeyError: The key does not exist in the dictionary.")
