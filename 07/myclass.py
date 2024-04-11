#!/usr/bin/env python3


class MyClass:
    def hello(self):
        return "Hello, World!"
    #ENDhello
#ENDPerson


class Hello():
    def create_name(self, name):
        self.name = name
    #ENDcreate_name
        
    
    def display_name(self):
        return self.name
    #ENDdisplay_name

    def greet(self):
        print(f"Hello, {self.name}!")
    #ENDgreet
#ENDHello


def main():
    o = MyClass()
    print(o.hello())

    h = Hello()
    h.create_name("Barka")
    print(h.display_name())
    h.greet()
    print(h.name)
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
