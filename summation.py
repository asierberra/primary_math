import random
import math
import os
import re
import time
from collections import OrderedDict


max_trials = 3
sleep_time = 2
session_size = 10

max_integer = 50
max_small_int = 10

positive_messages = [
    ':-)',
    'Great!!',
    'Nice!!',
    'Awesome!!',
    'Well done!!',
    'Keep it up!!',
    'I like it!!',
    'Cheers!!',
]


def seek_input(i1, i2):
    trial = 0
    guessed = False
    for  trial in range(1, max_trials+1):
        answer = ''
        while answer == '':
            answer = input(f"  {i1} + {i2} = ")
            answer = re.sub(r'[\+\-\*\/\,\.]','', answer)
        answer = re.sub('[^0-9]','', answer)
        answer = int(answer)
    
        if answer == i1 + i2:
            guessed = True
            break
        if trial < max_trials:
            print(f"Nope... try again! (attempt {trial} of {max_trials})")
        else:
            input(f"\nOps... The correct answer was {i1} + {i2} = {i1 + i2}")

    return guessed


def summary_to_str(summary):
    os.system('cls')
    txt = 'Here is your summary: \n \n'
    for s in summary:
        if s[2]:
            guessed = 'v'
        else:
            guessed = 'XXX'
        txt = (txt  + '  ' +
               guessed.ljust(5) + 
               str(s[0]).ljust(3) +  ' + ' + 
               str(s[1]).ljust(3) +  ' = ' + 
               str(s[0] + s[1])) + '\n'
    return txt


def enquiry_session():

    base_int = random.randint(1, 10)
    narrow_down_integers = [i for i in range(max_small_int+1) if i%10==base_int]
    summary = []

    for question in range(1, session_size+1):
        os.system('cls')
        print(f"Question {question} of {session_size}: \n")

        i1 = random.randint(0,max_integer)
        i2 = random.choice(narrow_down_integers)
        guessed = seek_input(i1, i2)
        
        summary.append((i1, i2, guessed))

        if guessed:
            message = f"\nCorrect!!! {random.choice(positive_messages)}"
            if sleep_time>0:
                print(message)
                time.sleep(sleep_time)
            else:
                input(message)
    
    input(summary_to_str(summary))


def main():
    
    while True:
        enquiry_session()
        




if __name__ == '__main__':
    try:
        main()
    except:
        pass
    finally:
        os.system('cls')