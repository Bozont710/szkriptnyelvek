#!/usr/bin/env python3

#import sys this way we can use the arguments straight from the command line
import sys

def main():
    #print and cast to int since it defaults as string
    print(f"{sys.argv[1]} + {sys.argv[2]} = {int(sys.argv[1]) + int(sys.argv[2])}")
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
