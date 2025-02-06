from colorama import *
import string 

def import_words():
    with open('words.txt', 'r') as file:
        words = file.read()    
    return words.split()

words = import_words() 
unused_lets = list(string.ascii_uppercase)
used_lets = []
