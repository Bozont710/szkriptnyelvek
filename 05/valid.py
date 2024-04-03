#!/usr/bin/env python3


def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    result = ""
    for n in text:
        for m in chars:
            if n==m:
              result += m
    return result
#ENDvalid


def main():
    print(valid("Barking!"))
    print(valid("KL754", "0123456789"))
    print(valid("BEAN", "abcdefghijklmnopqrstuvwxyz"))
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
