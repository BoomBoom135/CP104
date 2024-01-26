"""
-------------------------------------------------------
Biggest Average
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-10-10"
-------------------------------------------------------
"""
# Imports
from functions import largest_average

# Variables
val1 = float(input("What is value 1?: "))
val2 = float(input("What is value 2?: "))
val3 = float(input("What is value 3?: "))

# Display
total = largest_average(val1, val2, val3)
print(f"\nThe sum of the largest values is {total}!")
