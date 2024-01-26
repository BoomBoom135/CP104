"""
-------------------------------------------------------
Generate Matrix
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-11-27"
-------------------------------------------------------
"""
# Imports
from functions import generate_matrix_num

#Variables and Display
rows = int(input("Rows: "))
cols = int(input("Columns: "))
low = int(input("Low: "))
high = int(input("High: "))
value_type = input("int or float: ")
matrix = generate_matrix_num(rows, cols, low, high, value_type)
for item in matrix:
    print(f"{item}")
