#!/usr/bin/env python3


def main():
    word = input("Please enter a word: ")
    backwards = word[::-1]
    if word == backwards:
        print(f"{word} is a palindrome")
    else:
        print(f"{word} is not a palindrome")
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
