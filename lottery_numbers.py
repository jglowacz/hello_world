'''
This program generates 6 random numbers for Polish Lotto Lottery.
The aim is to draw 6 unique numbers out of 49.
'''

# Module needed for drawing random numbers and for simulating draw.
import random, time
# Module needed to exit the program.
from sys import exit

MIN_RANDOM = 1
MAX_RANDOM = 49
RESULTS = []

def main():
    welcome_user()
    draw_numbers()
    continue_or_exit()

def welcome_user():
    USER_NAME_ASK = input('Please enter your name to start: ')
    USER_NAME = str(USER_NAME_ASK)
    GREETING = f'Hello {USER_NAME}!\nWelcome to the Lottery Numbers Generator!'
    print(GREETING)

def draw_numbers():
    load_results()
    for i in range(6):
        generate_numbers()
    show_results()

def load_results():
    WAITING_PROMPT = 'Please wait while your numbers are being drawn.'
    print(WAITING_PROMPT)
    time.sleep(5)

def generate_numbers():
    DRAW = random.randint(MIN_RANDOM, MAX_RANDOM)
    if DRAW in RESULTS:
        generate_numbers()
    else:
        RESULTS.append(DRAW)

def show_results():
    RESULTS.sort()
    FINAL_NUMBERS = ', '.join(str(r) for r in RESULTS)
    DISPLAY_FINAL_NUMBERS = f'Your lucky numbers are: {FINAL_NUMBERS}.'
    print(DISPLAY_FINAL_NUMBERS)
    time.sleep(5)

def continue_or_exit():
    USER_INPUT = input('Do you want to try once again? (y/n): ')
    ANSWER_YES = USER_INPUT.lower().startswith('y')
    ANSWER_NO = USER_INPUT.lower().startswith('n')
    if ANSWER_YES:
        repeat_code()
    elif ANSWER_NO:
        exit(0)
    else:
        continue_or_exit()

def repeat_code():
    RESULTS.clear()
    draw_numbers()
    continue_or_exit()

if __name__ == '__main__':
    main()