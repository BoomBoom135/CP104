"""
-------------------------------------------------------
Money/Retirement Calculation
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-10-08"
-------------------------------------------------------
"""
# Imports
from functions import retirement

# Variables
age = int(input("What is your current age?: "))
salary = float(input("What is your salary?: "))
increase = float(input("What is your percent increase?: "))

# Calling function and display
retirement(age, salary, increase)
