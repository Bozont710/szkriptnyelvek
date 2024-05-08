#!/usr/bin/env python3


def main() -> None:
    while True:
        try:
            num1 = float(input("1. num: "))
            num2 = float(input("2. num: "))
            result = num1 / num2
            print('result of divison: {0:.2f}'.format(result))
            print('-' * 10)
        except ValueError:
            print("input not a number, try again")
        except KeyboardInterrupt:
            quit()
        except EOFError:
            quit()
        except ZeroDivisionError:
            print("You can't divide with zero, try again")
            
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
