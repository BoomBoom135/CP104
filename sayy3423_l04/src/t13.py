"""
-------------------------------------------------------
Fahrenheit to Celcius
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-09-18"
-------------------------------------------------------
"""
# Imports
from functions import f_to_c

fahrenheit = float(input("Fahrenheit: "))
celsius = f_to_c(fahrenheit)
print(f"Celsius: {celsius:.0f}")
