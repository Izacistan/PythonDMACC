class Person:
    """Person class"""
    def __init__(self, lname, fname, addy=''):
        self._last_name = lname
        self._first_name = fname
        self._address = addy


    def display(self):
        return self._last_name + ", " + self._first_name + ":" + self._address

class Student(Person): #Base class is Person
    """Student is a derived class of Person base class"""
    def __init__(self, student_id, lname, fname, major="Computer Science", gpa="0.0"):  # default values
        super().__init__(lname, fname)  # calls the base constructor
        self._student_id = student_id
        self._major = major
        self._gpa = gpa

    def display(self):
        return f"Student ID: {self._student_id}\nName: {self._last_name}, {self._first_name}\nMajor: {self._major}\nGPA: {self._gpa}\n"



# Driver
my_student = Student(900111111, 'Song', 'River')
print(my_student.display())
my_student = Student(900111111, 'Song', 'River', 'Computer Engineering')
print(my_student.display())
my_student = Student(900111111, 'Song', 'River', 'Computer Engineering', 4.0)
print(my_student.display())
del my_student