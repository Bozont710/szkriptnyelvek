#!/usr/bin/env python3


def main():
    message = ""
    with open("message.txt", 'r') as f1:
        for line in f1:
            (one, two) = line.split()
            message += chr(int(one,2))
            message += chr(int(two,2))
    print(message)
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
