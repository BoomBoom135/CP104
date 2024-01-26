"""
-------------------------------------------------------
Code True or False
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-11-01"
-------------------------------------------------------
"""
# Imports
from functions import validate_code

#VAraibles and Display
product_code = input("Code: ")
category, digits, qualifiers = validate_code(product_code)
print(f"Category: {category}, Digits: {digits}, Qualifiers: {qualifiers}")
