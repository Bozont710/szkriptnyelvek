#!/usr/bin/env python3


def generate(brd):
    stringboard = ""
    for n in brd:
        stringboard += n
    print(stringboard)
#ENDgenerate


def main():
    board0 = ['+', '-', '-', '-', '-', '-', '-', '-', '-', '+']
    board1 = ['|', '.', '.', '.', '.', '.', '.', '.', '.', '|']
    board2 = ['|', '.', '.', '.', '.', '.', '.', '.', '.', '|']
    board3 = ['|', '.', '.', '.', '.', '.', '.', '.', '.', '|']
    board4 = ['|', '.', '.', '.', '.', '.', '.', '.', '.', '|']
    board5 = ['|', '.', '.', '.', '.', '.', '.', '.', '.', '|']
    board6 = ['|', '.', '.', '.', '.', '.', '.', '.', '.', '|']
    board7 = ['|', '.', '.', '.', '.', '.', '.', '.', '.', '|']
    board8 = ['|', '.', '.', '.', '.', '.', '.', '.', '.', '|']
    board9 = ['+', '-', '-', '-', '-', '-', '-', '-', '-', '+']

    generate(board0)
    generate(board1)
    generate(board2)
    generate(board3)
    generate(board4)
    generate(board5)
    generate(board6)
    generate(board7)
    generate(board8)
    generate(board9)
    queenposition = [7,3,0,2,5,1,6,4]
    
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
