"""
-------------------------------------------------------
Annual tax Calcualtion
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-09-14"
-------------------------------------------------------
"""
# Constant
TAX = 18.5

# Collects sales and calculates tax
sales = float(input(f"Enter the total sales: $"))
allTax = sales * (TAX / 100)
dashes = ("-") * 25

print(
    f"\nProjected Tax Report\n{dashes}\nTotal sales:  $ {sales:,.2f}\nAnnual Tax:   % {TAX:.2f}\n{dashes}\nTax:\t      $ {allTax:.2f} ")
