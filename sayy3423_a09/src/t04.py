"""
-------------------------------------------------------
Finding Passage
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-11-25"
-------------------------------------------------------
"""
# Imports
from functions import line_numbering

#Variables and Display
fh_read = open("wilde.txt", "r", encoding = "utf-8")
fh_write = open("wilde_numbered.txt", "w", encoding = "utf-8")
line_numbering(fh_read, fh_write)
fh_read.close()
fh_write.close()
