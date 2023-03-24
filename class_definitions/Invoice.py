"""
Program: Invoice.py
Author: Tony Ehlert
Last date modified: 3/24/2023

The purpose of this program is to define an Invoice class and create invoice objects
The input is data needed to define and create the Invoice class and its methods
The output is prints to the console from the creat_invoice() that contains each item and price along with
the calculated tax and total including tax
"""
class Invoice:
    """Invoice Class"""

    # Constructor
    def __init__(self, invceid, cid, addy, lname, fname, pnum, items_with_price = {}):
        self._invoice_id = invceid
        self._customer_id = cid
        self._address = addy
        self._last_name = lname
        self._first_name = fname
        self._phone_number = pnum
        self._items_with_price = items_with_price

    def __str__(self):
        str_string = "Invoice ID: " + str(self._invoice_id) + ", "
        str_string = str_string + "Customer ID: " + str(self._customer_id) + ", "
        str_string = str_string + "Address: " + self._address + ", "
        str_string = str_string + "Last Name: " + self._last_name + ", "
        str_string = str_string + "First Name: " + self._first_name + ", "
        str_string = str_string + "Phone #: " + self._phone_number + ", "
        str_string = str_string + "Items w/ Price: " + str(self._items_with_price)
        return str_string

    def __repr__(self):
        return 'Invoice({},{},{},{},{},{}, {})'.format(self._invoice_id, self._customer_id, self._address,
                                                       self._last_name, self._first_name, self._phone_number,
                                                       self._items_with_price)

    @property
    def invoice_id(self):
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self._invoice_id = value

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value

    @property
    def items_with_price(self):
        return self._items_with_price

    @items_with_price.setter
    def items_with_price(self, value):
        self._items_with_price = value

    def add_item(self, item_with_price):
        """
        This method adds an item and price (contained in a dictionary variable) to the invoice's
        items_with_price dictionary

        :param item_with_price: dictionary containing single pair of item and price
        :return: NONE
        """
        self._items_with_price.update(item_with_price)

    def create_invoice(self):
        """
        This method prints each item in the invoice's items_with_price dictionary and also calculates and prints
        the tax total and invoice total including tax
        :return: NONE
        """
        # tax rate variable
        TAX_RATE = 0.06

        # create variable to store subtotal
        subtotal = 0.00

        # loop through all pairs in dictionary
        for key, value in self._items_with_price.items():
            # print each item and price
            print(f"{key}.....${value:.2f}")
            subtotal = subtotal + value

        # calculated tax amount
        tax_total = (subtotal * TAX_RATE)

        # print tax_total
        print(f"Tax.....${tax_total:.2f}")

        # calculate invoice_total
        invoice_total = (subtotal + tax_total)

        # print invoice_total
        print(f"Total.....${invoice_total:.2f}")




# driver code
if __name__ == "__main__":
    invoice = Invoice(1, 123, '1313 Disneyland Dr, Anaheim, CA 92802', 'Mouse', 'Minnie', '555-867-5309')
    invoice.add_item({'iPad': 799.99})
    invoice.add_item({'Surface': 999.99})
    invoice.create_invoice()

    # test of __str__ and __repr__ methods
    print("\n")
    print(invoice)
    print(invoice.__repr__())

    # delete objects
    del invoice