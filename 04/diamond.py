#!/usr/bin/env python3


def diamond(sz):
    n = 1
    while n < sz:
        text = "*"*n 
        print(text.center(100))
        n += 2
    while n > 0:
        text = "*"*n 
        print(text.center(100))        
        n -= 2
#ENDdiamond


def main():
    size = int(input("Please enter an odd whole number: "))
    if (size % 2 == 0):
        print("Incorrect number")
    else:
        diamond(size)
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
