"""
Program: Employee.py
Author: Tony Ehlert
Last date modified: 3/24/2023

The purpose of this program is to define an Employee class with private variables and a public display() method
The input is the required data needed to create and test objects create from the Employee class
The output is print statements of each variable that come from the display() method contained in the Employee class
"""
from datetime import date


class Employee:
    '''Employee Class '''

    # Constructor
    def __init__(self, lname, fname, address, phone_num, salaried, start_date, salary):
        self._last_name = lname
        self._first_name = fname
        self._address = address
        self._phone_number = phone_num
        self._salaried = salaried
        self._start_date = start_date
        self._salary = salary

    def set_last_name(self, lname):
        self._last_name = lname

    def get_last_name(self):
        return self._last_name

    def set_first_name(self, fname):
        self._first_name = fname

    def get_first_name(self):
        return self._first_name

    def set_address(self, address):
        self._address = address

    def get_address(self):
        return self._address

    def set_phone_number(self, phone_num):
        self._phone_number = phone_num

    def get_phone_number(self):
        return self._phone_number

    def set_salaried(self, salaried):
        self._salaried = salaried

    def get_salaried(self):
        return self._salaried

    def set_start_date(self, start_date):
        self._start_date = start_date

    def get_start_date(self):
        return self._start_date

    def set_salary(self, salary):
        self._salary = salary

    def get_salary(self):
        return self._salary

    def display(self):
        '''
        This method returns a formatted string containing the employee object first_name, last_name, address,
        pay(salaried vs hourly and rate), and start date

        :return: Formatted string containing employee object information
        '''
        display_string = str(self._first_name) + " " + str(self._last_name)
        display_string = display_string + "\n" + str(self._address)
        if self._salaried:
            display_string = display_string + "\nSalaried employee: $" + (f"{self._salary:,}/year")
        else:
            display_string = display_string + "\nHourly employee: $" + str(f"{self._salary:.2f}/hour")
        display_string = display_string + "\nStart Date: " + str(f"{self._start_date:%m-%e-%Y}".lstrip('0'))
        return display_string

    def __str__(self):
        str_string = "Last Name: " + self._last_name
        str_string = str_string + (", First Name: " + self._first_name)
        str_string = str_string + (", Address: " + str(self._address).replace('\n', ' '))
        str_string = str_string + (", Phone #: " + self._phone_number)
        str_string = str_string + (", Salaried: " + str(self._salaried))
        str_string = str_string + (", Start Date: " + str(self._start_date))
        str_string = str_string + (", Salary: " + str(self._salary))
        return str_string

    def __repr__(self):
        repr_string = "Employee(\"" + self._last_name
        repr_string = repr_string + ("\", \"" + self._first_name)
        repr_string = repr_string + ("\", \"" + str(self._address).replace('\n', '\\' + 'n'))
        repr_string = repr_string + ("\", \"" + self._phone_number)
        repr_string = repr_string + ("\", \"" + str(self._salaried))
        repr_string = repr_string + ("\", \"" + str(self._start_date))
        repr_string = repr_string + ("\", \"" + str(self._salary) + "\")")
        return repr_string


# Driver
if __name__ == '__main__':
    # call constructor to create new employee objects
    emp1 = Employee('Ruiz', 'Matthew', '456 Sesame Street\nAnkeny, Iowa', '515-555-1234', True, date(2023, 3, 24), 40000)
    emp2 = Employee('Patel', 'Sasha', '123 Main Street\nUrban, Iowa', '515-999-9876', False, date(2019, 6, 28), 7.25)

    # call of display()
    print(emp1.display())
    print("\n")
    print(emp2.display())
    print("\n")

    # call of __str__
    print(emp1.__str__())
    print(emp2.__str__())
    print("\n")

    # call of __rpr__
    print(emp1.__repr__())
    print(emp2.__repr__())
    print("\n")

    # delete objects
    del emp1
    del emp2
