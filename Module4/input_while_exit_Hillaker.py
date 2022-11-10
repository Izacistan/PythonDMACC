#Part 1
# list1 = []
# specialNumber = int(input("Please type in a number between 1 and 100: "))
#
# while specialNumber not in range(1, 101):
#     specialNumber = int(input("The number you typed is out of range. Please type in a number between 1 and 100: "))
#
# list1.append(specialNumber)
# print("You did it!")
# for x in list1:
#     print(x)

#Part 2
list2 = []
sentinel = 42
specialNumber2 = int(input("Please enter a number between 1 and 100 (If you would like to stop the program type 42): "))

while specialNumber2 != sentinel:
    while specialNumber2 not in range(1, 101):
        specialNumber2 = int(input("You entered a number out of range. Please enter a number between 1 and 100 "
                                       "(If you would like to stop the program type 42): "))
    list2.append(specialNumber2)
    print("Variable stored in list!")
    specialNumber2 = int(input("Enter another value between 1 and 100 (Or type 42 to exit the program): "))

print("You exited the loop!")
for y in list2:
    print(y)