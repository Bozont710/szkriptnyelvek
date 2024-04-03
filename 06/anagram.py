#!/usr/bin/env python3


def isanagram(words):
    (one, two) = words
    one = normalize(one)
    two = normalize(two)
    two = list(two)
    for n in one:
        if n in two:
            two.remove(n)
        else:
            return False
    return True
#ENDisanagram


def normalize(wrd):
    ret = ""
    wrd = wrd.lower()
    lst = wrd.split()
    return ret.join(lst)
#ENDnormalize


def main():
    words1 = ("listen", "silent")
    words2 = ("A gentleman", "Elegant man")
    words3 = ("Clint Eastwood", "Old west action")
    words4 = ("dormitory", "dirty room")
    print(isanagram(words1))
    print(isanagram(words2))
    print(isanagram(words3))
    print(isanagram(words4))
    
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
