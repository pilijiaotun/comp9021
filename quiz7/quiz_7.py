# Written by *** for COMP9021
#
# Randomly fills an array of size 10x10 with True and False,
# displayed as 1 and 0, and outputs the number of chess knights
# needed to jump from 1s to 1s and visit all 1s (they can jump back
# to locations previously visited).


from random import seed, randrange
import sys


dim = 10

def display_grid():
    for row in grid:
        print('    ', ' '.join(str(int(e)) for e in row))

try:
    for_seed, n = (int(i) for i in input('Enter two integers: ').split())
    if not n:
        n = 1
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
if n > 0:
    grid = [[randrange(n) > 0 for _ in range(dim)] for _ in range(dim)]
else:
    grid = [[randrange(-n) == 0 for _ in range(dim)] for _ in range(dim)]    
print('Here is the grid that has been generated:')
display_grid()

# INSERT YOUR CODE HERE
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == True:
            grid[i][j] = 1
        else:
            grid[i][j] = 0

import numpy as np
d = np.array([0,0,0,0,0,0,0,0,0,0])
c = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grid = np.insert(grid,0,d,0)
grid = np.insert(grid,0,d,0)
grid = np.append(grid,[[0,0,0,0,0,0,0,0,0,0]],axis=0)
grid = np.append(grid,[[0,0,0,0,0,0,0,0,0,0]],axis=0)
grid = np.c_[grid,c]
grid = np.c_[grid,c]
grid = np.c_[c,grid]
grid = np.c_[c,grid]

sum = 0
complex1 = []
for i in range(2,12):
    for j in range(2,12):
        if grid[i][j] == 1:
            if grid[i-1][j-2] == 0 and grid[i-2][j-1] == 0 and grid[i-2][j+1] == 0 and grid[i-1][j+2] == 0 and grid[i+1][j+2] == 0\
                and grid[i+2][j+1] == 0 and grid[i+1][j-2] == 0 and grid[i+2][j-1] == 0:
                grid[i][j] = 0
                sum = sum+1
            else:
                complex1.append([i,j])

board = grid
def patrol(board, row, col,step=1):
    if  board[row][col] == 1:
        board[row][col] = step
        if step == len(complex1)-2:
            return
        patrol(board, row - 2, col - 1,step+1)
        patrol(board, row - 1, col - 2,step+1)
        patrol(board, row + 1, col - 2,step+1)
        patrol(board, row + 2, col - 1,step+1)
        patrol(board, row + 2, col + 1,step+1)
        patrol(board, row + 1, col + 2,step+1)
        patrol(board, row - 1, col + 2,step+1)
        patrol(board, row - 2, col + 1,step+1)
        board[row][col] == 0

for i in range(len(complex1)):
    patrol(board,complex1[i][0],complex1[i][1])

number1 = 0
for i in board:
    for j in i:
        if j == 2:
            number1 = number1 + 1

number2 = sum+number1
if number2 == 0:
    print()
    print('No chess knight has explored this board.')
elif number2 == 1:
    print()
    print('At least 1 chess knight have explored this board.')
else:
    print()
    print('At least %d chess knights have explored this board.'%number2)

