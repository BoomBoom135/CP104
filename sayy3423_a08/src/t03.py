"""
-------------------------------------------------------
Same endings
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-11-23"
-------------------------------------------------------
"""
# Imports
from functions import common_end

#Variables and Display
str1 = input("String 1: ")
str2 = input("String 2: ")
suffix = common_end(str1, str2)
print(f'Longest: {suffix}')
