"""
-------------------------------------------------------
Index findings
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-11-01"
-------------------------------------------------------
"""
# Imports
from functions import get_indexes
from random import randint

#Variables and Display
low = int(input("Low: "))
high = int(input("High: "))
nums = int(input("Amount of Numbers: "))
numbers = []
for i in range(nums):
    rand = randint(low, high)
    numbers.append(rand)
target_number = int(input("Number to find: "))
index_list = get_indexes(numbers, target_number)
print(f"Indexes: {index_list}")
