"""
-------------------------------------------------------
Wind Speed
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-09-27"
-------------------------------------------------------
"""
# Imports
from functions import wind_speed

speed = float(input("What is the wind speed?: "))
cat = wind_speed(speed)

print(f"The category is: {cat}")
