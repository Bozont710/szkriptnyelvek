#!/usr/bin/env python3


def bydigit(lst):
    digit = []
    for n in lst:
        n = list(str(n))
        for i in n:
            digit.append(int(i))
    return sum(digit)
#ENDbydigit


def main():
    hundred = list(range(1,101))
    print(f"regular list: {sum(hundred)}")
    print(f"sum of digits: {bydigit(hundred)}")
    
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
