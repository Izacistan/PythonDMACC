def hourly_employee_input():
    '''This function asks a user for their name,
    hours worked, and an hourly pay rate. At the end
    it returns a name and a weekly pay rate. '''
    def weekly_pay(hours_worked, hourly_pay_rate):
        return hours_worked * hourly_pay_rate
    try:
        name = input("Please enter your name: ")
        hours_worked = int(input("Please enter the hours you have worked: "))
        hourly_rate = float(input("Please enter your hourly pay rate: "))

        if hours_worked < 0 or hourly_rate < 0:
            print("You entered a negative number!")
        else:
            weekly_pay(hours_worked, hourly_rate)
    except:
        print("Exception occurred.")
    else:
        return weekly_pay(hours_worked, hourly_rate)

if __name__ == '__main__':
    try:  # check for ValueError
        display_string = hourly_employee_input()
    except ValueError as err:
        print("ValueError encountered! ")
    else:
        print(display_string)
