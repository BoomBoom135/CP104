"""
-------------------------------------------------------
Lumber calculations
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-10-08"
-------------------------------------------------------
"""
# Imports
from functions import lumber

# Variables
b_min = int(input("Base minimum: "))
b_max = int(input("Base maximum: "))
b_inc = int(input("Base increment: "))
h_min = int(input("Height minimum: "))
h_max = int(input("Height maximum: "))
h_inc = int(input("Height increment: "))

# Calls function for display
lumber(b_min, b_max, b_inc, h_min, h_max, h_inc)
