def main():
    print("In main")

if __name__ == "__main__":
        main()

def get_user_input():
    '''Prompts the user for a name and age, and prints a message'''
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))
    print(name, "", age, " years old.")

if __name__ == "__main__":
    try:
        get_user_input()
    except ValueError as err:
        print("ValueError encountered!")

