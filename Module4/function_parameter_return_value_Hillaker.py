def multiply_string(message, n):
    try:
        if n < 2 or n > 7:
            print("Incorrect value.")
        else:
            return message * n
    except:
        print("An Exception occurred.")


if __name__ == '__main__':
    try:  # check for ValueError
        display_string = multiply_string("Hello ", 4)
    except ValueError as err:
        print("ValueError encountered! ")
    else:
        print(display_string)
