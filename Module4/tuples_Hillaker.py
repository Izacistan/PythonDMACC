'''
AUTHOR: Isaac Hillaker

This program takes a student's name and an unknown number
of test scores, stores them in a tuple, saves that tuple
into a file, and then finally prints the data from the
file back to the screen.
'''


# FUNCTIONS
def write_to_file(file, *args):
    with open(file, "w") as file:
        for t in args:
            file.write(' '.join(str(s) for s in t) + '\n')


def get_student_info(name):
    scoreTuple = (name, [])
    score = 0
    SENTINEL = -99
    while score != SENTINEL:
        score = int(input("Add a score (type -99 to exit loop): "))
        scoreTuple[1].append(score)
    write_to_file("student_info.txt", studentScores)


def read_from_file(file):
    with open(file, "r") as file:
        print(file.read())


# Run Program
get_student_info("Alice")

read_from_file("student_info.txt")
print("Program executed!")
