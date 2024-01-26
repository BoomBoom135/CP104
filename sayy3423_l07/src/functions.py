"""
-------------------------------------------------------
Functions for Lab 7
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-11-01"
-------------------------------------------------------
"""
# Function for t01


def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """
    from random import randint
    number = randint(1, high)
    count = 0
    guess = -1

    while guess != number:
        guess = int(input("Guess: "))
        count = count + 1
        if guess > number:
            print("Too high, try again.")
        elif guess < number:
            print("Too low, try again")
        else:
            print("Congratulations - good guess!")
    return count


# Function for t02
def power_of_two(target):
    """
    -------------------------------------------------------
    Determines the nearest power of 2 greater than or equal to
    a given target.
    Use: power = power_of_two(target)
    -------------------------------------------------------
    Parameters:
        target - value to find nearest power of 2 (int >= 0)
    Returns:
        power - first power of 2 >= target (int)
    -------------------------------------------------------
    """
    power = 0
    num = 2
    num = num**power
    while not num >= target:
        power = power + 1
        num = 2
        num = num**power
    return num


# Functions t04
def sum_squares(target):
    """
    -------------------------------------------------------
    Determines the sum of squares closest to, and greater than or
    equal to, a target value.
    Use: final = sum_squares(target)
    -------------------------------------------------------
    Parameters:
        target - target value (int >= 0)
    Returns:
        final - the final sum of squares >= target (int)
    -------------------------------------------------------
    """
    a = 1
    sum = a
    while sum <= target:
        a = a + 1
        sum = sum + (a**2)
    return sum

# Functions t08


def budget(available):
    """
    -------------------------------------------------------
    Asks a user for a series of expenses in a month. Calculate the
    total expenses and determines whether the user is in "Surplus",
    "Deficit", or "Balanced" status.
    Use: expenses, balance, status = budget(available)
    -------------------------------------------------------
    Parameters:
        available - money currently available (float >= 0)
    Returns:
        expenses - total monthly expenses (float)
        balance - remaining balance (float)
        status - One of (str):
            "Surplus" if user budget is in surplus
            "Deficit" if user budget is in deficit
            "Balanced" if user budget is balanced
    ------------------------------------------------------
    """
    add = float(input(f"Enter an expense (0 to quit): $"))
    expenses = 0

    while add != 0:
        expenses = expenses + add
        add = float(input(f"Enter another expense (0 to quit): $"))
    balance = available - expenses

    if expenses > balance:
        status = "Deficit"
    elif expenses < balance:
        status = "Surplus"
    else:
        status = "Balanced"

    return expenses, balance, status

# Function for t10


def employee_payroll():
    """
    -------------------------------------------------------
    Calculates and returns the weekly employee payroll for all employees
    in an organization. For each employee, ask the user for the employee ID
    number, the hourly wage rate, and the number of hours worked during a week.
    An employee number of zero indicates the end of user input.
    Each employee is paid 1.5 times their regular hourly rate for all hours
    over 40. A tax amount of 3.625 percent of gross salary is deducted.
    Use: total, average = employee_payroll()
    -------------------------------------------------------
    Returns:
        total - total net employee wages (i.e. after taxes) (float)
        average - average employee net wages (float)
    ------------------------------------------------------
    """
    id = -1
    total = 0
    count = 0
    paymentN = 0
    while id != 0:
        total = total + paymentN
        id = int(input("Employee ID: "))
        if id != 0:
            wageH = float(input("Hourly wage rate: "))
            worked = float(input("Hours worked: "))
            paymentN = float(input(f"Net payment for employee {id}: $"))
            count = count + 1
            print(" ")
    average = total / count

    return total, average
