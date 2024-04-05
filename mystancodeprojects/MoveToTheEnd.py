"""
File: MoveToTheEnd.py
Name:YiSi
------------------------
This file shows how to use while loop
to walk to the end of a certain row in
karel world
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will move to the end and fill up of the first Street in any world
    """
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()


    # When front is not clear
# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
