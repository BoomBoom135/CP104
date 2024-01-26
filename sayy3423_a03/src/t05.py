"""
-------------------------------------------------------
Falling Distance
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-09-21"
-------------------------------------------------------
"""
# Imports
from functions import falling_distance

time = int(input("How long was the fall(seconds)?: "))
distance = falling_distance(time)
print(f"The total Distance fell was: {distance} meters")
