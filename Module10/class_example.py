class Person:
    """Person class"""
    def __init__(self, lname, fname, addy=""): #Constructor
        self.last_name = lname
        self.first_name = fname
        self.address = addy

    def __str__(self):
        return 'Person with last name ' + str(self.last_name) + ', first name ' + str(self.first_name)

class Person2:
    TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')

    def __init__(self, title, name, surname, allowed_titles=TITLES):
        if title not in allowed_titles:
            raise ValueError("%s is not a valid title." % title)

        self.title = title
        self.name = name
        self.surname = surname

    def __str__(self):
        return 'Hello, ' + str(self.title) + '. ' + str(self.name) + '.'

#Driver
person2 = Person2('Dr', 'Duck', 'Donald') # ssn not required
print(str(person2))