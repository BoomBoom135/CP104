"""
-------------------------------------------------------
functions for assignment 7
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-11-09"
-------------------------------------------------------
"""

# function for t01


def list_factors(number):
    """
    -------------------------------------------------------
    Finds all the factors of a given number greater than 0.
    Use: factors = list_factors(number):
    -------------------------------------------------------
    Parameters:
        number = any given number(int>0)
    Returns:
        factors - A list of all factors(list of int)
    ------------------------------------------------------
    """
    factors = []
    for i in range(1, number, 1):
        if number % i == 0:
            factors.append(i)

    return factors

# function for t02


def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: number_list = list_positives()
    -------------------------------------------------------
    Returns:
        number_list - A list of positive integers (list of int)
    ------------------------------------------------------
    """
    number_list = []
    num = -1
    while num != 0:
        num = int(input("Enter a positive number: "))
        if num > 0:
            number_list.append(num)

    return number_list


# functions for t03
def get_indexes(numbers, target_number):
    """
    -------------------------------------------------------
    Finds the indexes of target_number in numbers.
    Use: index_list = get_indexes(numbers, target_number)
    -------------------------------------------------------
    Parameters:
        numbers - list of values (list)
        target_number - value to look for in num_list (*)
    Returns:
        index_list - list of indexes of target_number (list of int)
    -------------------------------------------------------
    """
    index_list = []
    for i in range(0, len(numbers), 1):
        if numbers[i] == target_number:
            index_list.append(i)

    return index_list


# functions for t04
def list_subtract(minuend, subtrahend):
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are removed from the first list.
    Use: list_subtract(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """

    for item in minuend:
        if item == subtrahend:
            minuend.pop(item)

    print(minuend)
    return

# function for t05


def verify_sorted(numbers):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = verify_sorted(numbers)
    -------------------------------------------------------
    Parameters:
        numbers - a list of numbers (list)
    Returns:
        in_order - True if numbers is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """
    in_order = True
    index = -1
    b = 0
    for a in range(0, len(numbers)):
        if numbers[a] < b:
            in_order = False
            index = a
            break
        else:
            b = numbers[a]

    return in_order, index
