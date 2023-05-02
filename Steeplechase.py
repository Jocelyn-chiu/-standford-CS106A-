"""
File: Steeplechase.py
Name: 邱淑雅
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():

    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()
            turn_left()

def jump():
    """
    pre-condition:karel is on the left,facing east
    post-condition:karel is on the right
    """
    up()
    cross()
    down()
def up():
    """
    pre-condition:karel is on the left,facing east
    post-condition:pass
    """
    while not front_is_clear():
        turn_left()
        move()
        turn_right()
def cross():
    """
    pre-condition
    post - condition:
    """
    move()
    turn_right()
def down():
    while front_is_clear():
        move()
def turn_right():
    turn_left()
    turn_left()
    turn_left()






# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
