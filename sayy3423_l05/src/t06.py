"""
-------------------------------------------------------
Checking for divisibility
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-09-27"
-------------------------------------------------------
"""
# Imports
from functions import is_divisible

# Number variables
n = int(input("What number are you dividing by?: "))
i = int(input("What is the first number?: "))
j = int(input("What is the second number?: "))

print(is_divisible(n, i, j))
