"""
-------------------------------------------------------
Frequency counting
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-11-23"
-------------------------------------------------------
"""
# Imports
from functions import count_frequency_word

#Variables and Display
fh = open("words.txt", "r", encoding="utf-8")
word = input("Word to count: ")
count = count_frequency_word(fh, word)
fh.close()
print(f"'{word}' appears {count} time(s)")
