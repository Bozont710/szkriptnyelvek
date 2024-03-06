#!/usr/bin/env python3


def main():
    #request two integers from the user in string format
    num1 = input("Please enter two integers: ")
    num2 = input()

    #check for empty values
    if num1 == "" or num2 == "":
        print("error: enter two integers")
    else:
        #print and cast to integers
        print(f"{int(num1)} + {int(num2)} = {int(num1) + int(num2)}")
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
