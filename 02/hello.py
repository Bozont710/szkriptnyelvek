#!/usr/bin/env python3


def hello(name, color, obj):
    #v1
    print("{0}, {1} az {2}!".format(name, color, obj))
    #v2
    print("{}, {} az {}!".format(name, color, obj))
    #v3
    print("{n}, {c} az {o}!".format(n=name.capitalize(), c=color, o=obj))
    #v4
    print(f"1 + 1 = {1+1}")
    print(f"{name}, {color} az {obj}!")
#ENDhello


def main():
    hello("Geza", "kek", "eg")
    print('-' * 50)
    hello("Julcsi", "piros", "auto")
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
