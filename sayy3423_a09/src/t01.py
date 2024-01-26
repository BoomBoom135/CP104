"""
-------------------------------------------------------
Specific lines
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-11-25"
-------------------------------------------------------
"""
# Imports
from functions import file_top

#Variables and Display
file_handle = open("students.txt", "r", encoding="utf-8")
count = int(input("Lines: "))
file_top(file_handle, count)
file_handle.close()
