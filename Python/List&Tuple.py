#List are mutable(changeable), ordered collections of items.
# They can contain elements of different data types, including other lists.
# They are defined using square brackets [] and can be modified after creation.
# Example of a list
mark = [1, 2, 3, 4, 5]
print("List:", mark)
# You can access elements in a list using indexing
print("First element:", mark[0])  # Output: 1
print("Last element:", mark[-1])  # Output: 5
# You can slice lists to get a sublist
print("Sublist (from index 1 to 3):", mark[1:4])  # Output: [2, 3, 4]
# You can also slice lists to get a sublist from the end
print("Sublist (from index 2 to the end):", mark[2:])
print("Sublist (up to index 3):", mark[:4])  # Output: [1, 2, 3, 4]
# You can access every second element in a list using slicing
print("Every second element:", mark[::2])  # Output: [1, 3, 5]
# You can reverse a list using slicing
print("Reversed list:", mark[::-1])  # Output: [5, 4, 3, 2, 1]
# You can also use negative indexing to access elements from the end
print("Last element using negative indexing:", mark[-1])  # Output: 5
print("Sublist using negative indexing (from index -4 to -2):", mark[- 4:-1]) # Output: [2, 3, 4]







# List methods
# You can add elements to a list using the append() method
mark.append(6)
print("List after appending 6:", mark)  # Output: [1, 2, 3, 4, 5, 6]
# You can insert elements at a specific index using the insert() method
mark.insert(2, 10)
print("List after inserting 10 at index 2:", mark)  # Output: [1, 2, 10, 3, 4, 5, 6]
# You can remove elements from a list using the remove() method
mark.remove(10)
print("List after removing 10:", mark)  # Output: [1, 2, 3, 4, 5, 6]
# You can pop elements from a list using the pop() method
popped_element = mark.pop()
print("Popped element:", popped_element)  # Output: 6
print("List after popping the last element:", mark)  # Output: [1, 2, 3, 4, 5]
# You can sort a list using the sort() method
mark.sort()
print("Sorted list:", mark)  # Output: [1, 2, 3, 4, 5]
# You can reverse a list using the reverse() method
mark.reverse()
print("Reversed list:", mark)  # Output: [5, 4, 3, 2, 1]
# You can find the index of an element using the index() method
index_of_3 = mark.index(3)
print("Index of 3:", index_of_3)  # Output: 2
# You can count the occurrences of an element using the count() method
count_of_2 = mark.count(2)
print("Count of 2:", count_of_2)  # Output: 1
# You can clear a list using the clear() method
mark.clear()
print("List after clearing:", mark)  # Output: []
# You can create a list with different data types
mixed_list = [1, "two", 3.0, True, None]
print("Mixed list:", mixed_list)  # Output: [1, 'two', 3.0, True, None]
# You can also create a list of lists (nested lists)
nested_list = [[1, 2], [3, 4], [5, 6]]
print("Nested list:", nested_list)  # Output: [[1, 2], [3, 4], [5, 6]]
# You can access elements in a nested list using multiple indexing
print("First element of the first sublist:", nested_list[0][0])  # Output: 1
print("Second element of the second sublist:", nested_list[1][1])  #
# Output: 4
# You can also use list comprehensions to create lists
squared_list = [x**2 for x in range(1, 6)]
print("List of squares:", squared_list )  # Output: [1, 4, 9, 16, 25]

# You can use the len() function to get the length of a list
print("Length of mark:", len(mark))  # Output: 0 (after clearing)
# You can use the in operator to check if an element is in a list
print("Is 3 in mark?", 3 in mark)  # Output: False (after clearing)
# You can use the max() and min() functions to find the maximum and minimum elements in a list
mark = [1, 2, 3, 4, 5]
print("Maximum element in mark:", max(mark))  # Output: 5
print("Minimum element in mark:", min(mark))  # Output: 1
# You can use the sum() function to calculate the sum of elements in a list
print("Sum of elements in mark:", sum(mark))  # Output: 15
# You can use the sorted() function to get a sorted version of a list without modifying the original list
sorted_mark = sorted(mark)
print("Sorted version of mark:", sorted_mark)  # Output: [1, 2, 3, 4, 5]
# You can use the copy() method to create a shallow copy of a list
copied_mark = mark.copy()
print("Copied list:", copied_mark)  # Output: [1, 2, 3, 4, 5]

# You can use the extend() method to add elements from another iterable (like a list) to the end of a list
mark.extend([6, 7, 8])
print("List after extending with [6, 7, 8]:", mark)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]



#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#------------------------------------------------------------



# Tuples are immutable (unchangeable) ordered collections of items.
# They can contain elements of different data types, including other tuples.

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print("Original tuple:", my_tuple)
# You can access elements in a tuple using indexing
print("First element:", my_tuple[0])  # Output: 1
print("Second element:", my_tuple[1])  # Output: 2
print("Last element:", my_tuple[-1])  # Output: 5

# You can slice tuples to get a subtuple
print("Subtuple (from index 1 to 3):", my_tuple[1:4])  # Output: (2, 3, 4)
# You can also slice tuples to get a subtuple from the end
print("Subtuple (last 3 elements):", my_tuple[-3:])  # Output: (3, 4, 5)
# You can access every second element in a tuple using slicing
print("Every second element:", my_tuple[::2])  # Output: (1, 3, 5)
# You can reverse a tuple using slicing
print("Reversed tuple:", my_tuple[::-1])  # Output: (5, 4, 3, 2, 1)
# You can also use negative indexing to access elements from the end
print("Last element using negative indexing:", my_tuple[-1])  # Output: 5
print("Subtuple using negative indexing (from index -4 to -2):", my_tuple[-4:-1])  # Output: (2, 3, 4)

# Tuple methods
# You can count the occurrences of an element using the count() method
count_of_2 = my_tuple.count(2)
print("Count of 2 in tuple:", count_of_2)  # Output: 1
# You can find the index of an element using the index() method
index_of_3 = my_tuple.index(3)
print("Index of 3 in tuple:", index_of_3)  # Output: 2
# You can create a tuple with different data types
mixed_tuple = (1, "two", 3.0, True, None)
print("Mixed tuple:", mixed_tuple)  # Output: (1, 'two', 3.0, True, None)
# You can also create a tuple of tuples (nested tuples)
nested_tuple = ((1, 2), (3, 4), (5, 6))
print("Nested tuple:", nested_tuple)  # Output: ((1, 2), (3, 4), (5, 6))
# You can access elements in a nested tuple using multiple indexing
print("First element of the first subtuple:", nested_tuple[0][0])  # Output: 1
print("Second element of the second subtuple:", nested_tuple[1][1])  # Output: 4
# You can use the len() function to get the length of a tuple
length_of_nested = len(nested_tuple)
print("Length of nested tuple:", length_of_nested)  # Output: 3
# You can use the in operator to check if an element is in a tuple
print("Is 'two' in mixed_tuple?", "two" in mixed_tuple)  # Output: True
# You can use the max() and min() functions to find the maximum and minimum elements in a tuple
print("Maximum element in my_tuple:", max(my_tuple))  # Output: 5
print("Minimum element in my_tuple:", min(my_tuple))  # Output: 1


# You can use the sum() function to calculate the sum of elements in a tuple
print("Sum of elements in my_tuple:", sum(my_tuple))  # Output: 15
# You can use the sorted() function to get a sorted version of a tuple without modifying the original tuple
sorted_tuple = sorted(my_tuple)
print("Sorted version of my_tuple:", sorted_tuple)  # Output: [1, 2, 3, 4, 5]
# You can use the tuple() function to convert a list to a tuple
list_to_tuple = tuple([6, 7, 8])
print("Converted list to tuple:", list_to_tuple)  # Output: (6, 7, 8)
# You can use the copy() method to create a shallow copy of a tuple
copied_tuple = my_tuple
print("Copied tuple:", copied_tuple)  # Output: (1, 2, 3, 4, 5)
# You can use the * operator to repeat a tuple
repeated_tuple = my_tuple * 2
print("Repeated tuple:", repeated_tuple)  # Output: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
# You can use the + operator to concatenate tuples
concatenated_tuple = my_tuple + list_to_tuple
print("Concatenated tuple:", concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6, 7, 8)
# You can use the tuple unpacking feature to assign elements of a tuple to variables
a, b, c, d, e = my_tuple
print("Unpacked variables:", a, b, c, d, e)  # Output: 1 2 3 4 5
# You can use the all() and any() functions to check conditions on elements in a tuple
print("Are all elements in my_tuple greater than 0?", all(x > 0 for x in my_tuple))  # Output: True
print("Is any element in my_tuple equal to 3?", any(x == 3 for x in my_tuple))  # Output: True
# You can use the zip() function to combine multiple tuples into a list of tuples
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
zipped = zip(tuple1, tuple2)
print("Zipped tuples:", list(zipped))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]
# You can use the reversed() function to reverse a tuple
reversed_tuple = tuple(reversed(my_tuple))
print("Reversed tuple:", reversed_tuple)  # Output: (5, 4, 3, 2, 1)
# You can use the tuple comprehension to create a tuple from an iterable
tuple_comprehension = tuple(x**2 for x in range(1, 6))
print("Tuple comprehension (squares):", tuple_comprehension)  # Output: (1, 4, 9, 16, 25)

# You can use the str() function to convert a tuple to a string
tuple_to_str = str(my_tuple)
print("Tuple to string:", tuple_to_str)  # Output: "(1, 2, 3, 4, 5)"
# You can use the eval() function to convert a string representation of a tuple back to a tuple
str_to_tuple    = eval(tuple_to_str)
print("String to tuple:", str_to_tuple)  # Output: (1, 2, 3, 4, 5)



