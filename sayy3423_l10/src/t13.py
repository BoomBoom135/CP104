"""
-------------------------------------------------------
Copy file
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-11-23"
-------------------------------------------------------
"""
# Imports
from functions import file_copy

#Variables in Display
fh_1 = open("words.txt", "r", encoding="utf-8")
fh_2 = open("new_words.txt", "w", encoding="utf-8")
file_copy(fh_1, fh_2)
fh_1.close()
fh_2.close()
