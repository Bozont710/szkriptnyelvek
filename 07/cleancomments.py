#!/usr/bin/env python3


def main():
    with open("string1.py", "r") as f1, open("string1_clean.py", 'w') as f2:
        for line in f1:
            line1 = line.lstrip()
            if not line1.startswith('#'):
                print(line, file=f2)
            
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
