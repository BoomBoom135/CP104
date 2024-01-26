"""
-------------------------------------------------------
Calculating Interest
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-10-31"
-------------------------------------------------------
"""
# Imports
from functions import interest_table
principal_amount = float(input(f"Principal: $"))
interest_rate = float(input("Interest Rate: "))
payment = float(input(f"Monthly Payments: $"))
interest_table(principal_amount, interest_rate, payment)
