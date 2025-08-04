# Set in Python

# Set is the collection of the unordered items
# Each element in the set must be unique and immutable

# All types of data can store in the set , but list and dictionary don't store

# Creating a set
my_set = {1, 2, 3, 4, 5, "hello", "world",8}
print("Original set:", my_set) #{1, 2, 3, 4, 5, 'hello', 'world', 8}

print(len(my_set)); # get length of the set



# Create empty set
empty_set = set()


# Set methods examples

# 1. add() - Adds an element
my_set.add(10)
print("After add(10):", my_set)

# 2. update() - Adds multiple elements
my_set.update([11, 12])
print("After update([11, 12]):", my_set)

# 3. remove() - Removes an element (raises KeyError if not found)
my_set.remove(1)
print("After remove(1):", my_set)

# 4. discard() - Removes an element (does nothing if not found)
my_set.discard(100)
print("After discard(100):", my_set)

# 5. pop() - Removes and returns an arbitrary element
popped = my_set.pop()
print("After pop():", my_set, "| Popped:", popped)

# 6. clear() - Removes all elements
copy_set = my_set.copy()
copy_set.clear()
print("After clear():", copy_set)

# 7. copy() - Returns a shallow copy
copied = my_set.copy()
print("Copy of set:", copied)

# 8. union() - Returns the union of sets
a = {1, 2, 3}
b = {3, 4, 5}
print("Union:", a.union(b))

# 9. intersection() - Returns the intersection
print("Intersection:", a.intersection(b))

# 10. difference() - Returns the difference
print("Difference:", a.difference(b))

# 11. symmetric_difference() - Returns the symmetric difference
print("Symmetric Difference:", a.symmetric_difference(b))  #{1, 2, 4, 5}

# 12. issubset() - Checks if set is subset
print("Is a subset of b?", a.issubset(b))

# 13. issuperset() - Checks if set is superset
print("Is a superset of b?", a.issuperset(b))

# 14. isdisjoint() - Checks if sets have no elements in common
print("Is disjoint?", a.isdisjoint(b))