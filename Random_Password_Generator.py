''' 
Random Password Generator

Project by Jacek Glowacz
Code in Place 2021
'''

# Importing needed libraries

import random, string
import PySimpleGUI as sg
from tkinter import Tk

# Creating concatenated string of text that will serve as basis to password generation

string_of_charts = string.ascii_letters + string.digits + string.punctuation
list_of_charts = list(string_of_charts)

# Defining function that generates strong password

def password_generate():
    passwd = []
    for x in range(14):
        x = random.choice(list_of_charts)
        passwd.append(x)
    password = ''.join(passwd)
    return password

# Theme and layout of PySimpleGUI interface

sg.theme('LightGreen2')
sg.theme_text_color('Green')
sg.theme_input_text_color('Green')
layout = [[sg.Text('Click "Run" to generate your strong password. Click "Copy" to save the password to the clipboard.', font = 'Helvetica, 14')],
          [sg.Input(size=(40, 2), font = 'Helvetica, 30', key = 'passwd')], [[sg.Button('Run'), sg.Button('Copy')]]]
window = sg.Window("Strong Password Generator", layout, finalize = True)

# Main function in the loop allowing PySimpleGUI interface to run

def main():

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == 'Run':
            password = password_generate()
            window['passwd'].update(password)
        elif event == 'Copy':
            hide_this_window = Tk()
            hide_this_window.clipboard_append(password)
            hide_this_window.destroy()

if __name__ == "__main__": 
    main()




