"""
-------------------------------------------------------
Functions for lab 5
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-09-27"
-------------------------------------------------------
"""


# Function for t01
def magic_date(day, month, year):
    """
    -------------------------------------------------------
    Determines if a date is magic. A date is magic if the day
    times the month equals the year.
    Use: magic = magic_date(day, month, year)
    -------------------------------------------------------
    Parameters:
        day - numeric day (int > 0)
        month - numeric month (int > 0)
        year - numeric two-digit year (int > 0)
    Returns:
        magic - True if date is magic, False otherwise (boolean)
    -------------------------------------------------------
    """
    if day * month == year:
        date = True
    else:
        date = False

    return date


# Function for t06
def is_divisible(n, i, j):
    """
    -------------------------------------------------------
    Determines if n is evenly divisible by both i and j.
    Use: result = is_divisible(n, i, j)
    -------------------------------------------------------
    Parameters:
        n - the number to check for divisibility (int)
        i - one of the values to divide n by (int)
        j - another value to divide n by (int)
    Returns:
        result - True if n is evenly divisible by both
            i and j, False otherwise (boolean)
    ------------------------------------------------------
    """
    if n % i == 0 and n % j == 0:
        div = True
    else:
        div = False

    return div


# Function for t09
def wind_speed(speed):
    """
    -------------------------------------------------------
    Determines the wind catagory based on speed.
    Use: category = wind_speed(speed)
    -------------------------------------------------------
    Parameters:
        speed - wind speed in km/hr (int >= 0)
    Returns:
        category - description of wind speed (str)
    ------------------------------------------------------
    """
    if speed > 117:
        cat = "Hurricane"
    elif speed >= 89:
        cat = "Whole Gale"
    elif speed >= 62:
        cat = "Gale Winds"
    elif speed >= 39:
        cat = "Strong Wind"
    elif speed >= 0:
        cat = "Breeze"
    else:
        cat = "Unknown"

    return cat


# Function for t11
def quadrant(x, y):
    """
    -------------------------------------------------------
    Determines location on a plane of an x, y coordinate.
    Use: location = quadrant(x, y)
    -------------------------------------------------------
    Parameters:
        x - x coordinate on a Cartesian plane (float)
        y - y coordinate on a Cartesian plane (float)
    Returns:
        location - one of: 'Quadrant 1', 'Quadrant 2', 'Quadrant 3'
          'Quadrant 4', 'X-Axis', 'Y-Axis', 'Origin' (str)
    -------------------------------------------------------
    """

    if x == 0 and y != 0:
        coord = "Y-Axis"
    elif x != 0 and y == 0:
        coord = "X-Axis"
    elif x > 0 and y > 0:
        coord = "Quadrant 1"
    elif x < 0 and y > 0:
        coord = "Quadrant 2"
    elif x < 0 and y < 0:
        coord = "Quadrant 3"
    elif x > 0 and y < 0:
        coord = "Quadrant 4"
    else:
        coord = "Origin"

    return coord


# Function for t13
def loan():
    """
    -------------------------------------------------------
    An employee may qualify for a loan if they have worked for a
    minimum of 5 years, and has a salary of $30,000 or more.
    This function must ask for the years employed and the salary
    as appropriate.
    Use: qualified = loan()
    -------------------------------------------------------
    Returns:
        qualified - True if employee qualifies for a loan,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    # Constants
    YEARQUAL = 5
    SALQUAL = 30000

    qual = False
    years = int(input("Years employed: "))
    if years >= YEARQUAL:
        salary = float(input(f"Annual salary: $"))
        if salary >= SALQUAL:
            qual = True

    return qual
