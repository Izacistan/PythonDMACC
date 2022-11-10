"""
Program: average_scores.py
Author: Isaac Hillaker
Last date modified: 09/08/2022

This program takes user input in the form of 1) last and first names, 2) age,
and 3) three seperate scores. The program then takes the three scores and finds
the average. At the end, the program prints the output in an organized manner,
with the inputted names and age, as well as the average score.
"""

# Declare/initialize constant and empty variables.
NUM_OF_SCORES = 3  # constant variable.
score_total = 0
score_average = 0

# Get user INPUT
last_name = input("Please type in your LAST name...")
first_name = input("Please type in your FIRST name...")
age = int(input("Using numbers only, please type in your age..."))

# Collect SCORES and convert to INTEGERS.
score1 = int(input("Using numbers only, please type your first score..."))
score2 = int(input("Using numbers only, please type your second score..."))
score3 = int(input("Using numbers only, please type your third score..."))

# Calculate AVERAGE SCORE
score_total = score1 + score2 + score3
score_average = round(score_total / NUM_OF_SCORES, 2)  # round to higher decimal point.
print(score_average)

# PRINT output
print(f"{last_name}, {first_name} age: {age} average grade: {score_average}")

'''
If the user inputs everything correctly, then
there are no errors and the program runs as expected.

If the user inputs a number when a string is expected, an error is thrown.

If the user inputs a string when an integer is expected, an error is thrown.
'''