"""
-------------------------------------------------------
Color Identity
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-10-10"
-------------------------------------------------------
"""
# Imports
from functions import colour_combine

# Variables
rgb_colour1 = input("What is color 1?: ")
rgb_colour2 = input("What is color 2?: ")

# Display
colour = colour_combine(rgb_colour1, rgb_colour2)
print(f"\n{rgb_colour1} + {rgb_colour2} = {colour}")
