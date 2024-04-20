"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Kateřina Bálint
email: k.svobodova.8@seznam.cz
discord: katerinabalint_41161
"""

import random


def create_number() -> list:
    """
    Generates a random 4-digit number that does not start with 0 and does not contain any duplicate digits.
    """
    random_number = list()
    random_number.append(random.randrange(1, 10))
    while len(random_number) <= 3:
        next_digit = random.randrange(10)
        if next_digit not in random_number:
            random_number.append(next_digit)
    return random_number


created_number = create_number()


def evaluate_guess() -> str:
    """
    Evaluates if the user's input meets all criteria: the input is numeric, has 4 unique digits a and does not start with 0.
    """
    evaluating = True
    while evaluating:
        user_number = input('Enter a number: ')
        if len(user_number) != 4:
            print(f'Your number doesn\'t consist of 4 digits. Try again.\n{line}')
            continue
        elif user_number[0] == '0':
            print(f'Your number starts with 0. Try again.\n{line}')
            continue
        elif not user_number.isdigit():
            print(f'You\'ve entered invalid characters. Try again.\n{line}')
            continue
        elif len(set(user_number)) < 4:
            print(f'Your number contains duplicate digits. Try again.\n{line}')
            continue
        else:
            evaluating = False
    return user_number


def convert_guess() -> list:
    """
    Converts the user's input from a string into a list of integers.
    """
    for number in guessed_number:
        converted_number.append(int(number))


line = 51 * '-'
print('Hi there!', line, 'I\'ve generated a random 4 digit number for you.', 'Let\'s play a bulls and cows game.', line, sep='\n')
converted_number = list()


bulls = 0
guesses = 0

while bulls < 4:
    bulls = 0
    cows = 0
    guessed_number = evaluate_guess()
    convert_guess()
    for digit in created_number:
        if digit not in converted_number:
            continue
        if digit in converted_number and created_number.index(digit) != converted_number.index(digit):
            cows += 1
        if digit in converted_number and created_number.index(digit) == converted_number.index(digit):
            bulls += 1
    guesses += 1
    cows_numeration = 'cow'
    bulls_numeration = 'bull'
    if cows != 1:
        cows_numeration = 'cows'
    if bulls != 1:
        bulls_numeration = 'bulls'
    print(f'{line} \n>>> {guessed_number} \n{bulls} {bulls_numeration}, {cows} {cows_numeration} \n{line}')
    converted_number.clear()
else:
    if guesses == 1:
        print(f'Correct, you\'ve guessed the right number \nin 1 guess! \n{line}')
    else:
        print(f'Correct, you\'ve guessed the right number \nin {guesses} guesses! \n{line}')


if guesses <= 6:
    print('That\'s amazing!')
elif 6 < guesses <= 12:
    print('That\'s average.')
elif 12 < guesses <= 18:
    print('That\'s not so good.')
else:
    print('That\'s lame.')