"""
-------------------------------------------------------
Locating the Quadrant
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-09-27"
-------------------------------------------------------
"""
# Imports
from functions import quadrant

# x and y variables
x = float(input("What is the x?: "))
y = float(input("What is the y?: "))

print("The location is the", quadrant(x, y))
