#!/usr/bin/env python3


def decode(str):
    for n in str:
        print(f"before{ord(n)}")
        new = ord(n) + 2
        print(f"new {chr(new)}")
        str = str.replace(n,chr(new))
        print(f"after{n}")
    return str
#ENDdecode


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
