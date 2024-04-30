#!/usr/bin/env python3

from collections import deque

class myque:
    def __init__(self):
        self.data = []
        self.data2 = []
    #END__init_

    def append(self, elem):
        self.data.append(elem)
    #ENDappend

    def popleft(self):
        self.empty_list()
        res = self.refill()
        return res
    #ENDpopleft

    def refill(self):
        res = self.data.pop()
        while len(self.data2):
            self.data.append(self.data2.pop())
        return res
    #ENDrefill

    def empty_list(self):
        while not len(self.data) == 1:
            self.data2.append(self.data.pop())

        return self.data
    #ENDempty_list

    def size(self):
        return len(self.data)
    #ENDsize

    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False
    #ENDis_empty

    def __str__(self):
        return f"deque({self.data})"
    #END__str__
#ENDmyque


def main():
    my = myque()
    de = deque()
    my.append(3)
    my.append(5)
    my.append(8)
    my.append(0)
    de.append(3)
    de.append(5)
    de.append(8)
    de.append(0)
    print(f"myque: {my}")
    print(f"deque: {de}")
    print(f"myque popleft: {my.popleft()}")
    print(f"deque popleft: {de.popleft()}")
    print(my.size())
    print(my.is_empty())
    print(f"myque: {my}")
    my.append(3)
    print(f"myque: {my}")

    my.popleft()
    my.popleft()
    my.popleft()
    print(my.is_empty())
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
