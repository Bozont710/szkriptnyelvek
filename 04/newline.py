#!/usr/bin/env python3

import sys
import random as r

UPTO = 100


def main():
    count = 0
    for i in range(UPTO):
        print(r.randint(0, 9), end="")
        count += 1
        if count % 10 == 0:
            print("\n")
    print()
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
