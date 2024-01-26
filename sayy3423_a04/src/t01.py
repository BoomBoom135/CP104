"""
-------------------------------------------------------
Day of the week
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-10-10"
-------------------------------------------------------
"""
# Imports
from functions import day_name

#Variables and Display
day_num = int(input("What is the day(1-7)?: "))
day = day_name(day_num)
print(f"\nThe day is {day}!")
