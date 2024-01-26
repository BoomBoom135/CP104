"""
-------------------------------------------------------
Circle defined by a triangle
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-09-18"
-------------------------------------------------------
"""
# Imports
from functions import pythag

s1 = float(input("Side A: "))
s2 = float(input("Side B: "))

# Calls function to calculate the wanted variables and print
radius, diameter, circ, area = pythag(s1, s2)
print(
    f"\nRadius: {radius}\nDiameter: {diameter}\nCircumference: {circ}\nArea: {area}")
