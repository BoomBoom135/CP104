"""
-------------------------------------------------------
Find Number in List
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-10-31"
-------------------------------------------------------
"""
# Imports
from functions import many_search
from random import randint

#Variables and Display
values = []
n = int(input("How many numbers?: "))
low = int(input("Lowest: "))
high = int(input("Highest: "))
for i in range(1, n+1, 1):
    num = randint(low, high)
    values.append(num)
value = int(input("Value Search: "))
indexes = many_search(values, value)
print(f"Indexes: {indexes}")
