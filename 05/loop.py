#!/usr/bin/env python3


def loop(n, debug=False):
    """This function takes an 'n' variable which marks the end of the loop, and an optional debug variable that adds strings"""
    i = 0
    if debug:
        print("#ciklus kezdete")
    print(list(range(1,n+1)))
    if debug:
        print("#ciklus vége")
#ENDloop


def main():
    loop(5)
    loop(7, debug=True)
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
