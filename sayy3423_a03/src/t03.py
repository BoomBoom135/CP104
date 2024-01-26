"""
-------------------------------------------------------
Splitting Date
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-09-21"
-------------------------------------------------------
"""
# Imports
from functions import extract_date

# Variable to Split date and Display
date_number = int(input("What is the date?: "))
year, month, day = extract_date(date_number)
print(f"The date is: {year}, {month}, {day}")
