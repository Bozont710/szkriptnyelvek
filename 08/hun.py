#!/usr/bin/env python3

from enum import Enum
from enum import auto

class hangrendenum(Enum):
    MELY = auto()
    MAGAS = auto()
    VEGYES = auto()
    SEMMILYEN = auto()
    def hangrend(wrd):
        mely = "aáoóuú"
        magas = "eéiíöőüű"
        ismely = False
        ismagas = False
        for n in wrd:
            for me in mely:
                if n == me:
                    ismely = True
            for ma in magas:
                if n == ma:
                    ismagas = True
        if ismely and ismagas:
            return hangrendenum.VEGYES.name
        elif ismely:
            return hangrendenum.MELY.name
        elif ismagas:
            return hangrendenum.MAGAS.name
        else:
            return hangrendenum.SEMMILYEN.name

#ENDhangrendenum


def main():
    word = input("Szó: ")
    print(f"{word} hangrendje: {hangrendenum.hangrend(word)}")
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
