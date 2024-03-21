#!/usr/bin/env python3


def loop(num, debug=False):
    list = range(1,num+1)
    if debug:
        print("# ciklus eleje")
    for n in list:
        print(n)
    if debug:
        print("# ciklus vege")
#ENDloop


def main():
    loop(5)
    loop(7, debug=True)
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
