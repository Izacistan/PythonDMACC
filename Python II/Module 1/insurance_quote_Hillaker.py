"""
    AUTHOR: Isaac Hillaker
    DATE: 01/09/2023
    This program takes in user data and gives back a quote for auto insurance based on that data.
    .
"""
# Declare lists, dictionaries, and variables.
customer_dict = {}
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

    global last_name, first_name, age

    def invalid_name_input_error():
        """Displays an error message when a user enters invalid data in the first or last name fields."""
        error_msg = "Name can only contains letters and ' - '. Please try again."
        print(error_msg)

    # 1) Gather User Input
    # 2) Try/Except User Input Validation
    name_characters = set(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")  # Characters users may enter in both the first and last name fields.

    while True:  # get FIRST and LAST name and VALIDATE info.
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

    while True:  # get AGE and VALIDATE that is an integer and that it is 16 or higher.
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

    while True:  # get coverage type from user and validate.
        desired_coverage = input("Type your preferred coverage level (SM, L, or F): ")
        desired_coverage = desired_coverage.upper()  # Converts desired_coverage variable to caps, accounting for user entering in lowercase options.
        if desired_coverage not in coverage_options:
            print("Data not valid. Please try again entering SM, L, or F.")
        else:
            break  # Leave the inner loop of the try/except statements.

    # Add new customer data to customer dictionary.
    customer_dict.update({"001": [first_name, last_name, age, desired_coverage]})
    return customer_dict  # Last line of create_customer() function


# 4) Add the customer’s coverage cost to the dictionary value according to their age and coverage desired using the table above

# 5): Ask the user if they've had any accidents
# If the user has had any accidents, their coverage rate increases by 41%
# Update the customer’s coverage cost in the dictionary

# 6): Output the annual insurance cost for the customer

# 7): Ensure that you have docstring at the top of your program with your name/date/program information

# DRIVER CODE
create_customer()
print(customer_dict)
