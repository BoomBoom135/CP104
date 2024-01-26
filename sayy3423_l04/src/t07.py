"""
-------------------------------------------------------
Calculating Change
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-09-18"
-------------------------------------------------------
"""
# Imports
from functions import total_change

nickels = int(input("Nickels: "))
dimes = int(input("Dimes: "))
quarters = int(input("Quarters: "))
loonies = int(input("Loonies: "))
toonies = int(input("Toonies: "))

# Calls function to add up and display for user
total = total_change(nickels, dimes, quarters, loonies, toonies)
print(f"\nTotal: ${total:.2f}")
