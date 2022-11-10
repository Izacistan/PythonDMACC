class Person:
    """Person class using class Student"""
    def __init__(self, lname, fname, student=''):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.student = student

    def display(self): #Grabs STUDENT CLASS and inserts its information at the end of the display string.
        return "Name: " + str(self.last_name) + ", " + str(self.first_name) + '\n'+ self.student.display()


class Student:
    """Student class for student information"""
    def __init__(self, major, start_date, gpa):
        self.major = major
        self.start_date = start_date
        self.gpa = gpa

    def change_major(self):
        self.major = "Being Awesome!"
        return self.major

    def update_gpa(self):
        self.gpa = "3.0"
        return self.gpa

    def display(self):
        return "Major: " + self.major + '\n' + "Start Date: " + self.start_date + '\n' "GPA: " + self.gpa

# Driver
student1 = Student("Computer Information Systems", '8/28/2022', '4.0')
person1 = Person('Hillaker', 'Isaac', student1)
print(person1.display()) #Prints given input from line 34.
print("")
student1.change_major() #Run change_major() function
student1.update_gpa() #Run update_gpa() function
print(person1.display()) #Prints person1 again, this time with updated student information.
#Garbage collection
del(student1)
del(person1)