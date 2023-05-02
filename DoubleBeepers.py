"""
File: DoubleBeepers.py
Name:邱淑雅
-------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will double the beepers
    """
    move()
    double_beeper()
    beeper_go_home()
def double_beeper():
    while on_beeper():
        #old beeper,facing east
        pick_beeper()
        move()
        put_beeper()
        put_beeper()
        # new beeper,facing east
        turn_around()
        move()
        turn_around()
    move()
    while on_beeper():
        pick_beeper()
        turn_around()
        move()
        put_beeper()
        turn_around()
        move()
    turn_around()
    move()
    move()
    turn_around()


    # pick_beeper()
    # turn_left()
    # turn_left()
    # turn_left()
    # put_beeper()
    # beeper_go_home()
def turn_around():
    turn_left()
    turn_left()

# def beeper_go_home():









# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
