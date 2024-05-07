#!/usr/bin/env python3


def is_palindrome_in_two_num_sys(num):
    result = 0
    for n in range(1, num):
        num2 = bin(n)[2:]
        if str(n) == str(n)[::-1] and str(num2) == str(num2)[::-1]:
            result += n
    return result
#ENDis_palindrome_in_two_num_sys


def main():
    num = 1000000
    print(is_palindrome_in_two_num_sys(num))
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
