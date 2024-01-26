"""
-------------------------------------------------------
Functions for assignemnt 6
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-11-08"
-------------------------------------------------------
"""

# function for t01


def total_wins():
    """
    -------------------------------------------------------
    returns two numbers representing how many times 
    the string "purple" appeared in the input and how 
    many times the string "gold" appeared in the input.
    Use: pscore, gscore = total_wins()
    -------------------------------------------------------

    Returns:
        purple - number of purple wins
        gold - number of gold wins
    ------------------------------------------------------
    """
    purple = 0
    gold = 0
    team = " "
    while team != "":
        team = input("Enter the winning team: ")
        if team.lower() == "purple":
            purple = purple + 1
        elif team.lower() == "gold":
            gold = gold + 1
        else:
            continue
    return purple, gold


# function for t02
def detect_prime(number):
    """
    -------------------------------------------------------
    Determines if number is a prime number.
    Use: prime = detect_prime(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int > 1)
    Returns:
        prime - True if number is prime, False otherwise (bool)
    ------------------------------------------------------
    """
    div = 1
    prime = True
    while div < number:
        if number % div == 0 and div != 1:
            prime = False
            div = number
        div = div + 1

    return prime


# function for t03
def interest_table(principal_amount, interest_rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal_amount, interest_rate, payment)
    -------------------------------------------------------
    Parameters:
        principal_amount - original value of a loan (float > 0)
        interest_rate - yearly interest interest_rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    print("-"*33)
    print("Month  Interest  Payment  Balance")
    print("-"*33)

    balance = principal_amount
    month = 0
    while balance > 0:
        interest = (balance * (interest_rate/100)) / 12
        if balance < payment:
            payment = balance + interest
            balance = 0
        else:
            balance = balance - payment + interest
        month = month + 1
        print(f"{month:>5}{interest:>10.2f}{payment:>9.2f}{balance:>9.2f}")

    return


# Function for t04
def count_of_digits(number):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: digits = count_of_digits(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int)
    Returns:
        digits - the number of digits in number (int)
    ------------------------------------------------------
    """
    if number < 0:
        number = number * -1

    digits = 0
    while not number < 1:
        number = number / 10
        digits = digits + 1

    return digits


# Function for t05
def factor_summation(number):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = factor_summation(number)
    -------------------------------------------------------
    Parameters:
        number - a positive integer (int >= 1)
    Returns:
        total - the total of number's factors (int)
    ------------------------------------------------------
    """
    n = 1
    total = 0
    while n < number:
        if number % n == 0:
            total = total + n
        n = n + 1

    return total
