#!/usr/bin/env python3


def main():
    word = input("Please enter a word: ")
    if word == word[::-1]:
        print(f"{word} is a palindrome")
    else:
        print(f"{word} is NOT a palindrome")
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
