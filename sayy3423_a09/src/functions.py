"""
-------------------------------------------------------
functions for assignment 9
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-11-26"
-------------------------------------------------------
"""
# function for t01
def file_top(file_handle, count):
    """
    -------------------------------------------------------
    Prints first count lines of file_handle. Line numbering starts at 0.
    If length of file is shorter than count, stops printing after
    last line of file.
    Use: file_top(file_handle, count)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
        count - number of lines to print (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """
    i = 0
    while i < count:
        line = file_handle.readline().strip()
        print(line)
        i = i + 1
    
    return

# function for t02
def read_integers(file_handle):
    """
    -------------------------------------------------------
    Extracts positive integers from a file into a list of integers.
    Numbers are comma-delimited. Non-numeric tokens are ignored.
    Use: number_list = read_integers(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        number_list - a list of integers from file_handle (list of int)
    -------------------------------------------------------
    """
    number_list = []
    for line in file_handle:
        line = line.strip().split(",")
        number_list.append(int(line[1]))
        number_list.append(int(line[2]))
        number_list.append(int(line[3]))
        
    return number_list
    
    
#function for t03
def file_statistics(file_handle):
    """
    -------------------------------------------------------
    Evaluates the contents of a file by counting upper-case letters,
    lower-case letters, digits, white-spaces (including end-of-line
    characters), and remaining characters.
    Use: ucount, lcount, dcount, wcount, rcount = file_statistics(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        ucount - The number of upper-case letters in the file (int)
        lcount - The number of lower-case letters in the file (int)
        dcount - The number of digits in the file (int)
        wcount - The number of white-space characters in the file (int)
        rcount - The number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    ucount = 0
    lcount = 0
    dcount = 0
    wcount = 0
    rcount = 0
    for line in file_handle:
        for c in line:
            if c.isdigit():
                dcount += 1   
            elif c.islower():
                lcount += 1
            elif c.isupper():
                ucount += 1
            elif c.isspace():
                wcount += 1
            else:
                rcount += 1
                
    return ucount,lcount,dcount,wcount,rcount
    
    
#function for t04
def line_numbering(fh_read, fh_write):
    """
    -------------------------------------------------------
    Adds line numbers to a file. Contents of fh_write contain contents
    of fh_read where every line has line numbers added to the beginning
    of the line in the format [number]. Line numbering starts at 0.
    Put a single space after the line number.
    Use: line_numbering(fh_read, fh_write)
    -------------------------------------------------------
    Parameters:
        fh_read - file to read (file - open for reading)
        fh_write - file to write (file - open for writing)
    Returns:
        None
    -------------------------------------------------------
    """
    i = 0
    while i < 142:
        line = fh_read.readline()
        fh_write.write(f"[{i}] {line}")
        i += 1
    
    return
    
#Function for t05
def student_stats(file_handle):
    """
    -------------------------------------------------------
    Get information from a file of file_handle and grades.
    Use: l_id, h_id, avg = student_stats(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - student information file in the format
            surname,forename,id,mark (file - open for reading)
    Returns:
        l_id - the id of the student with the lowest mark (str)
        h_id - the id of the student with the highest mark (str)
        avg - the average mark (float)
    -------------------------------------------------------
    """
    line = file_handle.readline().split(",")
    low = high = total = int(line[3])
    l_id = h_id = line[2]
    count = 1
    for line in file_handle:
        line = line.strip()
        line = line.split(",")
        if int(line[3]) > high:
            h_id = line[2]
            high = int(line[3])
        if int(line[3]) < low:
            l_id = line[2]
            low = int(line[3])
        count += 1
        total += int(line[3])
    avg = total / count
    
    return l_id, h_id, avg
    
    
    
    
    
