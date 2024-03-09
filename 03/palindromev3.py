#!/usr/bin/env python3


def recPal(str, s, e):
    if s == e:
        return True
    
    if str[s] != str[e]:
        return False
    
    if s < e:
        return recPal(str, s+1, e-1)
    return True

def isPalindrome(str):
    l = len(str)
    if l == 0:
        return True
    return recPal(str, 0, l-1)
#ENDisPalindrome


def main():
    word = input("Please enter a word: ")
    print(isPalindrome(word))
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
