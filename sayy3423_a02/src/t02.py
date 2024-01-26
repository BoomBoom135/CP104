"""
-------------------------------------------------------
Subtracting Numbers with a Number
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-09-14"
-------------------------------------------------------
"""

number = int(input("Enter a positive digit number: "))

# Uses given number to find the 2 numbers
num1 = number // 10
num2 = number % 10
difference = num1 - num2

print(f'\nThe difference of the digits of {number} is {difference}')
