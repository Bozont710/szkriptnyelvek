#!/usr/bin/env python3


class Greetings:
    def __init__(self, name):
        self.name = name
    #END__init__
        
    def say_hi(self):
        print(f"Hi, {self.name}!")
    #ENDsay_hi
#ENDGreetings


def main():
    g = Greetings("Barka")
    g.say_hi()
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
