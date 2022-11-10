'''

Author: Isaac Hillaker
Date last modified: 09/12/2022

This program runs as if you are buying something from a website. You are given a dollar coupon and a percetage coupon.
Depending on how much your item's discounted price is, your shipping is either low, higher, or free.
Tax is calculated after all other numbers are figured out.

'''

#Declare and initialize CONST variables.

#Shipping benchmark numbers to create ranges for calculating shipping costs.
SHIP_TIER_1 = 10.00
SHIP_TIER_2 = 30.00
SHIP_TIER_3 = 50.00
#Shipping costs
SHIP_COST_1 = 5.95
SHIP_COST_2 = 7.95
SHIP_COST_3 = 11.95
SHIP_COST_4 = 0.00
#Tax rate
TAX = 0.06
#Cash Coupon variables
CASH_COUPON_1 = 5.00
CASH_COUPON_2 = 10.00
dollarCoupon = 0.00

#Percetange coupon variables
PER_1 = 0.10
PER_2 = 0.15
PER_3 = 0.30
percentCoupon = 0.00
#Spacer variable for readability upon printing.
space = " "

#Give instructions and get user input.
purchaseAmount = float(input("Please type in your purchase amount and exclude dollar signs: "))
print(space)

#CASH COUPON INPUT
print(f"You may apply a ${CASH_COUPON_1} or ${CASH_COUPON_2} coupon to this purchase.")
print(space)
while not (dollarCoupon == CASH_COUPON_1 or dollarCoupon == CASH_COUPON_2):
    dollarCoupon = float(input(f"Enter a {CASH_COUPON_1} or a {CASH_COUPON_2}: "))

#PERCENTAGE COUPON INPUT
print(f"You may apply a {PER_1}%, {PER_2}%, or {PER_3}% discount to this purchase.")
print(space)
while not (percentCoupon == PER_1 or percentCoupon == PER_2 or percentCoupon == PER_3):
    percentCoupon = float(input(f"Enter {PER_1}, {PER_2}, or {PER_3}: "))


#MATH OPERATIONS
#Get discounted price after coupons applied.
discountPrice = purchaseAmount - dollarCoupon
perDiscount = discountPrice * percentCoupon
discountAmount = perDiscount + dollarCoupon
discountPrice = discountPrice - perDiscount
discountAmount = round(discountAmount, 2)
discountPrice = round(discountPrice, 2)

#Calculate Shipping
if discountPrice < SHIP_TIER_1:
    shipping = SHIP_COST_1
    total = discountPrice + SHIP_COST_1
    total = round(total, 2)
elif SHIP_TIER_1 <= discountPrice < SHIP_TIER_2 and discountPrice != SHIP_TIER_2:
    shipping = SHIP_COST_2
    total = discountPrice + SHIP_COST_2
elif SHIP_TIER_2 <= discountPrice < SHIP_TIER_3 and discountPrice != SHIP_TIER_3:
    shipping = SHIP_COST_3
    total = discountPrice + SHIP_COST_3
else:
    shipping = SHIP_COST_4
    total = discountPrice + SHIP_COST_4

#Calculate TAX
taxAmount = total * TAX
taxAmount = round(taxAmount, 2)
grandTotal = total + taxAmount

#Display all numbers before added up
print(space)
print("ITEM COST: " + "$" + str(purchaseAmount))
print("DISCOUNT: " + "-$" + str(discountAmount))
print("NEW PRICE: " + "$" + str(discountPrice))
print("SHIPPING: " + "+$" + str(shipping))
print("TAX: "+ "+$" + str(taxAmount))
print("SUBTOTAL: " + "$" + str(total))

#Format 'grandTotal' to two decimal places and OUPUT 'grandTotal'.
grandTotal = round(grandTotal, 2)
print("GRAND TOTAL: " + "$" + str(grandTotal))