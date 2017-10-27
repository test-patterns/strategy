#!/usr/bin/env python
""" Sample problem featuring the strategy pattern. """

import argparse

from round import Round
from pizza import Pizza

def main():
    """ Execute the program """

    args = parse_args()

    size = int(args.length)
    if args.shape == 'round':
        dough = Round(size)

    pizza = Pizza(dough)
    output(args, pizza.get_dough_amount())

def output(args, ounces):
    print("The " + args.length + " inch, " + args.shape + " pizza needs " + str(ounces) + " ounces of dough.")

def parse_args():
    """ Parse input arguments """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s",
        "--shape",
        help="The shape of pizza to order (round/square).",
        required=True)
    parser.add_argument(
        "-l",
        "--length",
        help="The length or diameter of pizza to order.",
        required=True)
    return parser.parse_args()

if __name__ == "__main__":
    main()
