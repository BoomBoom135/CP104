"""
-------------------------------------------------------
find smallest and biggest
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-11-27"
-------------------------------------------------------
"""
# Imports
from functions import find_position
from random import randint
from random import uniform

#Variables and Display
rows = int(input("Rows: "))
cols = int(input("Columns: "))
low = int(input("Low: "))
high = int(input("High: "))
value_type = input("int or float: ")
matrix = []
for a in range(rows):
    list = []
    for b in range(cols):
        if value_type == "float":
            num = uniform(low,high)
        elif value_type == "int":
            num = randint(low,high)
        else:
            continue
        list.append(num)
    matrix.append(list)
s_loc, l_loc = find_position(matrix)
print(f"Smallest: {s_loc}")
print(f"Largest: {l_loc}")
