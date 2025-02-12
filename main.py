from colorama import *
import string 
import random

def import_words():
    with open('words.txt', 'r') as file:
        words = file.read()    
    return words.split()

def choose_word():
    return random.choice(words)

def check_input(input):
    if not input.isalpha() or len(input) != 5: 
        return False
    return True

def take_input():
    while True:
        guess = str(input('enter a five letter word for your guess: '))
        if not check_input(guess) or guess not in words:
            print('invalid input! please try again')
            input('enter anything to continue')
        else:
            break
    return guess.upper()

def check_guess(guess, answer):
    if guess == answer:
        correct_flag = True
    final = {}
    for i in range(5):
        letter = guess[i]
        if letter in answer:
            if letter == answer[i]:
                final[letter] = 'GREEN'
            else:
                final[letter] = 'YELLOW'
        else:
            final[letter] = 'BLACK'
    return final

def print_guess(dict):
    for letter in dict.keys():
        color = Fore.BLACK
        if dict[letter] == 'GREEN':
            color = Fore.GREEN
        elif dict[letter] == 'YELLOW':
            color = Fore.YELLOW
        else:
            color = Fore.BLACK
        print(color + letter, end=' ')
    print(Fore.RESET)


def print_lets(used):
    for x in list(string.ascii_uppercase):
        if x in used:
            if used[x] == 'GREEN':
                print(Fore.GREEN + x, end=' ')
            elif used[x] == 'YELLOW':
                print(Fore.YELLOW + x, end=' ')
            else:
                print(Fore.BLACK + x, end=' ')
        else:
            print(Fore.RESET + x, end=' ')
    print('\n')
                

words = import_words() 
unused_lets = list(string.ascii_uppercase)
used_lets = {} 
correct_flag = False

answer = random.choice(words).upper()
guess = take_input()
guess_results = check_guess(guess, answer)
print('your guess: ', end=''); print_guess(guess_results)
for letter in guess_results:
    used_lets[letter] = guess_results[letter]
print_lets(used_lets)


