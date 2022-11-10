class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa = 3.7):
        #Setup basic inout validation
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        gpa_max_limit = 4.0

        # Check if LAST and FIRST names contain only characters found in name_characters variable
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        #Check if MAJOR contains only characters found in name_characters variable
        if not (name_characters.issuperset(major)):
            raise ValueError
        #Check is GPA is a float
        if not isinstance(gpa, float):
            raise ValueError
        #Check is GPA exceeds 4.0 (gpa_max_limit)
        if gpa > gpa_max_limit:
            raise ValueError

        #Setup Student class attributes
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return f"Name: {self.last_name}, {self.first_name}\nMajor: {self.major}\nGPA: {self.gpa}"

#Correct Formatting, TWO student objects
student1 = Student("Hillaker", "Isaac", "CIS", 3.7)
print(student1)

student2 = Student("Applebaum", "Alice", "BUS", 3.9)
print(student2)