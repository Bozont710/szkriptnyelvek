#!/usr/bin/env python3

import sys


def hello(s):
    if s == "Batman" or s == "Robin":
        print("Bat danger!")
    else:
        print(f"Hello {s}!")
    #ENDif
#ENDhello


def main():
    name = sys.argv[1]
    hello(name)
#ENDmain


if __name__ == "__main__":
    main()
#ENDif
