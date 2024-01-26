"""
-------------------------------------------------------
Calculating Slope
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-09-18"
-------------------------------------------------------
"""
# Imports
from functions import slope

# collects variables, calls function, and displays slope
x1 = float(input("What is x1: "))
y1 = float(input("What is y1: "))
x2 = float(input("What is x2: "))
y2 = float(input("What is y2: "))
slp = slope(x1, y1, x2, y2)

print(f"\nSlope = {slp}")
