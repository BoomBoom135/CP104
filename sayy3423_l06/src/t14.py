"""
-------------------------------------------------------
Marketing Ia's
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-10-08"
-------------------------------------------------------
"""
# Imports
from functions import ia_hours

ia_count = int(input("Number of IA's: "))

total_hours = ia_hours(ia_count)

print(f"\nTotal Hours: {total_hours:.2f}")
