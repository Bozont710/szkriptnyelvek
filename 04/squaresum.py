#!/usr/bin/env python3


def squaresum():
    nums = list(range(1,101))
    sum1 = 0
    for n in nums:
        sum1 += n**2
    sum2 = 0
    for n in nums:
        sum2 += n
    sum2 = sum2**2
    return sum2 - sum1
#ENDsquaresum


def main():
    print(squaresum())
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
