"""
    AUTHOR: Isaac Hillaker
    DATE: 01/09/2023
    This program takes in user data to create a customer. After a customer has been created, the program calculates (based on the customer's given age)
    how much their quote will cost. The cost of the coverage increases by 41% if the customer has been in a car accident before. The price of coverage
    gets smaller as the customer's age increases.
"""
# Declare lists, dictionaries, and variables.
customer_dict = {"001": ["Isaac", "Hillaker", 26, "F"]}
coverage_options = ["SM", "L", "F"]
coverage_prices = {"SM": [2593, 608, 552, 525, 494, 515],
                   "L": [2957, 691, 627, 596, 560, 585],
                   "F": [6930, 1745, 1564, 1469, 1363, 1402]}


# DEFINE FUNCTIONS
def create_customer():
    """
    This function takes user input, validates the input,
    and adds the customer to the customer_dict dictionary.
    """

    global last_name, first_name, age, customer_coverage_price
    customer_coverage_price = 0  # initial value of 0, changed later in function depending on customer's age.
    def invalid_name_input_error():
        """Displays an error message when a user enters invalid data in the first or last name fields."""
        error_msg = "Name can only contains letters and ' - '. Please try again."
        print(error_msg)

    #Get and validate user input
    name_characters = set(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")  # Characters users may enter in both the first and last name fields.


    # get FIRST and LAST name and VALIDATE info.
    while True:
        first_name = input("Type your first name: ")
        last_name = input("Type your last name: ")
        if len(first_name.strip()) == 0 or len(
                last_name.strip()) == 0:  # Makes sure users can't enter NO data or BLANK data.
            invalid_name_input_error()
        elif not (name_characters.issuperset(last_name) and name_characters.issuperset(
                first_name)):  # Validate user input against 'name_characters'. Returns and error if given user data is bad.
            invalid_name_input_error()
        else:
            break

    # get AGE and VALIDATE that is an integer and that it is 16 or higher.
    while True:
        try:
            while True:
                age = int(input("Enter your age. You must be at least 16 years old: "))
                if age < 16:
                    print("Must be 16 or older.")
                else:
                    break
        except ValueError:
            print("Invalid data. Please try again, entering only numbers.")
            continue
        else:
            break

    # get coverage type from user and validate.
    while True:
        desired_coverage = input("Type your preferred coverage level (SM, L, or F): ")
        desired_coverage = desired_coverage.upper()  # Converts desired_coverage variable to caps, accounting for user entering in lowercase options.
        if desired_coverage not in coverage_options:
            print("Data not valid. Please try again entering SM, L, or F.")
        else:
            break  # Leave the inner loop of the try/except statements.

    # calculate costs for ages 16-24.
    if 16 <= age <= 24:
        if desired_coverage == "SM":
            price = coverage_prices["SM"]
            customer_coverage_price = price[0]
        elif desired_coverage == "L":
            price = coverage_prices["L"]
            customer_coverage_price = price[0]
        else:
            price = coverage_prices["F"]
            customer_coverage_price = price[0]

    # calculate costs for ages 25-34.
    if 25 <= age <= 34:
        if desired_coverage == "SM":
            price = coverage_prices["SM"]
            customer_coverage_price = price[1]
        elif desired_coverage == "L":
            price = coverage_prices["L"]
            customer_coverage_price = price[1]
        else:
            price = coverage_prices["F"]
            customer_coverage_price = price[1]

    # calculate costs for ages 35-44.
    if 35 <= age <= 44:
        if desired_coverage == "SM":
            price = coverage_prices["SM"]
            customer_coverage_price = price[2]
        elif desired_coverage == "L":
            price = coverage_prices["L"]
            customer_coverage_price = price[2]
        else:
            price = coverage_prices["F"]
            customer_coverage_price = price[2]

    # calculate costs for ages 45-54.
    if 45 <= age <= 54:
        if desired_coverage == "SM":
            price = coverage_prices["SM"]
            customer_coverage_price = price[3]
        elif desired_coverage == "L":
            price = coverage_prices["L"]
            customer_coverage_price = price[3]
        else:
            price = coverage_prices["F"]
            customer_coverage_price = price[3]

    # calculate costs for ages 55-64.
    if 55 <= age <= 64:
        if desired_coverage == "SM":
            price = coverage_prices["SM"]
            customer_coverage_price = price[4]
        elif desired_coverage == "L":
            price = coverage_prices["L"]
            customer_coverage_price = price[4]
        else:
            price = coverage_prices["F"]
            customer_coverage_price = price[4]

    # calculate costs for aged 65+.
    if age > 65:
        if desired_coverage == "SM":
            price = coverage_prices["SM"]
            customer_coverage_price = price[5]
        elif desired_coverage == "L":
            price = coverage_prices["L"]
            customer_coverage_price = price[5]
        else:
            price = coverage_prices["F"]
            customer_coverage_price = price[5]

    # Add new customer data to customer dictionary.
    customer_dict.update({"002": [first_name, last_name, age, desired_coverage, customer_coverage_price]})
    return customer_dict  # Last line of create_customer() function


def calc_final_quote():
    """
    This function checks if a customer has been involved in a car accident. If they have, then their coverage cost is increased by 41%.
    Otherwise, their price does not change. The function then updates the previous coverage cost in the customer's list, in the cust_dictionary.
    """
    customer = customer_dict["002"] #automatically created by the create_customer() function. In a real world program I would make a new, unique key everytime.
    # adjust coverage price if customer has been involved in an accident before.
    while True:
        try:
            has_accidents = input("Have you ever been involved in a car accident? Type Y or N: ")
            has_accidents = has_accidents.upper()
            if has_accidents == "Y":
                final_price = customer_coverage_price * 0.41 + customer_coverage_price # price increases by 41% if customer answered YES.
                customer[4] = final_price  # add final price to list within customer_dict
                print(f"Your quote is: ${final_price}")
                break
            elif has_accidents == "N":
                final_price = customer_coverage_price
                customer[4] = final_price  # add final price to list within customer_dict
                print(f"Your quote is: ${final_price}")
                break
            else:
                print("Try again. Type Y or N.")
        except TypeError:
            print("You entered invalid data, please try again.")


# DRIVER CODE
create_customer()
print(customer_dict)
calc_final_quote()
print(customer_dict)
