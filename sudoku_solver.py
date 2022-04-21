from gettext import find
from typing import Tuple, List, Union
board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9] 
]

def print_board(brd) -> None:
    """
    Prints out <brd> in a nicely formatted 
    way
    """
    for r_index, row in enumerate(brd):
        print()
        if r_index % 3 == 0 and r_index != 0:
            print('-'*20)

        for c_index, col in enumerate(row):
            if c_index % 3 == 0 and c_index != 0:
                print('|', end='')
            
            print(f"{brd[r_index][c_index]}"+',', end='')
    print()

def find_empty(brd:List[List[int]]) -> Union[Tuple[int, int], None]:
    """
    Goes through <brd> and returns a tuple
    containing (row, col) of an empty spot
    """
    #i represents row and j represents col
    for i in range(len(brd)):
        for j in range(len(brd[i])):
            if brd[i][j] == 0:
                return (i, j) #(row, col)
    
    return None

def validate(brd:List[List[int]], pos: Tuple[int, int], num: int) -> bool:
    """
    check if <num> is a valid input for <pos>
    """
    row, col = pos
    r, c, s, =  True, True, True
    #Check Row
    if num in brd[row]:
        r = False
    #Check Col
    for i in range(len(brd)):
        if brd[i][col] == num:
            c = False
    #Check Square
    square = []
    srow = row // 3
    scol = col // 3
    for i in range(srow*3, srow*3+3):
        square.append(brd[i])
        for j in range(scol*3, scol*3+3):
            square.append(brd[i][j])
    if num in square:
        s = False
    
    return r and c and s


def solve(brd:List[List[int]]) -> None:
    """
    Solves a sudoku board
    """
    find = find_empty(brd)
    if find is None:
        return True
    else:
        row, col = find
    for x in range(1, 10):
        if validate(brd, (row, col), x):
            brd[row][col] = x
            if solve(brd):
                return True
            brd[row][col] = 0
    return False

print('UNSOLVED BOARD')
print_board(board)
solve(board)
print('\nSOLVED BOARD:')
print_board(board)