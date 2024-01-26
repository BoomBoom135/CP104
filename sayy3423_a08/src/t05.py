"""
-------------------------------------------------------
chain words
-------------------------------------------------------
Author:  Nicholas Sayyad Shahbaz
ID:      169063423
Email:   sayy3423@mylaurier.ca
__updated__ = "2023-11-24"
-------------------------------------------------------
"""
# Imports
from functions import has_word_chain

#Variables and Display
print("Enter 'stop' to quit")
word = ""
words = []
while word != "quit":
    word = input("Enter a word: ")
    if word != "quit:":
        words.append(word)
word_chain = has_word_chain(words)
print(f"Result: {word_chain}")
