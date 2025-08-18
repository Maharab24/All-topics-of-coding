"""
del keyword:
    used to delete object properties or object itself.

    del s1.name

    del s1
"""

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Opi")
print(s1.name)   # Opi
del s1
# print(s1.name)  # ❌ NameError: name 's1' is not defined


"""
Private(like) attributes & methods:
    Private attributes & methods are meant to be used only within the class and are not accessible from outside the class.

    If I set public, i can access it from the outside of the class.



"""

class Student:

    __name = "Anonymous"
    def __hello():            # This a private function
        print("Hello person") # Used for internal uses of function
    def __init__(self, name, marks):
        self.name = name          # public attribute
        self.__marks = marks      # private attribute (double underscore)

    # method to access private attribute
    def get_marks(self):
        return self.__marks

    # method to update private attribute safely
    def set_marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self.__marks = new_marks
        else:
            print("Invalid marks!")


s1 = Student("Opi", 95)

print(s1.name)          # ✅ Works: public attribute
# print(s1.__marks)     # ❌ Error: private attribute not directly accessible

print(s1.get_marks())   # ✅ Access through method → 95

s1.set_marks(88)
print(s1.get_marks())   # ✅ Now updated → 88



#Inheritance

# When one class  (child/derived) derives the properties & methods of another class (parent/base). 