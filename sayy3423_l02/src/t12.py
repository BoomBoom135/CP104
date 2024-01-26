"""
-------------------------------------------------------
Calculates Days, Hours, Minutes and Seconds from a total amount of Seconds
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-09-13"
-------------------------------------------------------
"""

# Process to calculate each time variable
seconds = int(input("Number of seconds: "))
MINUTES = 60

SECPMIN = seconds / MINUTES
numDays = SECPMIN // 1440
SECPMIN = SECPMIN - (numDays * 1440)
numHours = SECPMIN // 60
SECPMIN = SECPMIN - (numHours * 60)
seconds = SECPMIN * 60
numMinutes = seconds // 60
seconds = seconds - (numMinutes * 60)

# Returns variables to integers if needed
numDays = int(numDays)
numHours = int(numHours)
numMinutes = int(numMinutes)
seconds = int(round(seconds, 0))


print("\nDays:", numDays, "Hours:", numHours,
      "Minutes:", numMinutes, "Seconds:", seconds)
