"""
-------------------------------------------------------
Multiplying fraction with functions
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-09-21"
-------------------------------------------------------
"""
# Imports
from functions import multiply_fractions

# Variables from user
num1 = float(input("What is numerator 1?: "))
den1 = float(input("What is denominator 1?: "))
num2 = float(input("What is numerator 2?: "))
den2 = float(input("What is denominator 2?: "))

num, den, product = multiply_fractions(num1, den1, num2, den2)
print(f"\nResult: {num}, {den}, {product}")
