"""
-------------------------------------------------------
Count of characters
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-11-25"
-------------------------------------------------------
"""
# Imports
from functions import file_statistics

#Variables and Display
file_handle = open("addresses.txt", "r", encoding="utf-8")
ucount, lcount, dcount, wcount, rcount = file_statistics(file_handle)
file_handle.close()
print(f"Uppers: {ucount}")
print(f"Lowers: {lcount}")
print(f"Digits: {dcount}")
print(f"Spaces: {wcount}")
print(f"Others: {rcount}")
