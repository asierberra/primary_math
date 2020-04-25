import random
import math
import os
import re

max_trials = 5

def main():
    os.system('cls')
    
    while True:
        i1 = random.randint(0,11)
        i2 = random.randint(0,25)

        trial = 0
        while  trial < max_trials:
            answer = input(f"{i1} + {i2} = ")
            if answer == 'e':
                exit()
            else:
                answer = int(re.sub('[^0-9]','', answer))
            
            if answer == i1 + i2:
                guessed = True
                break
            print("Thats's not it... try again!")
            trial += 1
        else:
            guessed = False

        if guessed:
            input(f"Correct!!! ")
        else:
            input(f"Ops, those where not the answers... The correct answer was {i1} + {i2} = {i1 + i2} \n")
        
        os.system('cls')
        




if __name__ == '__main__':
    main()