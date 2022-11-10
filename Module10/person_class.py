class Person:
    """Person class"""
    def __init__(self, lname, fname, ssn=''):         # Constructor sets all to no value
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        ssn_characters = set("1234567890-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        if ssn and not ssn_characters.issuperset(ssn):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.ssn = ssn           # Social Security Number

    def __str__(self):
        return self.last_name + ", " + self.first_name + ":" + self.ssn

import unittest
from class_definitions import Person as t

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.person = t("Duck", "Daisy")

    def tearDown(self):
        del self.person

    def test_initial_value_required_attributes(self):
        self.assertEqual(self.person.last_name, 'Duck')
        self.assertEqual(self.person.first_name, 'Daisy')

    def test_inital_all_attributes(self):
        person = t('Duck', 'Daisy', '111-11-1111')  # this is not self.person from setUp, but local
        assert person.last_name == 'Duck'  # note no self here on person or assert
        assert person.first_name == 'Daisy'
        assert person.ssn == '111-11-1111'

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            p = t('123', 'Daisy')

    def test_object_not_created_error_fist_name(self):
        with self.assertRaises(ValueError):
            p = t('Duck', '123')

    def test_object_not_created_error_ssn(self):
        with self.assertRaises(ValueError):
            p = t('Duck', 'Daisy', 'abc')

    def test_person_class_display_name(self):
        self.assertEqual(str(self.person), "Duck, Daisy:")  # Uses person from setUp()

    def test_person_class_display_name_ssn(self):
        p = t('Duck', 'Daisy', '111-11-1111')  # Does not use person from setUp(), has local p
        self.assertEqual(str(p), "Duck, Daisy:111-11-1111")

    def test_person_str(self):
        self.assertEqual(str(self.person), 'Duck, Daisy:')


if __name__ == '__main__':
    unittest.main()