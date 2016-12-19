#!/usr/bin/python3

from random import Random
import sys


def badArgument():
    print('Requires 1 integer argument', file=sys.stderr)
    sys.exit(1)


def shuffle(n, rng):
    if n > 1:
        print('Take pile of {0} cards.'.format(n))
        aCards = n // 2
        bCards = aCards
        if n % 2:
            bCards += 1
        selection = [True] * aCards + [False] * bCards
        rng.shuffle(selection)
        while selection:
            i = 1
            while i < len(selection) and selection[i] == selection[0]:
                i += 1
            pile = 'A' if selection[0] else 'B'
            print('{0} to {1}'.format(i, pile), end='')
            selection = selection[i:]
            try:
                input()
            except EOFError:
                print()
                sys.exit()
        shuffle(aCards, rng)
        shuffle(bCards, rng)


if len(sys.argv) < 2:
    badArgument()

# Main program
rng = Random()
try:
    shuffle(int(sys.argv[1]), rng)
except ValueError:
    badArgument()