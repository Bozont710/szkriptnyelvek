#!/usr/bin/env python3


def main():
    file = open('pass2.txt', 'r')
    Lines = file.readlines()
    whatever = ""
    for line in Lines:
        shit = set(line.split())
        print(line)
        whatever.join(str(shit))
        whatever.split(',')
        print(whatever)
        if line == shit:
            pass#print(f"{line} is valid")
        else:
            pass#print(f"{line} is invalid")
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
