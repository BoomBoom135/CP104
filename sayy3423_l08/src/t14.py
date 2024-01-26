"""
-------------------------------------------------------
Common values in both lists
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-10-31"
-------------------------------------------------------
"""
# Imports
from functions import intersection
from random import randint

#Variables and Display
n = int(input("How many numbers?: "))
low = int(input("Lowest: "))
high = int(input("Highest: "))

source1 = []
for a in range(1, n+1, 1):
    num = randint(low, high)
    source1.append(num)

source2 = []
for b in range(1, n+1, 1):
    num = randint(low, high)
    source2.append(num)

target = intersection(source1, source2)
print(f"Intersections: {target}")
