from colorama import Fore, Style
import string
import random
import os

def import_words():
    with open('words.txt', 'r') as file:
        words = file.read().split()
    return words

def choose_word(words):
    return random.choice(words).upper()

def check_input(word):
    return word.isalpha() and len(word) == 5

def take_input(words):
    while True:
        guess = input('enter a five-letter word for your guess: ').strip().lower()
        if not check_input(guess):
            print('invalid input! please enter a five-letter word. ')
        else:
            return guess.upper()

def check_guess(guess, answer):
    result = {}
    answer_freq = {letter: answer.count(letter) for letter in set(answer)}
   
    for i in range(5):
        letter = guess[i]
        if letter == answer[i]:
            result[i] = (letter, 'GREEN')
            answer_freq[letter] -= 1  

    for i in range(5):
        letter = guess[i]
        if i in result:  
            continue
        if letter in answer and answer_freq[letter] > 0:
            result[i] = (letter, 'YELLOW')
            answer_freq[letter] -= 1
        else:
            result[i] = (letter, 'BLACK')

    return result

def print_guess(result):
    for i in range(5):
        letter, color = result[i]
        if color == 'GREEN':
            print(Fore.GREEN + letter, end=' ')
        elif color == 'YELLOW':
            print(Fore.YELLOW + letter, end=' ')
        else:
            print(Fore.BLACK + letter, end=' ')
    print(Style.RESET_ALL)

def print_lets(used):
    for x in string.ascii_uppercase:
        if x in used:
            if used[x] == 'GREEN':
                print(Fore.GREEN + x, end=' ')
            elif used[x] == 'YELLOW':
                print(Fore.YELLOW + x, end=' ')
            else:
                print(Fore.BLACK + x, end=' ')
        else:
            print(Fore.RESET + x, end=' ')
    print('\n' + Style.RESET_ALL)

def reprint(past_guesses, used_lets):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('=================== my wordle!! ===================\n')
    for guess_result in past_guesses:
        print('                    ', end='')
        print_guess(guess_result)
    print('\n')
    print_lets(used_lets)

words = import_words()
answer = choose_word(words)
unused_lets = set(string.ascii_uppercase)
used_lets = {}
past_guesses = []
correct_flag = False

for attempt in range(6):
    print(f"\nattempt {attempt + 1} of 6")
    guess = take_input(words)
    guess_results = check_guess(guess, answer)
    past_guesses.append(guess_results)

    for i in range(5):
        letter, color = guess_results[i]
        used_lets[letter] = color
   
    reprint(past_guesses, used_lets)

    if guess == answer:
        correct_flag = True
        print(Fore.GREEN + f"   congratulations! you guessed the word: {answer.upper()}\n" + Style.RESET_ALL)
        break

if not correct_flag:
    print(Fore.RED + f"      game over! the correct word was: {answer}\n" + Style.RESET_ALL)
