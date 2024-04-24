#!/usr/bin/env python3
 
from collections import deque

class Myqueue:
    def __init__(self):
        self.data = []
        self.data2 = []
    #END__init__

    def append(self, elem):
        self.data.append(elem)
    #ENDappend

    def pop(self):
        return self.data.pop()
    #ENDpop

    def popleft(self):
        return self.data.pop(0)
    #ENDpopleft

    def is_empty(self):
        if self.size:
            return False
        else:
            return True
    #ENDis_empty

    def size(self):
        return len(self.data)
    
    def __str__(self):
        return f"deque({self.data})"
    #END__str__


#ENDMyqueue


def main():
    myq = Myqueue()
    que = deque([])
    myq.append(1)
    myq.append(3)
    myq.append(5)
    myq.append(9)
    que.append(1)
    que.append(3)
    que.append(5)
    que.append(9)
    print(f"myque: {myq}")
    print(f"deque: {que}")
    print(myq.popleft())
    print(que.popleft())
    print(myq.pop())
    print(que.pop())
    print(f"myque: {myq}")
    print(f"deque: {que}")
    print(myq.is_empty())
    print(myq.size())
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
