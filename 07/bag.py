#!/usr/bin/env python3


class Bag:
    def __init__(self):
        self.data = []
    #END__init__
        

    def add(self, value):
        self.data.append(value)
    #ENDadd
        
    
    def add_twice(self, value):
        self.add(value)
        self.add(value)
    #ENDadd_twice
        
    
    def __str__(self):
        return f"Bag({self.data})"
    #END__str__
#ENDBag


def main():
    b = Bag()
    b.add(5)
    print(b)
    b.add(3)
    print(b)
    b.add_twice(9)
    print(b)
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
