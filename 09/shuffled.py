#!/usr/bin/env python3

import random

def shuffled(li):
    li1 = li[:]
    random.shuffle(li1)
    return li1
#ENDshuffled

def main():
    li = [1, 6, 3, 9, 3, 6, 2]
    print(shuffled(li)[-1])
    print(li)
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
