"""
-------------------------------------------------------
Positive integers
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-11-25"
-------------------------------------------------------
"""
# Imports
from functions import read_integers

#Variables and Display
file_handle = open("numbers.txt", "r", encoding = "utf-8")
number_list = read_integers(file_handle)
file_handle.close()
print(f"Numbers: {number_list}")
