#!/usr/bin/env python3


def decode(str):
    ret = ""
    for n in str:
        if ord(n) <= 122 and ord(n) >= 65 and not (ord(n)<=96 and ord(n)>=91):
            if ord(n) > 120 and ord(n) < 122:
                ret += chr(ord(n)-24)
            elif ord(n) > 88 and ord(n) < 90:
                ret += chr(ord(n)-24)
            else:
                ret += chr(ord(n)+2)
        else:
            ret += n
    return ret
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
