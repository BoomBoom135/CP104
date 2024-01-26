"""
-------------------------------------------------------
Finding longest word
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-11-16"
-------------------------------------------------------
"""
# Imports
from functions import find_longest

#Variables and Display
fh = open("words.txt", "r", encoding="utf-8")
word = find_longest(fh)
fh.close()
print(f"'{word}' is the last longest word")
