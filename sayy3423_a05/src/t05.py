"""
-------------------------------------------------------
Adding in a range
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-10-30"
-------------------------------------------------------
"""
# Imports
from functions import range_addition

#Variables and Display
start = int(input("Starting Number: "))
increment = int(input("Increment: "))
count = int(input("Count: "))
total = range_addition(start, increment, count)
print(f"The sum is {total}")
