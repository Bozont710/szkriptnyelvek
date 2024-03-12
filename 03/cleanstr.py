#!/usr/bin/env python3


def clean(str):
    cleaned = str.split()
    for n in cleaned:
        print(n)
    return cleaned
#ENDclean


def main():
    toclean1 = "192.20.246.138:\n 6666"
    toclean2 =  "206.130.99.82:\n8080"

    clean(toclean1)
    clean(toclean2)
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
