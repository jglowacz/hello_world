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
results = []

def main():
    welcome_user()
    draw_numbers()
    continue_or_exit()

def welcome_user():
    ask_user_name = input('Please enter your name to start: ')
    user_name = str(ask_user_name)
    greeting = f'Hello {user_name}!\nWelcome to the Lottery Numbers Generator!'
    print(greeting)

def draw_numbers():
    load_results()
    for i in range(6):
        generate_numbers()
    show_results()

def load_results():
    waiting_prompt = 'Please wait while your numbers are being drawn.'
    print(waiting_prompt)
    time.sleep(5)

def generate_numbers():
    draw = random.randint(MIN_RANDOM, MAX_RANDOM)
    if draw in results:
        generate_numbers()
    else:
        results.append(draw)

def show_results():
    results.sort()
    final_numbers = ', '.join(str(r) for r in results)
    display_final_numbers = f'Your lucky numbers are: {final_numbers}.'
    print(display_final_numbers)
    time.sleep(5)

def continue_or_exit():
    user_input = input('Do you want to try once again? (y/n): ')
    answer_yes = user_input.lower().startswith('y')
    answer_no = user_input.lower().startswith('n')
    if answer_yes:
        repeat_code()
    elif answer_no:
        exit(0)
    else:
        continue_or_exit()

def repeat_code():
    results.clear()
    draw_numbers()
    continue_or_exit()

if __name__ == '__main__':
    main()