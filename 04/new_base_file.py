#!/usr/bin/env python3

import shutil
import os.path

def main():
    print("*"*27)
    print("Create an empty source file")
    print("*"*27)
    print("1) Python")
    print("2) Java")
    print("q) quit")

    option = input(">")
    if option == "q":
        quit()
    new_file = input("Please input the name of the new file(extension already included): ")
    if option == "1":
        if os.path.isfile(f"{new_file}.py"):
            print("file already exists")
        else:
            shutil.copy("base.py", new_file+".py")
    if option == "2":
        if os.path.isfile(f"{new_file}.java"):
            print("file already exists")
        else:
            shutil.copy("base.java", new_file+".java")
    
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
