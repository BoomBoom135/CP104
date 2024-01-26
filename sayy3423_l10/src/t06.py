"""
-------------------------------------------------------
Number statistics
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-11-14"
-------------------------------------------------------
"""
# Imports
from functions import number_stats

#FVariables and Display
fh = open("numbers.txt", "r", encoding="utf-8")
smallest, largest, total, average = number_stats(fh)
fh.close()
print(
    f"Smallest: {smallest}\nLargest: {largest}\nTotal: {total:.2f}\nAverage: {average:.2f}")
