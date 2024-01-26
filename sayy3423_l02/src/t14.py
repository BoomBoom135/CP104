"""
-------------------------------------------------------
Different Servings for 6
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-09-16"
-------------------------------------------------------
"""

# Constant for serving of 6
MILKC = 4
BUTTERC = 8
FLOURC = 0.5
SALTC = 2
SERVING_SIZE = 6

SERVS = int(input("Enter servings of Mac & Cheese: "))
SERVINGS = SERVS / SERVING_SIZE

# Calculations for servings
milkF = (MILKC * SERVINGS)
butterF = (BUTTERC * SERVINGS)
flourF = (FLOURC * SERVINGS)
saltF = (SALTC * SERVINGS)

# Display for user
print(SERVS, "servings of Mac & Cheese requires:")
print("milk (cups):", milkF)
print("butter (tablespoons):", butterF)
print("flour (cups):", flourF)
print("salt (teaspoons):", saltF)
