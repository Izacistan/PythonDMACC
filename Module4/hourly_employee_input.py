def hourly_employee_input():
    '''This function asks a user for their name,
    hours worked, and an hourly pay rate. At the end
    it prints a string including the information'''
    try:
        name = input("Please enter your name: ")
        hoursWorked = int(input("Please enter the hours you have worked: "))
        hourlyRate = float(input("Please enter your hourly pay rate: "))
        if hoursWorked < 0 or hourlyRate < 0:
            print("You entered a negative number!")
        else:
            print(name, hoursWorked, hourlyRate)
    except:
        print("Something went wrong! BYE.")

hourly_employee_input()