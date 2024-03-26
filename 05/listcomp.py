#!/usr/bin/env python3


def greet(name, greetings="Hello"):
    print(f"{greetings}, {name}!")
#ENDgreet


def sum_digits(n):
    return sum([int(c) for c in str(n)])
#ENDsum_digits


def hello(name, repeat=1, postfix=""):
    """this is a docstring"""
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
    print(f"fourth: {four}")

    listfive = [str(n) for n in range(1,11)]
    five = [int(n) for n in listfive]
    print(f"fifth: {five}")

    listsix = "1234567"
    six = list(listsix)
    six2 = [int(n) for n in six]
    print(f"sixth: {six2}")

    listseven = "The quick brown fox jumps over the lazy dog"
    seven = [len(n) for n in listseven.split()]
    print(f"seventh: {seven}")

    listeight = "python is an awesome language"
    eight = [n[0] for n in listeight.split()]
    print(f"eighth: {eight}")

    listnine = "The quick brown fox jumps over the lazy dog"
    nine = [(n, len(n)) for n in listnine.split()]
    print(f"ninth: {nine}")

    listten = list(range(0,10,2))
    print(f"tenth: {listten}")

    listeleven = range(0,20)
    eleven = [n**2 for n in listeleven]
    for n in eleven:
        if n % 2 == 0:
            pass
        else:
            eleven.remove(n)
    print(f"eleventh: {eleven}")

    
    listtwelve = range(0,20)
    twelve1 = [n**2 for n in listtwelve]
    twelve = []
    for n in twelve1:
        if str(n)[-1] == "4":
            twelve.append(n)
    print(f"twelvth: {twelve}")

    listthirteen = range(65, 91)
    thirteen1 = [chr(n) for n in listthirteen]
    word = ""
    for n in thirteen1:
        word += n
    print(f"thirteenth: {word}")

    listfourteen = [" apple ", " banana ", " kiwi "]
    fourteen = [n.split() for n in listfourteen]
    print(f"fourteenth: {fourteen}")

    listfifteen = [1, 0, 1, 1, 0, 1, 0, 0]
    word1 = ""
    for n in listfifteen:
        word1 += str(n)
    print(f"fifteenth: {word1}")

    #list100 = sum([sum_digits(n) for n in range(1,101)])
    #print(f"sum of digits: {list100}")

    #li = ["alfa", "beta", "gamma"]
    #for index, elem in enumerate(li, start=1):
    #    print(index, elem)

    #greet("Barka")
    #greet("Barka", greetings="Hola")
    #greet("Barka", greetings="Bonjour")


    #hello("Barka")
    #hello("Barka", repeat=1)
    #hello("Barka", repeat=1, postfix="!")
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
