"""
-------------------------------------------------------
Flyers per person and remaining
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-09-14"
-------------------------------------------------------
"""
# Collects inputs and does calculations
flyersN = int(input("Number of flyers: "))
peopleN = int(input("Number of delivery people: "))
deliveryPP = flyersN // peopleN
leftOver = flyersN % peopleN

print(
    f"\nFlyers per delivery person: {deliveryPP}\nFlyers left over: {leftOver}")
