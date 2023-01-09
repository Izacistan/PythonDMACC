# 1) Gather User Input
# Age (integer)
# Name (string)
# Coverage Level (string (SM, L, F))
def create_customer():
    """This function takes user input, validates the input,
    and adds the customer to the customer_dict dictionary."""

    global last_name, first_name, age

    def invalid_name_input_error():
        """Displays an error message when a user enters invalid data in the first or last name fields."""
        error_msg = "Name can only contains letters and ' - '. Please try again."
        print(error_msg)

    # 2) Try/Except User Input Validation
    # Gets FIRST and LAST names from user. Validates data.
    name_characters = set(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")  # Characters users may enter in both the first and last name fields.
    # Validate name input
    while True:
        try:
            while True:
                first_name = input("Type your first name: ")
                last_name = input("Type your lastname: ")
                age = int(input("Enter your age. You must be at least 16 years old: "))

                if len(first_name.strip()) == 0 or len(
                        last_name.strip()) == 0:  # Makes sure users can't enter NO data or BLANK data.
                    invalid_name_input_error()
                elif not (name_characters.issuperset(last_name) and name_characters.issuperset(
                        first_name)):  # Validate user input against 'name_characters'. Returns and error if given user data is bad.
                    invalid_name_input_error()
                elif age < 16: # Make sure user is at least 16 years old.
                    print("You must be at least 16 years old to get a quote.")
                else:
                    break # Leave the inner loop of the try/except statements.
        except ValueError:
            print("You entered bad data. Please try again.") # This is triggered by the age variable containing letters instead of numbers.
            continue
        else:
            break # Leave the main loop of the try/except statements.


    return first_name, last_name, age



# 3) Store the above information in a dictionary (you could have an ID be the key and the value be a list of attributes [drivername,driverage,coverage])

# 4) Add the customer’s coverage cost to the dictionary value according to their age and coverage desired using the table above

# 5): Ask the user if they've had any accidents
# If the user has had any accidents, their coverage rate increases by 41%
# Update the customer’s coverage cost in the dictionary

# 6): Output the annual insurance cost for the customer

# 7): Ensure that you have docstring at the top of your program with your name/date/program information

# DRIVER CODE
print(create_customer())
