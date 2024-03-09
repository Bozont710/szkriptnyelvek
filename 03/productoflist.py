#!/usr/bin/env python3


def product(li):
    prod = 1
    for n in li:
        prod = prod * n
    return prod
#ENDproduct

def main():
    li = [1, 2, 3, 4, 5, 6]
    print(product(li))
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
