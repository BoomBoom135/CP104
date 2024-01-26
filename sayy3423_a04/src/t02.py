"""
-------------------------------------------------------
Pollution Ranks
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-10-10"
-------------------------------------------------------
"""
# Imports
from functions import pollution_ranking

#Variables and Display
air_quality_index = float(input("What is the Pollution Index?: "))
air = pollution_ranking(air_quality_index)
print(f"\nThe air quality is {air}!")
