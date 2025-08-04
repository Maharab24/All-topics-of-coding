# Loop in Python

# 1. For loop
print("For loop example:")
for i in range(5):
    print(i)

# 2. While loop
print("While loop example:")
count = 0
while count < 5:
    print(count)
    count += 1

# 3. Looping through a list
fruits = ["apple", "banana", "cherry"]
print("Looping through a list:")
for fruit in fruits:
    print(fruit)

# 4. Looping through a dictionary
student = {"name": "Alice", "age": 20}
print("Looping through a dictionary (keys):")
for key in student:
    print(key, ":", student[key])

print("Looping through a dictionary (items):")
for key, value in student.items():
    print(key, ":", value)




# For-else example
print("For-else example:")
for i in range(3):
    print("Inside loop:", i)
else:
    print("This runs after the for loop completes (no break)")

# For-else with break
print("For-else with break example:")
for i in range(3):
    print("Inside loop:", i)
    if i == 1:
        break
else:
    print("This will NOT run because the loop was broken with break")





# Using range() in for loop
print("Using range() in for loop:")
for i in range(1, 6):  # Starts from 1, ends at 5
    print(i)

# range(start, stop, step)
print("Using range() with step:")
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)