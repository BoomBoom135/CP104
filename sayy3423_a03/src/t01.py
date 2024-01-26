"""
-------------------------------------------------------
Calculating footage to acres using a function
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-09-21"
-------------------------------------------------------
"""
# Imports
from functions import footage_to_acres

# Get variable for calculation and Display
footage = float(input("What is the Footage: "))
acres = footage_to_acres(footage)
print(f"The amount of acres are: {acres:.3f}")
