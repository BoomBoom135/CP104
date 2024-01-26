"""
-------------------------------------------------------
Analyzing text
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-11-01"
-------------------------------------------------------
"""
# Imports
from functions import text_analyze

#Variables and Display
txt = input("Enter Text: ")
uppr, lowr, dgts, whtspc = text_analyze(txt)
print(f"Upper: {uppr}, Lower: {lowr}, Digits: {dgts}, Whitespaces: {whtspc}")
