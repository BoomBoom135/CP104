"""
-------------------------------------------------------
Remove target
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-11-09"
-------------------------------------------------------
"""
# Imports
from functions import list_subtract
from random import randint

#variables and Display
'''
low = int(input("Low: "))
high = int(input("High: "))
nums = int(input("Amount of Numbers: "))
minuend = []
for i in range(nums):
    rand = randint(low, high)
    minuend.append(rand)
subtrahend = []
subtrahend.append(int(input("Target: ")))
'''
minuend = [5, 5, 4, 5]
subtrahend = [5]
list_subtract(minuend, subtrahend)

print(minuend)
