import random
import math
import os
import re
import time

max_trials = 5
sleep_time = 2

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
        answer = input(f"{i1} + {i2} = ")
        answer = int(re.sub('[^0-9]','', answer))
    
        if answer == i1 + i2:
            guessed = True
            break
        if trial < max_trials:
            print(f"Nope... try again! ({trial} of {max_trials})")
        else:
            input(f"Ops... The correct answer was {i1} + {i2} = {i1 + i2}")

    return guessed

def main():
    
    while True:
        os.system('cls')
        i1 = random.randint(0,11)
        i2 = random.randint(0,25)
        guessed = seek_input(i1, i2)
        
        if guessed:
            message = f"Correct!!! {random.choice(positive_messages)}"
            if sleep_time>0:
                print(message)
                time.sleep(sleep_time)
            else:
                input(message)
        




if __name__ == '__main__':
    try:
        main()
    except:
        pass
    finally:
        os.system('cls')