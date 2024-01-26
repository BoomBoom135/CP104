"""
-------------------------------------------------------
Formatting the Date 
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-09-14"
-------------------------------------------------------
"""
dateSet = int(input("Enter a date in the format YYYYMMDD: "))

# Calculates each time slot
day = dateSet % 100
month = dateSet // 100 % 100
year = dateSet // 10000

print(f"\nThe reformatted date: {year}/{month}/{day}")
