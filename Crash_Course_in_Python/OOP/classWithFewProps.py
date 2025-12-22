class Student():
    """"This object will keep the information about student name and grade in a school"""

    #__init__ means initialization. Whenever we create an object from this class
    def __init__(self, name: str, grade: int):
        self.name = name
        self.grade = grade
    
    #This is another built in method to print out student details when calling print(ObjectName)
    def __repr__(self):
        return f"Name: {self.name}\nGrade{self.grade}"

    #This is a user defined method to get the name of the student
    def getName(self):
        return self.name
    
    #This is a user defined method to update the grade
    def setGrade(self, grade:int):
        self.grade = grade


#Making an object from the Student class
student1 = Student("Nimal Peiris", 12)

#Printing the object
print("Printing the object")
print(student1)

#Getting the name
print("\nGetting the name")
print(student1.getName())

#Updating the grade
student1.setGrade(13)

#Print the updated student1 object
print("\nPrint the updated student1 object")
print(student1)