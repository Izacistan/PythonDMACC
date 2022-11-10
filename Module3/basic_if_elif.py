'''
author: Isaac Hillaker
last date modified: 09/08/2022

This program takes input in the form of strings.

It is looking for a 'rank' to be chosen, then using
if/elif statements print the correct price for the corresponding rank.
'''

txt = "The price is: "

memberLevel = input("Please type in your preferred membership level for the Programmer's "
      "Toolkit Monthly subscription box!\n Type one of the following: Platinum, "
      "Gold, Silver, Bronze, or Free Trial.").upper()



if memberLevel == "PLATINUM":
    print(f"{txt}$60.")
elif memberLevel == "GOLD":
    print(f"{txt}$50")
elif memberLevel == "SILVER":
    print(f"{txt}$40")
elif memberLevel == "BRONZE":
    print(f"{txt}$30")
else:
    print("The Free Trial is free!")