"""
-------------------------------------------------------
functions for assignemnt 8
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-11-24"
-------------------------------------------------------
"""
#function for t01
def add_spaces(sentence):
    """
    -------------------------------------------------------
    Create a new sentence with added space between words. Words start
    with upper-case characters.
    Use: spaced = add_spaces(sentence)
    -------------------------------------------------------
    Parameters:
        sentence - sentence that represents a sentence in which all the
            words are run together (no spaces), but the first character
            of each word is uppercase. sentence has at least one
            character (str)
    Returns:
        spaced - new sentence in which the words are separated
            by spaces and only the first word starts with
            an uppercase character (str)
    -------------------------------------------------------
    """
    spaced = sentence[0]
    for i in range(1,len(sentence),1):
        if sentence[i] == sentence[i].upper() and sentence[i].isalpha():
            spaced = spaced + " " + sentence[i].lower()
        else:
              spaced = spaced + sentence[i]
    
    return spaced

#function for t02
def pluralize(string):
    """
    -------------------------------------------------------
    Pluralizes a string according to the rules:
        - if string ends with 's', 'sh', or 'ch', add 'es'
        - if string ends with 'y' but not 'ay' or 'oy', replace
            the 'y' with 'ies'
        - otherwise add 's'
    Use: pluralized = pluralize(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        pluralized - a pluralized_string version of string (str)
    -------------------------------------------------------
    """

    if string[-1] == "y":
        string = string[:-1] + "ies"
    elif string == "s":
        string = string + "'"
    else:
        string = string + "s"
        
    return string
    
#function for t03
def common_end(str1, str2):
    """
    -------------------------------------------------------
    Returns the longest common ending of two strings.
    Use: suffix = common_end(str1, str2)
    -------------------------------------------------------
    Parameters:
        str1 - first string for ending comparison (str)
        str2 - second string for ending comparison (str)
    Returns:
        suffix - the longest common ending of str1 and str2 (str)
    -------------------------------------------------------
    """
    if len(str1) < len(str2):
        shortest = len(str1)
    elif len(str2) < len(str1):
        shortest = len(str2)
    else: 
        shortest = len(str1)
    
    i = -1
    suffix = ""
    while i != -shortest-1:
        if str1[i] == str2[i]:
            suffix = str1[i] + suffix
        i = i - 1
        
    return suffix
    
    
#function for t04
def valid_isbn(isbn):
    """
    -------------------------------------------------------
    Determines if an ISBN string is valid. An ISBN string is valid if:
        - it consists of only digits and dashes ('-')
        - it contains 5 groups of digits separated by dashes
        - its first group of digits is either '978' or '979'
        - its final group of digits is a single digit
        - its entire length is 17 characters
    Use: is_valid = valid_isbn(isbn)
    -------------------------------------------------------
    Parameters:
        isbn - a string (str)
    Returns:
        is_valid - True if isbn is valid, False otherwise (boolean)
    -------------------------------------------------------
    """
    is_valid = True
    groups = []
    sep = isbn.split("-")
    for a in sep:
        if a != "":
            groups.append(a)
    
    if len(isbn) != 17 or len(groups[-1]) != 1 or int(groups[0]) != 978 and int(groups[0]) != 979 or len(groups) != 5:
        is_valid = False
   
    i = 0
    while is_valid == True and i < len(isbn):
        if isbn[i] != "-" and isbn[i].isalpha():
            is_valid = False
        i = i + 1
    
    return is_valid

#function for t05
def has_word_chain(words):
    """
    -------------------------------------------------------
    Determines if a list of strings is a word chain. A word chain
    is a list of words in which the last character of a word in
    the list is the same as the first character of the next word
    in the list.
    Use: word_chain = has_word_chain(words)
    -------------------------------------------------------
    Parameters:
        words - a of strings (list of str, len > 1)
    Returns:
        word_chain - True if words is a word chain,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    word_chain = True
    end = words[0][-1]
    i = 1
    while i < len(words)-1:
        if words[i][0] != end:
            word_chain = False
            i = len(words)
        else:
            end = words[i][-1]
            i = i + 1
    return word_chain
            

