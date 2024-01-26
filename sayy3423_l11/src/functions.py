"""
-------------------------------------------------------
functions for lab 11
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-11-27"
-------------------------------------------------------
"""
#imports
from random import randint
from random import uniform


# function for t01
def generate_matrix_num(rows, cols, low, high, value_type):
    """
    -------------------------------------------------------
    Generates a 2D list of numbers of the given type, 'float' or 'int'.
    (To generate random float number use random.uniform and to
    generate random integer number use random.randint)
    Use: matrix = generate_matrix_num(rows, cols, low, high, value_type)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the list (int > 0)
        cols - number of columns (int > 0)
        low - low value of range (float)
        high - high value of range (float > low)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        matrix - a 2D list of random numbers (2D list of float/int)
    -------------------------------------------------------
    """
    matrix = []
    for a in range(rows):
        list = []
        for b in range(cols):
            if value_type == "float":
                num = uniform(low,high)
            elif value_type == "int":
                num = randint(low,high)
            else:
                continue
            list.append(num)
        matrix.append(list)
        
    return matrix
        
        
#function for t03
def print_matrix_num(matrix, value_type):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list in a formatted table.
    Prints float values with 2 decimal points and prints row and
    column headings.
    Use: print_matrix_num(matrix, 'float')
    Use: print_matrix_num(matrix, 'int')
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of values (2D list)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        None.
    -------------------------------------------------------
    """
    rows = len(matrix[0])
    cols = len(matrix)
    
    header = "   "
    for i in range(cols):
        header += f"{i:>7}"
    print(header)
    
    for a in range(rows):
        line = f"{a:>4}"
        for b in range(cols):
            if value_type == "float":
                line += f"{matrix[a][b]:>6.2f} "
            else:
                line += f"{matrix[a][b]:>6} "
        print(line)
    
    return
    
#function for t07
def find_position(matrix):
    """
    -------------------------------------------------------
    Determines the first locations [row, column] of smallest and
    largest values in a 2D list.
    Use: s_loc, l_loc = find_position(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list)
    Returns:
        s_loc - a list of of the row and column location of
            the smallest value in matrix (list of int)
        l_loc - a list of of the row and column location of
            the largest value in matrix (list of int)
    -------------------------------------------------------
    """
    rows = len(matrix[0])
    cols = len(matrix)
    smallest = biggest = matrix[0][0]
    s_loc = l_loc = [0,0]
    for a in range(cols):
        for b in range(rows):
            if matrix[a][b] < smallest:
                s_loc = [a,b]
                smallest = matrix[a][b]
            elif matrix[a][b] > biggest:
                l_loc = [a,b]
                biggest = matrix[a][b]
            else:
                continue
    return s_loc, l_loc
    

#function for t13
def matrix_scalar_multiply(matrix, num):
    """
    -------------------------------------------------------
    Update matrix by multiplying each element of matrix by num.
    Use: matrix_scalar_multiply(matrix, num)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix to multiply (2D list of int/float)
        num - the number to multiply by (int/float)
    Returns:
        None
    ------------------------------------------------------
    """
    rows = len(matrix)
    cols = len(matrix[0])
    
    for a in range(rows):
        for b in range(cols):
            matrix[a][b] *= num
            
    return


#function for t14
def matrix_transpose(matrix):
    """
    -------------------------------------------------------
    Transpose the contents of matrix. (Swap the rows and columns.)
    Use: transposed = matrix_transpose(matrix):
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list (2D list of *)
    Returns:
        transposed - the transposed matrix (2D list of *)
    ------------------------------------------------------
    """
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = []
    for a in range(cols):
        line = []
        for b in range(rows):
            line.append(matrix[b][a])
        transposed.append(line)
        
    return transposed
            
        
    
    
    
