"""
-------------------------------------------------------
Checking for sort
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-11-02"
-------------------------------------------------------
"""
# Imports
from functions import verify_sorted
from random import randint

#Variables and Display
numbers = []
for i in range(3):
    numbers.append(randint(1, 5))
in_order, index = verify_sorted(numbers)
print(f"Numbers: {numbers}")
print(f"Order: {in_order}, Index: {index}")
