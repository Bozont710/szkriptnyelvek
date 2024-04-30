#!/usr/bin/env python3

from prime import is_prime_mr

def main():
    primes1 = [n for n in range(1,100) if is_prime_mr(n)]
    print(primes1)
    primes2 = [n for n in range(1,200) if is_prime_mr(n)]
    print(sum(primes2))
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
