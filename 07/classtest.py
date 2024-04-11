#!/usr/bin/env python3


class Test:
    cnt = 0
    def __init__(self):
        Test.cnt += 1
#ENDTest


def main():
    print(Test.cnt)
    t1 = Test()
    t2 = Test()
    t3 = Test()
    print(Test.cnt)
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
