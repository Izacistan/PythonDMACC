import tkinter as tkr
import random as r

'''
*********
FUNCTIONS
*********
'''


def invalid_name_input_error():
    """Displays error message to GUI when a user enters invalid data in the first or last name field."""
    error_label = tkr.Label(root, fg="red", bg="#FFFFFF",
                            text="Name can only contain letters and '-'. Please try again.")
    error_label.grid(row=1, column=1)
    return error_label


def invalid_customer_id_input_error():
    """Displays error message when a user enters bad data for the 'customer_ID' field."""
    id_error_label = tkr.Label(root, fg="red", bg="#FFFFFF",
                               text="Error. Customer ID creation failed. Must contain numbers only.")
    id_error_label.grid(row=3, column=1)
    return id_error_label


def add_to_customer_list(new_customer):
    """Appends/adds a newly created customer to 'customer_list' list."""
    customer_list.append(new_customer)


def add_to_inventory(new_item):
    """Appends/adds a newly created customer to 'customer_list' list."""
    inventory.append(new_item)


def create_customer():
    """This function takes user input from the tkinter GUI fields, validates the input,
    and creates a new customer using the customer class. It also appends the newly created
    customer to the 'customer_list'."""
    name_characters = set(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")  # Characters users may enter in both the first and last name fields.
    customer_id_characters = set(
        "1234567890")  # Characters that are allowed in the customer_ID variable. This is randomly assigned by the program and is simply an extra step in proper data validation.
    first_name = first_name_field.get()  # Gets user input from tkinter GUI, first name field.
    last_name = last_name_field.get()  # Gets user input from tkinter GUI, last name field.
    customer_ID = str(r.randint(1000000, 9999999))  # Creates a random, 7-digit customer ID between 1000000 and 9999999.
    # Validate user input against 'name_characters' and 'customer_id_characters'. Returns and error if given user data is bad.
    if not (name_characters.issuperset(last_name) and name_characters.issuperset(first_name)):
        return invalid_name_input_error()
    if not customer_id_characters.issuperset(customer_ID):
        return invalid_customer_id_input_error()
    success_msg_label = tkr.Label(root, fg="green", bg="#FFFFFF", text="New customer created!")
    success_msg_label.grid(row=7, columns=2)
    customer = Customer(first_name, last_name, customer_ID)
    add_to_customer_list(customer)
    print(customer_list)


# def display_shopping_cart():

'''
*******
CLASSES
*******
'''


class Customer:
    def __init__(self, first_name, last_name, customer_ID, shopping_cart={}):
        self._first_name = first_name
        self._last_name = last_name
        self._customer_number = customer_ID
        self._shopping_cart = shopping_cart

    def __repr__(self):
        return f"{self._first_name} {self._last_name} {self._customer_number}"

    def display_shopping_cart(self):
        return self._shopping_cart


class Item:
    def __init__(self, item_name, item_number, price, quantity):
        self._item_name = item_name
        self._item_number = item_number
        self._price = price
        self._quantity = quantity

    def __repr__(self):
        return f"{self._item_name} (Item#: {self._item_number})"

'''
***************************
INVENTORY and CUSTOMER LIST
***************************
'''
customer_list = []
inventory = []

'''
**************************
CREATE ITEMS FOR INVENTORY
**************************
'''
item1 = Item("Nintendo Switch", 1001, 299.00, 6)
item2 = Item("Playstation 5", 1002, 499.00, 0)
item3 = Item("Xbox Series X", 1003, 499.00, 1)
add_to_inventory(item1)
add_to_inventory(item2)
add_to_inventory(item3)
print(inventory)

'''
***
GUI
***
'''
root = tkr.Tk()
root.geometry('700x700')  # Resize window to adequately show buttons
root['background'] = '#FFFFFF'
# Title and Icon
root.title("Browse Items")
root.iconbitmap(
    'C:/Users/hilla/PycharmProjects/PythonDMACC/Final Project/ecommerce_supermarket_cart_store_grocery_icon_229138.ico')

# Buttons
# Button setting variables
btn_width = 35
btn_height = 15
# Exit Button
exit_button = tkr.Button(root, text="Exit", padx=35, pady=20, fg="white", bg="red", command=root.quit)
exit_button.grid(row=0, column=0)
# Customer Buttons
create_customer_btn = tkr.Button(root, text="Create New Customer", padx=35, pady=20, command=create_customer)
create_customer_btn.grid(row=0, column=5)
# Create Customer Form
first_name_label = tkr.Label(root, bg="#FFFFFF", text="First name")  # First name label
first_name_label.grid(row=1, column=1)
first_name_field = tkr.Entry(root, bg="lightgray", width=btn_width)  # First name field
first_name_field.grid(row=2, column=1)
last_name_label = tkr.Label(root, bg="#FFFFFF", text="Last name")  # Last name label
last_name_label.grid(row=3, column=1)
last_name_field = tkr.Entry(root, bg="lightgray", width=btn_width)  # Last name field
last_name_field.grid(row=4, column=1)

# View Shopping Cart Button
exit_button = tkr.Button(root, text="View Shopping Cart", padx=20, pady=20)
exit_button.grid(row=0, column=6)

# Items Gallery
# item_1 = tkr.Button(root, text="Nintendo Switch", padx=btn_width, pady=btn_height)
# item_1.pack()
# item_2 = tkr.Button(root, text="Playstation 5", padx=btn_width, pady=btn_height)
# item_2.pack()
# item_3 = tkr.Button(root, text="Xbox Series X", padx=btn_width, pady=btn_height)
# item_3.pack()


root.mainloop()
