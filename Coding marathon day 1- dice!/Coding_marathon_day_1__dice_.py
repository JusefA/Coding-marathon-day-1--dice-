
#dice rolling game by Jussiboe
#29.6.2020


import random


def roll():
    c = int(input("how many times would you like to roll the dice?\n"))
    print([random.randint(1,6) for i in range(c)])
        
roll()


#Finished!