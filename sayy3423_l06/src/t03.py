"""
-------------------------------------------------------
Sums from start to finish
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-10-07"
-------------------------------------------------------
"""
# Imports
from functions import sum_all

# Needed varaibles fromuser
start = int(input("What is the start?: "))
finish = int(input("What is the finish?: "))
increment = int(input("What is the increment?: "))

# Output for user
total = sum_all(start, finish, increment)
print(f"\nSum = {total}")
