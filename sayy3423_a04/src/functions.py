"""
-------------------------------------------------------
Functions for assignment 4
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-10-10"
-------------------------------------------------------
"""

# Function for t01


def day_name(day_num):
    """
    -------------------------------------------------------
    Returns the name of a day of the week given an integer day number.
    Day 1 is Sunday, day 7 is Saturday.
    Returns Error if the number is not valid.
    Use: day = day_name(day_num)
    -------------------------------------------------------
    Parameters:
        day_num - day number (1 <= int <= 7)
    Returns:
        day - name of a day of the week (str)
    ------------------------------------------------------
    """
    if day_num == 1:
        day_num = "Sunday"
    elif day_num == 2:
        day_num = "Monday"
    elif day_num == 3:
        day_num = "Tuesday"
    elif day_num == 4:
        day_num = "Wednesday"
    elif day_num == 5:
        day_num = "Thursday"
    elif day_num == 6:
        day_num = "Friday"
    elif day_num == 7:
        day_num = "Saturday"
    else:
        day_num = False

    return day_num


# Function for t02
def pollution_ranking(air_quality_index):
    """
    -------------------------------------------------------
    Returns the pollution level given an AQI (Air Quality Index):
        Good - 0 to 50 AQI
        Moderate - 51 - 100 AQI
        Unhealthy for Sensitive Groups - 101 - 150 AQI
        Unhealthy - 151 - 200 AQI
        Very Unhealthy - 201 - 300 AQI
        Hazardous - 300+ AQI
    Returns Error if air_quality_index is negative.
    Use: pollution = pollution_ranking(air_quality_index)
    -------------------------------------------------------
    Parameters:
        air_quality_index - Air Quality Index (int)
    Returns:
        pollution - name of pollution level (str)
    ------------------------------------------------------
    """
    if air_quality_index >= 1:
        if air_quality_index <= 50:
            air_quality_index = "Good"
        elif air_quality_index <= 100:
            air_quality_index = "Moderate"
        elif air_quality_index <= 150:
            air_quality_index = "Unhealthy for Sensitive Groups"
        elif air_quality_index <= 200:
            air_quality_index = "Unhealthy"
        elif air_quality_index <= 300:
            air_quality_index = "Very Unhealthy"
        else:
            air_quality_index = "Hazardous"
    else:
        air_quality_index = "Error"

    return air_quality_index

# Function for t03


def largest_average(val1, val2, val3):
    """
    -------------------------------------------------------
    Returns the average of the two largest values of
    val1, val2, and val3.
    Use: average = largest_average(val1, val2, val3)
    -------------------------------------------------------
    Parameters:
        val1 - a number (float)
        val2 - a number (float)
        val3 - a number (float)
    Returns:
        average - the average of the two largest values of
            val1, val2, and val3 (float)
    ------------------------------------------------------
    """
    if val1 >= val2 or val2 >= val1 and val1 > val3 and val2 > val3:
        average = (val1 + val2) / 2
    elif val1 >= val3 or val3 >= val1 and val1 > val2 and val3 > val2:
        average = (val1 + val3) / 2
    elif val2 >= val3 or val3 >= val2 and val2 > val1 and val3 > val1:
        average = (val2 + val3) / 2
    else:
        average = "Error"
    return average


# Function for t04
def colour_combine(rgb_colour1, rgb_colour2):
    """
    -------------------------------------------------------
    Determines the secondary rgb_colour from mixing two primary
    RGB (Red, Green, Blue) colours. The order of the colours
    is *not* significant.
    Returns "Error" if any of the rgb_colour parameter(s) are invalid.
        "red" + "blue": "fuchsia"
        "red" + "green": "yellow"
        "green" + "blue": "aqua"
        "red" + "red": "red"
        "blue" + "blue": "blue"
        "green" + "green": "green"
    Use: rgb_colour = colour_combine(rgb_colour1, rgb_colour2)
    -------------------------------------------------------
    Parameters:
        rgb_colour1 - a primary RGB rgb_colour (str)
        rgb_colour2 - a primary RGB rgb_colour (str)
    Returns:
        rgb_colour - a secondary RGB rgb_colour (str)
    -------------------------------------------------------
    """
    if rgb_colour1 == rgb_colour2:
        colour = rgb_colour2
    elif rgb_colour1 == "red" and rgb_colour2 == "blue" or rgb_colour1 == "blue" and rgb_colour2 == "red":
        colour = "fuchsia"
    elif rgb_colour1 == "red" and rgb_colour2 == "green" or rgb_colour1 == "green" and rgb_colour2 == "red":
        colour = "yellow"
    elif rgb_colour1 == "green" and rgb_colour2 == "blue" or rgb_colour1 == "blue" and rgb_colour2 == "green":
        colour = "aqua"
    else:
        colour = "Error"

    return colour


# Function for t05
def hoo_rah(number):
    """
    -------------------------------------------------------
    Returns the word or parts of the 'Hoo Rah' based on any number
    divided by 2 and 7
    Use: phrase = hoo_rah(number)
    -------------------------------------------------------
    Parameters:
        number - any given number
    Returns:
        if num / 2, returns 'Hoo'
        if num / 7, returns 'Rah
        if both, returns 'Hoo Rah'
        if neither, returns 'Zip'
    ------------------------------------------------------
    """
    if number % 2 == 0 and number % 7 == 0:
        number = "Hoo Rah"
    elif number % 2 == 0 and number % 7 != 0:
        number = "Hoo"
    elif number % 2 != 0 and number % 7 == 0:
        number = "Rah"
    else:
        number = "Zip"

    return number
