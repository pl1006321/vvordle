from colorama import *
import string 

def import_words():
    with open('words.txt', 'r') as file:
        words = file.read()    
    return words.split()

def check_input(input):
    if not input.isalpha() or len(input) != 5: 
        return False
    return True

def print_lets(used):
    for x in list(string.ascii_uppercase):
        if x in used:
            if used[x] == 'GREEN':
                print(Fore.GREEN + x, end=' ')
            elif used[x] == 'YELLOW':
                print(Fore.YELLOW + x, end=' ')
            else:
                print(Fore.BLACK + x, end='')
        else:
            print(Fore.RESET + x, end=' ')
    print('\n')


words = import_words() 
unused_lets = list(string.ascii_uppercase)
used_lets = {'A':'GREEN', 'C':'YELLOW', 'Z':'BLACK'} # testing
print_lets(used_lets)
