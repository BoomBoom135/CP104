"""
-------------------------------------------------------
Calculates Paycheck by salary and hours
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-09-16"
-------------------------------------------------------
"""

# Pay and Hour input, calculation, and display
Pay = float(input("Hourly rate of pay: $"))
Hours = float(input("Hours worked in the week: "))
Total = (Pay*Hours)
Total = str(Total)

print("\nTotal pay for the week: ${0}".format(Total))
