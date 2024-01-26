"""
-------------------------------------------------------
Calculating Total Meal Cost
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-09-24"
-------------------------------------------------------
"""

# Variables From User
Breakfast = float(input(f"Enter cost of breakfast: $"))
Lunch = float(input(f"Enter cost of lunch: $"))
Supper = float(input(f"Enter cost of supper: $"))

Total = Breakfast + Lunch + Supper

# Display for user
print("")
print("Meal\t\tCost")
print(f"Breakfast\t${Breakfast:6.2f}")
print(f"Lunch\t\t${Lunch:6.2f}")
print(f"Supper\t\t${Supper:6.2f}")
print(f"Total\t\t${Total:6.2f}")
