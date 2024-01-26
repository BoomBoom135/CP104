"""
-------------------------------------------------------
Calculating Celsius from Fahrenheit.
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-09-16"
-------------------------------------------------------
"""

#Calculation and Display
FREEZING = 32
Fahrenheit = int(input("Temperature (F): "))
Celsius = (Fahrenheit - FREEZING) * (5/9)
print("\nTemperature (C):", Celsius)
