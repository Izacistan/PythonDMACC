import datetime


class Employee:
    def __init__(self, last_name, first_name, streetAddress, cityStateAddress, phone_number, salaried, start_date, salary):
        self._last_name = last_name
        self._first_name = first_name
        self._streetAddress = streetAddress
        self._cityStateAddress = cityStateAddress
        self._phone_number = phone_number
        self._salaried = salaried
        self._start_date = start_date
        self._salary = salary

    def set_last_name(self, last_name):
        self._last_name = last_name

    def set_first_name(self, first_name):
        self._first_name = first_name

    def set_street_address(self, streetAddress):
        self._address = streetAddress

    def set_city_state_address(self, cityStateAddress):
        self._cityStateAddress = cityStateAddress

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    def set_salaried(self, salaried):
        self._salaried = salaried

    def set_start_date(self, start_date):
        self._start_date = start_date

    def set_salary(self, salary):
        self._salary = salary


    # continue the setters

    def display(self):
        salary_msg = ""
        if self._salaried == False:
            salary_msg = "$7.25/hour"
        else:
            salary_msg = "$40,000/year"

        #Convert datetime and floats to strings for concatination.
        self._start_date = self._start_date.strftime("%x")
        self._start_date = str(self._start_date)
        self._salary = str(self._salary)

        msg = self._first_name + " " + self._last_name + "\n" + self._streetAddress + "\n" + self._cityStateAddress + "\n" + self._phone_number + "\n" + salary_msg + "\n" + self._start_date + "\n" + self._salary # Formatted output

        return msg


if __name__ == "__main__":
    emp = Employee("Patel", "Sasha", "123 Main Street", "Urban, Iowa", "515-555-5555", False, datetime.datetime.now(), 1.00)  # Finish arguments
    print(emp.display())
