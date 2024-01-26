"""
-------------------------------------------------------
Lab 4 Functions
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-09-18"
-------------------------------------------------------
"""
# Imports
import math


# Area of a circle for t03
def area(radius):
    """
    -------------------------------------------------------
    Calculates and returns area of a circle.
    Use: ar = area(radius)
    -------------------------------------------------------
    Parameters:
        radius - radius of a circle (float >= 0)
    Returns:
        ar - area of a circle (float)
    ------------------------------------------------------
    """
    areaC = math.pi * (radius ** 2)
    return areaC

# Radius, diameter, circumference, and area using pythagorean theorem for t06


def pythag(s1, s2):
    """
    -------------------------------------------------------
    Calculates and returns the radius, diameter, circumference,
    and area of circle defined by a right triangle.
    Use: radius, diam, circ, area = pythag(s1, s2)
    -------------------------------------------------------
    Parameters:
        s1 - length of side 1 of a right triangle (float > 0)
        s2 - length of side 2 of a right triangle (float > 0)
    Returns:
        radius - radius of the resulting circle (float)
        diam - diameter of the resulting circle (float)
        circ - circumference of the resulting circle (float)
        area - area of the resulting circle (float)
    ------------------------------------------------------
    """
    radius = math.sqrt((s1 ** 2) + (s2 ** 2))
    diameter = 2 * radius
    circ = 2 * math.pi * radius
    area = math.pi * (radius ** 2)

    return radius, diameter, circ, area


# Change for t07
def total_change(nickels, dimes, quarters, loonies, toonies):
    """
    -------------------------------------------------------
    Calculates the total value of a set of coins in dollars.
    Each coin is worth:
        nickel:  $0.05
        dime:    $0.10
        quarter: $0.25
        loonie:  $1.00
        toonie:  $2.00
    Use: total = total_change(nickels, dimes, quarters,
        loonies, toonies)
    -------------------------------------------------------
    Parameters:
        nickels - number of nickels (int >= 0)
        dimes - number of dimes (int >= 0)
        quarters - number of quarters (int >= 0)
        loonies - number of loonies (int >= 0)
        toonies - number of toonies (int >= 0)
    Returns:
        total - total value of coins (float)
    -------------------------------------------------------
    """
    NICKELS = 0.05
    DIMES = 0.10
    QUARTERS = 0.25
    LOONIES = 1
    TOONIES = 2
    total = (nickels * NICKELS) + (dimes * DIMES) + (quarters *
                                                     QUARTERS) + (loonies * LOONIES) + (toonies * TOONIES)

    return total


# Calculating Slope for t11
def slope(x1, y1, x2, y2):
    """
    -------------------------------------------------------
    Calculates the slope of a line. Slope is calculated as
    rise / run, where rise is distance between y coordinates,
    and run is distance between x coordinates.
    Use: slp = slope(x1, y1, x2, y2)
    -------------------------------------------------------
    Parameters:
        x1 - x coordinate of first point on a graph (float)
        y1 - y coordinate of first point on a graph (float)
        x2 - x coordinate of second point on a graph (float)
        y2 - y coordinate of second point on a graph (float)
        x2 != x1
    Returns:
        slp - slope of the line through (x1,y1) and (x2,y2)
    -------------------------------------------------------
    """
    slp = (y2 - y1) / (x2 - x1)
    return slp


# Calculating Celsius for t13
def f_to_c(fahrenheit):
    """
    -------------------------------------------------------
    Converts temperatures in fahrenheit to celsius.
    Use: celsius = f_to_c(fahrenheit)
    -------------------------------------------------------
    Parameters:
        fahrenheit - temperature in fahrenheit (int >= -459)
    Returns:
        celsius - equivalent to celsius (float)
    -------------------------------------------------------
    """
    FAHRENHEIT = 32
    celsius = (fahrenheit - FAHRENHEIT) * (5 / 9)

    return celsius
