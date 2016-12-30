#!/usr/bin/python3

from random import Random
import sys


def badArgument():
    print('Requires 1 integer argument', file=sys.stderr)
    sys.exit(1)


def shuffle(rng, n):
    if n > 1:
        print('Take pile of {0} cards.'.format(n))
        aCards = n // 2
        bCards = aCards + n % 2
        selection = [True] * aCards + [False] * bCards
        rng.shuffle(selection)
        while selection:
            i = 1
            first = selection[0]
            while i < len(selection) and selection[i] == first:
                i += 1
            try:
                input('{0} to {1}'.format(i, 'A' if first else 'B'))
            except EOFError:
                print()
                sys.exit()
            selection = selection[i:]
        shuffle(rng, aCards)
        shuffle(rng, bCards)


def main():
    rng = Random()
    try:
        shuffle(rng, int(sys.argv[1]))
    except ValueError:
        badArgument()


if len(sys.argv) < 2:
    badArgument()
main()
