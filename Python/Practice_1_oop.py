
"""
Qus: Create student class that takes name and marks of 3 subjects
        as arguments in constructor. Then create a method to print the
        average.
"""

class Student:

    def __init__(self):
        pass

    def __init__(self,name, marks):
        self.name=name
        self.marks = marks


    def average(self):
        sum=0
        for i in self.marks:
            sum+=i
        print("HI ",self.name," This is your avg marks: ",sum/len(self.marks))










s1=Student("Maharab Hossain Opi",[99,90,95])
s1.average()