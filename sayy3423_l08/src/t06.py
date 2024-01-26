"""
-------------------------------------------------------
Statistic returns
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-10-31"
-------------------------------------------------------
"""
# Imports
from functions import list_stats
from random import randint

#Variables and Display
values = []
n = int(input("How many numbers?: "))
low = int(input("Lowest: "))
high = int(input("Highest: "))
for i in range(1, n+1, 1):
    num = randint(low, high)
    values.append(num)
smallest, largest, total, average = list_stats(values)
print(
    f"Smallest: {smallest}, Largest: {largest}, Total: {total}, Average: {average}")
