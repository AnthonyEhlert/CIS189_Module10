"""
Program: Customer.py
Author: Tony Ehlert
Last date modified: 3/24/2023

The purpose of this program is to create customer objects
The input is data needed to define the class and necessary methods
The output is print statements in the driver code to test the class
"""
class Customer:
    '''Customer Class'''

    # constructor
    def __init__(self, cust_id, lname, fname, phone_num, address):
        # define supersets for validation
        id_characters = set("1234567890")
        phone_num_characters = set("1234567890-()")

        # check passed in values against supersets for validation
        if not (id_characters.issuperset(cust_id)):
            raise ValueError
        if not (phone_num_characters.issuperset(phone_num)):
            raise ValueError

        self._customer_id = cust_id
        self._last_name = lname
        self._first_name = fname
        self._phone_number = phone_num
        self._address = address

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        id_characters = set("1234567890")
        if not id_characters.issuperset(value):
            raise ValueError
        self._customer_id = value


    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if value.isdigit():
            raise ValueError
        self._last_name = value
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if value.isdigit():
            raise ValueError
        self._first_name = value

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_num(self, value):
        phone_num_characters = set("1234567890-()")
        if not phone_num_characters.issuperset(value):
            raise ValueError
        self._phone_number = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    def __str__(self):
        return self.customer_id + ": " + self.last_name + ", " + self.first_name + " Phone: " + self.phone_number + " Address: " + self.address

    def __repr__(self):
        return 'Customer({},{},{},{},{})'.format(self.customer_id, self.last_name, self.first_name, self.phone_number,
                                                 self.address)

    def change_last_name(self, name):
        self.last_name = name

    def change_first_name(self, name):
        self.first_name = name

    def change_phone_number(self, number):
        self.phone_number = number

    def change_address(self, addy):
        self.address = addy

    def display(self):
        return self.customer_id + ": " + self.last_name + ", " + self.first_name + " Phone: " + self.phone_number + " Address: " + self.address

if __name__ == "__main__":
    # Valid customer
    customer_one = Customer('123', 'Duck', 'Donald', '(555)555-5555', '123 main street')  # all required
    print(str(customer_one))
    print(repr(customer_one))

    # Invalid phone
    # Wait! try/except needed!
    try:
        customer_two = Customer('123', 'Duck', 'Donald', '(555)555-5555P', '123 main street')  # all required
    except ValueError:
        print("Error found, customer not created")

    # Invalid customer_id
    # try/except needed
    try:
        customer_two = Customer('ABC', 'Duck', 'Donald', '(555)555-5555', '123 main street')  # all required
    except ValueError:
        print("Error found, customer not created")

    # Invalid first_name
    # try/except needed!
    try:
        customer_two = Customer('123', 'Duck', '2', '(555)555-5555', '123 main street')  # all required
    except ValueError:
        print("Error found, customer not created")