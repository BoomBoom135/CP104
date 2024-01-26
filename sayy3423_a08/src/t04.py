"""
-------------------------------------------------------
Check valid
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-11-24"
-------------------------------------------------------
"""
# Imports
from functions import valid_isbn

#Variables and Display
isbn = input("Enter: ")
is_valid = valid_isbn(isbn)
print(f"Result: {is_valid}")
