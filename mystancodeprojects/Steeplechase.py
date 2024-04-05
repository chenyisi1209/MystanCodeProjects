"""
File: Steeplechase.py
Name: YiSi
---------------------------------
This program makes Karel climb all obstacles
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(7):
        if front_is_clear():
            move()
            jump()
            turn_left()
        else:
            jump()
            turn_left()
def jump():
    """
    Pre-condition:Karel is on the left side of the wall,facing East
    Past-condition:Karel is on the right side of the wall
    """
    up()
    cross()
    down()
def up():
    while not front_is_clear():
        turn_left()
        move()
        turn_right()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def cross():
    move()
    turn_right()
def down():
    while front_is_clear():
        move()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
