#!/usr/bin/env python3


def hangrend(w):
    mely = ["a", "á", "o", "ó", "u", "ú"]
    magas = ["e", "é", "i", "í", "ö", "ő", "ü", "ű"]
    ismely = False
    ismagas = False
    for n in w:
        for me in mely:
            if me == n:
                ismely = True
        for ma in magas:
            if ma == n:
                ismagas = True
    if ismely and ismagas:
        return "vegyes"
    elif ismagas:
        return "magas"
    elif ismely:
        return "mély"
    else:
        return "semmilyen"
#ENDhangrend


def main():
    word = input("Szó: ")
    print(f"A {word} hangrendje: {hangrend(word)}")
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
