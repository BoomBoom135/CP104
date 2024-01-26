"""
-------------------------------------------------------
functions for lab 9
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-11-01"
-------------------------------------------------------
"""

# Function for t03


def parse_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code. A product code has three parts:
        The first three letters describe the product category
        The next four digits are the product ID
        The remaining characters describe the product's qualifiers
    Use: pc, pi, pq = parse_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a valid product code (str)
    Returns:
        pc - the category part of product_code (str)
        pi - the id part of product_code (str)
        pq - the qualifier part of product_code (str)
    -------------------------------------------------------
    """
    pc = product_code[0:3]
    pi = product_code[3:7]
    pq = product_code[7:]
    return pc, pi, pq


# function for t04
def validate_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code and prints whether the various parts are valid.
    A product code has three parts:
        The first three letters describe the product category and must
        all be in upper case.
        The next four digits are the product ID.
        The remaining characters describe the product's qualifiers,
        such as colour, size, etc. and always begins with an uppercase letter.
    Use: category, digits, qualifiers = validate_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a product code (str)
    Returns:
        category - True if three upper-case characters, False otherwise
        digits - True if four digits, False otherwise
        qualifiers - True if starts with 1 upper-case letter, False otherwise
    -------------------------------------------------------
    """
    category = product_code[0:3]
    digits = product_code[3:7]
    qualifiers = product_code[7:]

    if len(product_code) >= 3:
        if category.isalpha() and category.isupper():
            category = True
        else:
            category = False
    else:
        category = False

    if len(product_code) >= 7:
        if digits.isdigit():
            digits = True
        else:
            digits = False
    else:
        digits = False

    if len(product_code) >= 8:
        if qualifiers[0].isupper():
            qualifiers = True
        else:
            qualifiers = False
    else:
        qualifiers = False

    return category, digits, qualifiers


# function for t05
def password_strength(password):
    """
    -------------------------------------------------------
    Checks the strength of a given password. A password is
    strong if it contains at least eight characters, has a
    combination of upper-case and lower-case letters, and
    includes digits. Prints one or more of:
        not long enough - if password less than 8 characters
        no digits - if password has no digits
        no upper case - if password has no upper case letters
        no lower case - if password has no lower case letters
    Use: password_strength(password)
    -------------------------------------------------------
    Parameters:
        password - the password to be checked (str)
    Returns:
        None
    ------------------------------------------------------
    """
    length = False
    digit = False
    upper = False
    lower = False

    if len(password) >= 8:
        length = True

    for a in password:
        if a.isdigit():
            digit = True

    for b in password:
        if b.isupper():
            upper = True

    for c in password:
        if c.islower():
            lower = True

    if length == False:
        print("Not long Enough")
    if digit == False:
        print("No Digits")
    if upper == False:
        print("No Upper Case")
    if lower == False:
        print("No Lower Case")

    return


# function fro t10
def text_analyze(txt):
    """
    -------------------------------------------------------
    Analyzes txt and returns the number of uppercase letters,
    lowercase letters, digits, and number of whitespaces in txt.
    Use: uppr, lowr, dgts, whtspc = text_analyze(txt)
    -------------------------------------------------------
    Parameters:
        txt - the text to be analyzed (str)
    Returns:
        uppr - number of uppercase letters in txt (int >= 0)
        lowr - number of lowercase letters in txt (int >= 0)
        dgts - number of digits in txt (int >= 0)
        whtspc - number of white spaces in the text (spaces, tabs, linefeeds) (int >= 0)
    ------------------------------------------------------
    """
    uppr = 0
    lowr = 0
    dgts = 0
    whtspc = 0

    for a in txt:
        if a.isupper():
            uppr = uppr + 1

    for b in txt:
        if b.islower():
            lowr = lowr + 1

    for c in txt:
        if c.isdigit():
            dgts = dgts + 1

    for d in txt:
        if d.isspace():
            whtspc = whtspc + 1

    return uppr, lowr, dgts, whtspc


# function for t12
def comma_period_replace(string):
    """
    -------------------------------------------------------
    Replaces all the commas with a period in s.
    Use: out = comma_period_replace(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        out - string with all commas replaced by a period (str)
    ------------------------------------------------------
    """
    out = ""

    for i in range(0, len(string), 1):
        if string[i] == ",":
            out = out + "."
        else:
            out = out + string[i]

    return out
