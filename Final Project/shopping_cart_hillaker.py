import tkinter as tkr
import random as r
from datetime import date

'''
*********
FUNCTIONS
*********
'''


# def update_drop_menu(new_customer):
#     drop_menu.children["menu"].delete(0, "end")
#     for c in customer_list:
#         customer_list.append(c._first_name)
#         drop_menu.children["menu"].add_command(label=c._first_name, command=lambda cust=c._first_name: clicked.set(cust))
#     clicked.set(customer_list[0])


def add_item_to_cart(item):
    """Appends an item object to the shopping cart list."""
    def delete_labels():
        try:
            out_of_stock_label.after(500, out_of_stock_label.destroy())
            added_item_label.after(500, added_item_label.destroy())
        except NameError:
            pass

    if item._quantity <= 0:
        global out_of_stock_label, added_item_label
        delete_labels()
        out_of_stock_label = tkr.Label(root, fg="red", bg="#FFFFFF", text="Out of stock!")
        out_of_stock_label.grid(row=9, column=1)
    else:
        delete_labels()
        cart.append(item)
        added_item_label = tkr.Label(root, fg="green", bg="#FFFFFF",
                                     text=f"{item} added to your cart!")
        added_item_label.grid(row=9, column=1)
        print(cart)


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


def display_shopping_cart():
    # Setup Shopping Cart GUI
    shop_cart_win = tkr.Toplevel()
    shop_cart_win.geometry('700x700')
    shop_cart_win.group(root)
    shop_cart_win.title("Your Cart")
    shop_cart_win.iconbitmap(
        'C:/Users/hilla/PycharmProjects/PythonDMACC/Final Project/ecommerce_supermarket_cart_store_grocery_icon_229138.ico')

    def checkout_cart():
        checkout_win = tkr.Toplevel()
        checkout_win.geometry('700x700')
        checkout_win.group(root)
        checkout_win.title("Checkout your Cart")
        checkout_win.iconbitmap(
            'C:/Users/hilla/PycharmProjects/PythonDMACC/Final Project/ecommerce_supermarket_cart_store_grocery_icon_229138.ico')
        # Remove items from shopping cart
        cart.clear()
        print(cart)
        shop_cart_win.destroy()
        order_date = date.today()
        exit_btn = tkr.Button(checkout_win, text="Exit Shopping Cart", padx=35, pady=20, fg="white", bg="red",
                              command=checkout_win.destroy)
        exit_btn.grid(row=0, column=0)
        order_placed_label = tkr.Label(checkout_win, text=f"ORDER PLACED on {order_date}", padx=35, pady=20, fg="white", bg="blue")
        order_placed_label.grid(row=0, column=1)

    def get_cart_total():
        """Calculate total price for items in shopping cart. Return the total."""
        TAX_RATE = 0.07
        total = 0
        for price in cart:
            total += price._price
        # Calculate tax
        tax_owed = round(total * 0.07, 2)
        # Add tax to total for result.
        total = round(tax_owed + total, 2)
        return f"TAX: ${tax_owed}\nTOTAL: ${total}"

    def remove_from_cart(item):
        cart.remove(item)
        added_item_label = tkr.Label(shop_cart_win, fg="red", bg="#FFFFFF",
                                     text="Removed from cart!")
        added_item_label.grid(row=9, column=1)
        print(cart)

    # Exit Button, closes Shopping Cart Window.
    exit_btn = tkr.Button(shop_cart_win, text="Exit Shopping Cart", padx=35, pady=20, fg="white", bg="red",
                          command=shop_cart_win.destroy)
    exit_btn.grid(row=0, column=0)

    checkout_btn = tkr.Button(shop_cart_win, text="Checkout Cart", padx=35, pady=20, fg="white", bg="green",
                              command=checkout_cart)
    checkout_btn.grid(row=0, column=2)

    # Display Items
    rows = 0
    for items in cart:
        rows = rows + 1
        tkr.Button(shop_cart_win, text=items, borderwidth=1, padx=btn_width, pady=btn_height, command=lambda: remove_from_cart(items)).grid(row=rows, column=1)
        rows = rows + 1
        tkr.Label(shop_cart_win, text=items.display_price(), borderwidth=1, padx=btn_width, pady=btn_height).grid(
            row=rows, column=1)

    # Calculate tax and total cost of order.
    print(get_cart_total())
    tkr.Label(shop_cart_win, text=get_cart_total(), borderwidth=1, padx=btn_width, pady=btn_height).grid(
        row=rows, column=2)


def create_customer():
    """This function takes user input from the tkinter GUI fields, validates the input,
    and creates a new customer using the customer class. It also appends the newly created
    customer to the 'customer_list' list."""

    def invalid_name_input_error():
        global error_label
        """Displays error message to GUI when a user enters invalid data in the first or last name field."""

        error_label = tkr.Label(root, fg="red", bg="#FFFFFF",
                                text="Name can only contain letters and '-'. Please try again.")
        error_label.grid(row=1, column=1)
        return error_label

    def delete_entries():
        """Deletes the entry text within the first_name_field and last_name_field of the main GUI.
        This function runs when the create_customer() function is called via the create_customer_button in the main GUI.
        At the end of that function, delete_entries() runs and the entries are wiped clean for reuse."""
        first_name_field.delete(0, 35)
        last_name_field.delete(0, 35)
        try:
            error_label.destroy()
        except NameError:
            pass

    name_characters = set(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")  # Characters users may enter in both the first and last name fields.
    customer_id_characters = set(
        "1234567890")  # Characters that are allowed in the customer_ID variable. This is randomly assigned by the program and is simply an extra step in proper data validation.
    first_name = first_name_field.get()  # Gets user input from tkinter GUI, first name field.
    last_name = last_name_field.get()  # Gets user input from tkinter GUI, last name field.
    customer_ID = str(r.randint(1000000, 9999999))  # Creates a random, 7-digit customer ID between 1000000 and 9999999.

    if len(first_name.strip()) == 0 or len(
            last_name.strip()) == 0:  # Makes sure users can't enter NO data or BLANK data.
        return invalid_name_input_error()

    if not (name_characters.issuperset(last_name) and name_characters.issuperset(
            first_name)):  # Validate user input against 'name_characters' and 'customer_id_characters'. Returns and error if given user data is bad.
        return invalid_name_input_error()

    if not customer_id_characters.issuperset(customer_ID):
        return invalid_customer_id_input_error()

    success_msg_label = tkr.Label(root, fg="green", bg="#FFFFFF", text="New customer created!")
    success_msg_label.grid(row=7, columns=3)
    customer = Customer(first_name, last_name, customer_ID)
    add_to_customer_list(customer)
    delete_entries()
    print(customer_list)


'''
*******
CLASSES
*******
'''


class Customer:
    def __init__(self, first_name, last_name, customer_ID, shopping_cart=[], active=False):
        self._first_name = first_name
        self._last_name = last_name
        self._customer_number = customer_ID
        self._shopping_cart = shopping_cart
        self._active = active

    def __repr__(self):
        return f"{self._first_name} {self._last_name}"

    def __str__(self):
        return f"{self._first_name} {self._last_name}"

    def add_to_shopping_cart(self, item):
        self._shopping_cart.append(item)


class Item:
    def __init__(self, item_name, item_number, price, quantity):
        self._item_name = item_name
        self._item_number = item_number
        self._price = price
        self._quantity = quantity

    def __repr__(self):
        return self._item_name

    def __str__(self):
        return f"{self._item_name}"

    def display_price(self):
        return f"${self._price}"


'''
***************************
INVENTORY and CUSTOMER LIST
***************************
'''

cust_1 = Customer("Isaac", "Hillaker", 3001)
cust_2 = Customer("Alice", "Applebaum", 3001)
cust_3 = Customer("Bob", "Smith", 3001)
customer_list = [cust_1, cust_2, cust_3]
inventory = []
cart = []
'''
**************************
CREATE ITEMS FOR INVENTORY
**************************
'''
item1 = Item("Nintendo Switch", 1001, 299.00, 6)
item2 = Item("Playstation 5", 1002, 499.00, 0)
item3 = Item("Xbox Series X", 1003, 499.00, 2)
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
root.geometry('800x700')  # Resize window to adequately show buttons
root['background'] = '#FFFFFF'
# Title and Icon
root.title("Shopping Website")
root.iconbitmap(
    'C:/Users/hilla/PycharmProjects/PythonDMACC/Final Project/ecommerce_supermarket_cart_store_grocery_icon_229138.ico')

# Buttons
# Button setting variables
btn_width = 35
btn_height = 15
# Exit Button
exit_button = tkr.Button(root, text="Exit", padx=35, pady=20, fg="white", bg="red", command=root.quit)
exit_button.grid(row=0, column=0)

# Customer Select Dropdown
clicked = tkr.StringVar()
clicked.set(customer_list[0])
drop_menu = tkr.OptionMenu(root, clicked, *customer_list)
drop_menu.grid(row=0, column=1)

# Customer Buttons
create_customer_btn = tkr.Button(root, text="Create New Customer", padx=35, pady=20, command=create_customer)
create_customer_btn.grid(row=0, column=2)
# View Shopping Cart Button
view_cart = tkr.Button(root, text="View Shopping Cart", padx=20, pady=20, command=display_shopping_cart)
view_cart.grid(row=0, column=3)
# Create Customer Form
first_name_label = tkr.Label(root, bg="#FFFFFF", text="First name")  # First name label
first_name_label.grid(row=1, column=1)
first_name_field = tkr.Entry(root, bg="lightgray", width=btn_width)  # First name field
first_name_field.grid(row=2, column=1)
last_name_label = tkr.Label(root, bg="#FFFFFF", text="Last name")  # Last name label
last_name_label.grid(row=3, column=1)
last_name_field = tkr.Entry(root, bg="lightgray", width=btn_width)  # Last name field
last_name_field.grid(row=4, column=1)
# Items Gallery
item_1 = tkr.Button(root, text="Nintendo Switch", padx=btn_width, pady=btn_height,
                    command=lambda: add_item_to_cart(item1))
item_1.grid(row=8, column=0)
item_2 = tkr.Button(root, text="Playstation 5", padx=btn_width, pady=btn_height,
                    command=lambda: add_item_to_cart(item2))
item_2.grid(row=8, column=1)
item_3 = tkr.Button(root, text="Xbox Series X", padx=btn_width, pady=btn_height,
                    command=lambda: add_item_to_cart(item3))
item_3.grid(row=8, column=2)

root.mainloop()
