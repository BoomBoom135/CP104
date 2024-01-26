"""
-------------------------------------------------------
Hi and Low Game
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-10-19"
-------------------------------------------------------
"""
# Imports
from functions import hi_lo_game

#Variables and Print
high = int(input("Give a High Value: "))
count = hi_lo_game(high)
print(f"You made {count} guesses.")
