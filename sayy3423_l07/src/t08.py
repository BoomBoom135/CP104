"""
-------------------------------------------------------
Calculating budget
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-10-30"
-------------------------------------------------------
"""
# Imports
from functions import budget

#Variable and Display
available = float(input(f"Budget: $"))
expenses, balance, status = budget(available)
print(f"{expenses} in expenses, {balance} in balance...status: {status}")
