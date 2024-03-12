#!/usr/bin/env python3


def decode(str):
    str = str.replace("A", "C")
    str = str.replace("C", "E")
    str = str.replace("D", "F")
    str = str.replace("Y", "A")
    str = str.replace("a", "c")
    str = str.replace("b", "d")
    str = str.replace("c", "e")
    str = str.replace("e", "g")
    str = str.replace("g", "i")
    str = str.replace("h", "j")
    str = str.replace("k", "m")
    str = str.replace("l", "n")
    str = str.replace("m", "o")
    str = str.replace("n", "p")
    str = str.replace("p", "r")
    str = str.replace("q", "s")
    str = str.replace("r", "t")
    str = str.replace("s", "u")
    str = str.replace("t", "v")
    str = str.replace("w", "y")
    str = str.replace("x", "z")
    str = str.replace("y", "a")
    return str
#ENDdecode
#abcdefghijklmnopqrstuvwxyz

def main():
    mess = """Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb"""

    mess = decode(mess)
    print(mess)
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
