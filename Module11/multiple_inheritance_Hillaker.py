class Person:
    """Person class"""
    def __init__(self, lname, fname):
        self._last_name = lname
        self._first_name = fname


class Employee:
    """Employee class"""
    def __init__(self, start_date, salary):
        self._start_date = start_date
        self._salary = salary

    def display(self):
        return f"Start Date: {self._start_date}\nSalary: {self._salary}"


class Manager(Person, Employee):
    """Manager class"""
    def __init__(self, _last_name, _first_name, _start_date, _salary, dept):
        Person.__init__(self, _last_name, _first_name)
        Employee.__init__(self, _start_date, _salary)
        self._department = dept
        self._direct_reports = []

    def display(self):
        return f"Name: {self._last_name}, {self._first_name}\nStart date: {self._start_date}\nSalary: {self._salary}\nDepartment: {self._department}\n"

    def get_reports(self):
        return f"{self._direct_reports[0]}\n"

    def change_salary(self, salary):
        self._salary = salary

# Driver

# Creates and displays Manager object.
manager1 = Manager("Hillaker", "Isaac", "11/09/2022", "$40,000", "IT")
print(manager1.display())

#Creates at least 3 direct_reports
employee1 = Employee("01/01/2017", "$30,000")
employee2 = Employee("02/01/2018", "$40,000")
employee3 = Employee("03/01/2019", "$50,000")
manager1._direct_reports.append(employee1)
manager1._direct_reports.append(employee2)
manager1._direct_reports.append(employee3)

# manager1 not returning direct_report list as readable objects. Using __str__ does not help.
print(manager1.get_reports())

# Change Salary to $42,000
manager1.change_salary("$42,000")
print(manager1.display())
