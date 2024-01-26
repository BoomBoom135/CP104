"""
-------------------------------------------------------
Functions for Lab 6
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-10-08"
-------------------------------------------------------
"""

# function for t03


def sum_all(start, finish, increment):
    """
    -------------------------------------------------------
    Sums and returns all numbers from start to finish (inclusive)
    by increment.
    Use: total = sum_all(start, finish, increment)
    -------------------------------------------------------
    Parameters:
        start - an integer (int > 0)
        finish - an integer (int >= start)
        increment - an integer (int > 0)
    Returns:
        total - sum of all numbers from start to
            finish by increment (int)
    ------------------------------------------------------
    """
    total = 0
    for i in range(start, finish + 1, increment):
        total = total + i
    return total

# Function for t08


def draw_hollow_triangle(width, char):
    """
    -------------------------------------------------------
    Prints a hollow triangle of width characters using
    the char character.
    Use: draw_hollow_triangle(width, char)
    -------------------------------------------------------
    Parameters:
        width - number of characters wide (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(0, width):
        if i < 1:
            print(char)
        elif i < width - 1:
            print(char + (i-1) * " " + char)
        else:
            print(char * width)

    return


# Function for t11
def retirement(age, salary, increase):
    """
    -------------------------------------------------------
    Calculates a prints a table of how much a worker earns
    between age and retirement at 65.
    Use: retirement(age, salary, increase)
    -------------------------------------------------------
    Parameters:
        age - worker's current age (int > 0)
        salary - worker's current salary (float > 0)
        increase - percent increase in salary per year (float >= 0)
    Returns:
        None
    ------------------------------------------------------
    """
    print("\nAge\t     Salary")
    print("-------------------")
    total = salary
    for i in range(age, 66, 1):
        print(f"{i}{total:>17,.2f}")
        total = total + (total * increase / 100)

    return


# Function for t13
def lumber(b_min, b_max, b_inc, h_min, h_max, h_inc):
    """
    -------------------------------------------------------
    Create a table of the engineering properties of lumber.
    Given the base and height of a piece of lumber in inches,
    different properties of a piece of lumber are calculated as:
        cross-sectional area = base × height
        moment of inertia = base × height^3 / 12
        section modulus = base × height^2 / 6
    Use: lumber(b_min, b_max, b_inc, h_min, h_max, h_inc)
    -------------------------------------------------------
    Parameters:
        b_min - minimum value of base (int > 0)
        b_max - maximum value of base (int > b_min)
        b_inc - increment in base value (int > 0)
        h_min - minimum value of height (int > 0)
        h_max - maximum value of height (int > h_min)
        h_inc - increment in height value (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """
    print("\n              Cross-Sectional   Moments of   Section")
    print("Base  Height  Area              Inertia      Modules")
    print("----------------------------------------------------")
    for b in range(b_min, b_max+1, b_inc):
        for h in range(h_min, h_max+1, h_inc):
            area = b * h
            inertia = (b * h**3) / 12
            modules = (b * h**2) / 6
            print(f"{b:>4}  x {h:>4} {area:>16.2f} {inertia:>12.2f} {modules:>9.2f}")

    return


# Function for t14
def ia_hours(ia_count):
    """
    -------------------------------------------------------
    Calculates the total number of hours that IAs (Instructional
    Assistants) work over a 6 week period by asking for the hours
    for each IA per week.
    Use: total_hours = ia_hours(ia_count)
    -------------------------------------------------------
    Parameters:
        ia_count - number of IAs (int > 0)
    Returns:
        total_hours - hours worked by all IAs (float)
    ------------------------------------------------------
    """
    total = 0
    WEEKS = 6
    print("")
    for i in range(1, WEEKS + 1):
        print(f"Week {i}")
        for j in range(1, ia_count + 1):
            hours = float(input(f"  Marking hours for IA {j}: "))
            total = total + hours

    return total
