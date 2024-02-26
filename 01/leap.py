#!/usr/bin/env python3

def main():
    year = int(input("Year: "))
    nextleap = year
    print(isleap(1900))
    if isleap(year):
            nextleap = findnext(nextleap)
            print(f"The next leap year after {year} is {nextleap}")
    else:
        nextleap = findnext(nextleap)
        print(f"The next leap year after {year} is {nextleap}")
        

#ENDmain


def findnext(y):
    while True:
        y += 1
        if isleap(y):
            return y
#ENDfindnext


def isleap(y):
    if y % 4 == 0 and y % 100 != 0:
        return True
    elif y % 4 == 0 and y % 100 == 0 and y % 400 == 0:
        return True
    else:
        return False
#ENDisleap


if __name__ == "__main__":
    main()
#ENDif
