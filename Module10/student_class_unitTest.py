import unittest
from class_definitions import Student as s

class MyTestCare(unittest.TestCase):
    def setUp(self):
        self.hillaker = s("Hillaker", "Isaac", "CIS", 3.7) #Add 3.7 to the end!
    def tearDown(self):
        del self.hillaker

    def test_object_created_required_attributes(self):
        self.assertEqual(self.hillaker.last_name, "Hillaker")
        self.assertEqual(self.hillaker.first_name, "Isaac")
        self.assertEqual(self.hillaker.major, "CIS")

    def test_object_created_all_attributes(self):
        self.assertEqual(self.hillaker.last_name, "Hillaker")
        self.assertEqual(self.hillaker.first_name, "Isaac")
        self.assertEqual(self.hillaker.major, "CIS")
        self.assertEqual(self.hillaker.gpa, 3.7)

    def test_student_str(self):
        self.assertEqual(str(self.hillaker), f"Name: Hillaker, Isaac\nMajor: CIS\nGPA: 3.7")

    def test_object_not_created_error_last_name(self):
        # Incorrect LAST name
        try:
            student = s('123', 'Isaac', 'CIS', 3.7)
        except ValueError:
            print("Last name incorrect formatting, student object not created.")

    def test_object_not_created_error_first_name(self):
        # Incorrect FIRST name
        try:
            student = s('Hillaker', '123', 'CIS', 3.7)
        except ValueError:
            print("First name incorrect formatting, student object not created.")

    def test_object_not_created_error_major(self):
        # Incorrect MAJOR name
        try:
            student = s('Hillaker', 'Isaac', '123', 3.7)
        except ValueError:
            print("Major incorrect formatting, student object not created.")

    def test_object_not_created_error_gpa(self):
        # Incorrect GPA value, whole number/integer
        try:
            student = s('Hillaker', 'Isaac', 'CIS', 4)
        except ValueError:
            print("GPA wrong data type, student object not created.")

    def test_object_not_created_error_gpa_type(self):
        # Incorrect GPA value, whole number/integer
        try:
            student = s('Hillaker', 'Isaac', 'CIS', 4.1)
        except ValueError:
            print("GPA exceeds limits, student object not created.")


if __name__ == '__main__':
    unittest.main()