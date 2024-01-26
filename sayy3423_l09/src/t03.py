"""
-------------------------------------------------------
3 parts of string
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-11-01"
-------------------------------------------------------
"""
# Imports
from functions import parse_code

#Variables and Display
product_code = input("Code: ")
pc, pi, pq = parse_code(product_code)
print(f"PC: {pc}, PI: {pi}, PQ: {pq}")
