#!/usr/bin/env python3


def greet(name, greetings="Hello"):
    print(f"{greetings}, {name}!")
#ENDgreet


def sum_digits(n):
    return sum([int(c) for c in str(n)])
#ENDsum_digits


def hello(name, repeat=1, postfix=""):
    for i in range(repeat):
        print(f"{name}{postfix}")
#ENDhello


def main():
    listone = ['auto', 'villamos', 'metro']
    one = [n.upper() for n in listone]
    print(f"first: {one}")

    listtwo = ['aladar', 'bela', 'cecil']
    two = [n.capitalize() for n in listtwo]
    print(f"second: {two}")

    listthree = [ 0 for i in range(10)]
    print(f"third: {listthree}")

    listfour = [n for n in range(1,11)]
    four = [n*2 for n in listfour]
    print(f"fourth: {listfour}")
    print(f"fourth: {four}")

    listfive = [str(n) for n in range(1,11)]
    five = [int(n) for n in listfive]
    print(f"fifth: {listfive}")
    print(f"fifth: {five}")

    listsix = "1234567"
    six = list(listsix)
    six2 = [int(n) for n in six]
    print(f"sixth: {six2}")


    list100 = sum([sum_digits(n) for n in range(1,101)])
    print(f"sum of digits: {list100}")

    li = ["alfa", "beta", "gamma"]
    for index, elem in enumerate(li, start=1):
        print(index, elem)

    greet("Barka")
    greet("Barka", greetings="Hola")
    greet("Barka", greetings="Bonjour")


    hello("Barka")
    hello("Barka", repeat=4)
    hello("Barka", repeat=2, postfix="!")
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
