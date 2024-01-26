"""
-------------------------------------------------------
Calorie Calculation
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-10-30"
-------------------------------------------------------
"""
# Imports
from functions import calories_treadmill

#Variables and Display
per_min = float(input("Number of calories per minute: "))
minutes = int(input("Number of minutes: "))
calories_treadmill(per_min, minutes)
