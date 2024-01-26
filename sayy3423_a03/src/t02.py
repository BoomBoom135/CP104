"""
-------------------------------------------------------
Speed to cut grass
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-09-21"
-------------------------------------------------------
"""
# Imports
from functions import lawn_mow_time

# Variables from user
width = float(input("What is the Width?: "))
length = float(input("What is the Length?: "))
speed = int(input("What is the Speed?: "))

time = lawn_mow_time(width, length, speed)
print(f"The time it will take in minutes is: {time:.1f}")
