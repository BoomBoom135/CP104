"""
-------------------------------------------------------
functions for a05
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-10-30"
-------------------------------------------------------
"""

# Function for t01


def calc_factorial(number):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of number.
    Use: product = calc_factorial(number)
    -------------------------------------------------------
    Parameters:
        number - number to factorial (int > 0)
    Returns:
        product - number! (int)
    ------------------------------------------------------
    """
    num = 1
    for i in range(1, number+1):
        num = num * i

    return num


# Function for t02
def calories_treadmill(per_min, minutes):
    """
    -------------------------------------------------------
    Calculates and returns the amount of calories burned
    within a given time.
    Use: calories = calories_treadmill(per_min, minutes)
    -------------------------------------------------------
    Parameters:
        per_min - number = increment (int > 0)
        mintues - the total minutes (int)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(5, minutes+1, 5):
        sum = i * per_min
        print(f"{i:>3}{sum:>7.1f}")

    return


# Function for t03
def arrow_up(rows):
    """
    -------------------------------------------------------
    Draws an arrow given the number of rows.
    Use: arrow_up(rows)
    -------------------------------------------------------
    Parameters:
        rows - the number of rows wanted
    Returns:
        None
    ------------------------------------------------------
    """
    hash = "#"
    width = rows
    space = " "
    for i in range(1, rows+1):
        if i == 1:
            print(f"{hash:>{width}}")
        else:
            print(f"{hash:>{width}}{space}{hash}")
            space = space + (2*(" "))

        width = width - 1
    return

# Function for t04


def multiplication_table(start_num, stop_num):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start_num to stop_num.
    Use: multiplication_table(start_num, stop_num)
    -------------------------------------------------------
    Parameters:
        start_num - the range start value (int)
        stop_num - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """

    top = "\t    "
    barM = 0
    for a in range(start_num, stop_num+1, 1):
        top = top + str(a) + "    "
        barM = barM + 5

    print(" ")
    print(top)
    print("\t" + "-"*(barM))

    row = " "
    gap = " "
    for b in range(start_num, stop_num+1, 1):
        row = "     " + str(b) + " |"
        for c in range(start_num, stop_num+1, 1):
            if b*c > 9:
                gap = "   "
            elif b*c > 99:
                gap = "  "
            else:
                gap = "    "
            row = row + gap + str(b*c)
        print(row)

    return

# Function for t05


def range_addition(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum values from start by increment.
    Use: total = range_addition(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """
    sum = 0
    for i in range(start, (count*increment)+1, increment):
        sum = sum + i

    return sum
