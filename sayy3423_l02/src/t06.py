"""
-------------------------------------------------------
Calculates the monthly pay of mortgage.
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-09-13"
-------------------------------------------------------
"""

# Variables to calculate mortgage
principal = float(input("Mortgage principal ($): $"))
numYears = int(input("Number of years: "))
interestR = float(input("Yearly interest rate (%): "))

# Calculations for the Final/ Total Amount
numYears = numYears * 12
interestR = interestR / 12 / 100
tAmount = principal * (interestR*(1 + interestR) **
                       numYears) / ((1 + interestR) ** numYears - 1)
tAmount = str(tAmount)

print("\nThe monthly payments are: ${0}".format(tAmount))
