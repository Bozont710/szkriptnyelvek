#!/usr/bin/env python3

from prime import is_prime_mr


def is_palindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False
#ENDpalindrome


def prime_palindrome(num):   
    while True:
        if is_palindrome(num):
            if  is_prime_mr(num):
                return num
            else:
                num += 1
        else:
            num += 1

#ENDprime_palindrome


def main():
    num1 = 31
    num2 = 130
    num3 = 131
    num4 = 1977
    print(prime_palindrome(num1))
    print(prime_palindrome(num2))
    print(prime_palindrome(num3))
    print(prime_palindrome(num4))    
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
