"""
File: PotholeFilling.py
Name: YiSi
--------------------------
This program shows karel filling 3
potholes.
"""

from karel.stanfordkarel import *


def main():
    """
    Pre-condition:
    Post-condition:
    """
    for i in range(3):
        go_in()
        put_99_beepers()
        go_out()
def go_in():
    move()
    turn_right()
    move()
def go_out():
    turn_left()
    turn_left()
    move()
    turn_right()
    move()
def put_99_beepers():
    for i in range(99):
        put_beeper()
def turn_right():
    for i in range(3):
        turn_left()


# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
