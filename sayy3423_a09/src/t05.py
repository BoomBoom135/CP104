"""
-------------------------------------------------------
Stats for students
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-11-26"
-------------------------------------------------------
"""
# Imports
from functions import student_stats

#Variables and Display
file_handle = open("students.txt" ,"r", encoding = "utf-8")
l_id, h_id, avg = student_stats(file_handle)
file_handle.close()
print(f"Id Lowest: {l_id}")
print(f"Id Highest: {h_id}")
print(f"Average: {avg}")
