"""
-------------------------------------------------------
Customers Records
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-11-14"
-------------------------------------------------------
"""
# Imports
from functions import customer_record

#Variables and Display
fh = open("customers.txt", "r", encoding="utf-8")
n = int(input("Enter a Record Number: "))
result = customer_record(fh, n)
fh.close()
print(f"Results: {result}")
