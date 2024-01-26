"""
-------------------------------------------------------
Calculating Discount
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-09-13"
-------------------------------------------------------
"""
# Gets inputs and calculates the discount
Number = float(input("Enter number: "))
Percent = float(input("Enter percent: "))
Discount = (Number * (Percent / 100))

print(f"\nA {Percent} percent discount on {Number} is {Discount:.1f}")
