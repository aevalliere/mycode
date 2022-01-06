#!/usr/bin/env python3
"""Author: Alex Valliere | Learning functions"""

import crayons
def zork():
    """This function prints strings in red, red white and blue, and with the crayon feature disabled"""
    #print red string in red
    print(crayons.red('red string'))

    #Red white blue
    print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))


def zero():
    """This string prints in other colors and in bold"""

    # print 'red string' in red
    print(crayons.red('red string', bold=True))

    # print 'yellow string' in yellow
    print(crayons.yellow('yellow string', bold=True))

    # print 'magenta string' in magenta
    print(crayons.magenta('magenta string', bold=True))

    # print 'white string' in white
    print(crayons.white('white string', bold=True))

def name():
    """Prints my name in blue"""
    print(crayons.blue('Alex'))

def main():
    zero()
    zork()
    name()

if __name__ == "__main__":
    main()
