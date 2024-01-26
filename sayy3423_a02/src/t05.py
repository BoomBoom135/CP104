"""
-------------------------------------------------------
Contractor Calculations
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-09-14"
-------------------------------------------------------
"""

# Input variables
lengthF = float(input("Foundation length (m): "))
widthF = float(input("Foundation width (m): "))
heightF = float(input("Foundation height (m): "))
heightW = float(input("Wall height (m): "))
concreteC = float(input("Cost of concrete ($/m^3): $"))
bricksC = float(input("Cost of bricks ($/m^2): $"))

# Calculations for size and cost
foundationA = lengthF * widthF * heightF
concreteT = foundationA * concreteC
bricksA = (2 * (heightW * widthF)) + (2 * (heightW * lengthF))
bricksT = bricksC * bricksA
totalC = bricksT + concreteT

# Displays print
print(f"\nConcrete needed for foundation (m^3): {foundationA:.2f}")
print(f"Cost of concrete: {concreteT:.2f}")
print(f"Bricks needed for walls (m^2): {bricksA:.2f}")
print(f"Cost of bricks: ${bricksT:.2f}")
print(f"Total cost: ${totalC:.2f}")
