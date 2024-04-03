#!/usr/bin/env python3


def munchausen(start):
    square = 0
    end = 440000000
    end1 = 1000000
    while end1 <= end:
        for n in range(start, end1):
            for m in str(n):
                square += int(m)**int(m)
            if square == n:
                print(n)
            square = 0
        start = end1 + 1
        end1 *= 2
#ENDmunchausen


def main():
    munchausen(1)
    
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
