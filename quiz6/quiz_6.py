# Written by *** for COMP9021
#
# Randomly generates a grid with 0s and 1s, whose dimension is
# controlled by user input, as well as the density of 1s
# in the grid, and finds out, for a given direction being
# one of N, E, S or W (for North, East, South or West)
# and for a given size greater than 1, the number of triangles
# pointing in that direction, and of that size.
#
# Triangles pointing North:
# - of size 2:
#   1
# 1 1 1
# - of size 3:
#     1
#   1 1 1
# 1 1 1 1 1
#
# Triangles pointing East:
# - of size 2:
# 1
# 1 1
# 1
# - of size 3:
# 1
# 1 1
# 1 1 1 
# 1 1
# 1
#
# Triangles pointing South:
# - of size 2:
# 1 1 1
#   1
# - of size 3:
# 1 1 1 1 1
#   1 1 1
#     1
#
# Triangles pointing West:
# - of size 2:
#   1
# 1 1
#   1
# - of size 3:
#     1
#   1 1
# 1 1 1 
#   1 1
#     1
#
# The output lists, for every direction and for every size,
# the number of triangles pointing in that direction and of that size,
# provided there is at least one such triangle.
# For a given direction, the possible sizes are listed
# from largest to smallest.
#
# We do not count triangles that are truncations of larger triangles,
# that is, obtained from the latter by ignoring at least one layer,
# starting from the base.


from random import seed, randint
import sys
from collections import defaultdict


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0))
                                  for j in range(len(grid))
                              )
             )

try:
    arg_for_seed, density, dim =\
        (int(e) for e in input('Enter three nonnegative integers: ').split())
    if arg_for_seed < 0 or density < 0 or dim < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()

# INSERT YOUR CODE HERE
def roate(a):
    a = list(zip(*a[::-1]))
    a = np.array(a)
    return a

import numpy as np
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j]>1:
            grid[i][j] = 1

if len(grid[0])%2 ==1:
    size = int((len(grid[0])+1)/2)
elif len(grid[0])%2 == 0:
    size = int(len(grid[0])/2)

c = []
d = []
for q in range(size,1,-1):
    line1 = 0
    for i in range(len(grid[0])-q+1):
        for j in range(q-1,len(grid)-q+1):
            size1 = 2
            while size1>0:
                if ([(i,j)]) in c:
                    break
                else:
                    if grid[i][j] == 1:
                        if list(grid[i+size1-1][j+1-size1:j+size1]) == [1]*(2*size1-1):
                            size1 = size1 + 1
                            if size1==q+1:
                                line1=line1+1
                                c.append([(i,j)])
                                break
                        else:
                            break
                    else:
                        break
    if line1 != 0:
        d.append((line1,q))
if len(d)>0:
    print()
    print('For triangles pointing N, we have:')
for i in range(len(d)):
    if d[i][0]>0:
        if d[i][0]>1:
            print('     %d'%d[i][0],'triangles of size %d'%d[i][1])
        elif d[i][0]==1:
            print('     %d'%d[i][0],'triangle of size %d'%d[i][1])
grid = roate(grid)
grid = roate(grid)
grid = roate(grid)

c = []
d = []
for q in range(size,1,-1):
    line1 = 0
    for i in range(len(grid[0])-q+1):
        for j in range(q-1,len(grid)-q+1):
            size1 = 2
            while size1>0:
                if ([(i,j)]) in c:
                    break
                else:
                    if grid[i][j] == 1:
                        if list(grid[i+size1-1][j+1-size1:j+size1]) == [1]*(2*size1-1):
                            size1 = size1 + 1
                            if size1==q+1:
                                line1=line1+1
                                c.append([(i,j)])
                                break
                        else:
                            break
                    else:
                        break
    if line1 != 0:
        d.append((line1,q))
if len(d)>0:
    print()
    print('For triangles pointing E, we have:')
for i in range(len(d)):
    if d[i][0]>0:
        if d[i][0]>1:
            print('     %d'%d[i][0],'triangles of size %d'%d[i][1])
        elif d[i][0]==1:
            print('     %d'%d[i][0],'triangle of size %d'%d[i][1])
grid = roate(grid)
grid = roate(grid)
grid = roate(grid)


c = []
d = []
for q in range(size,1,-1):
    line1 = 0
    for i in range(len(grid[0])-q+1):
        for j in range(q-1,len(grid)-q+1):
            size1 = 2
            while size1>0:
                if ([(i,j)]) in c:
                    break
                else:
                    if grid[i][j] == 1:
                        if list(grid[i+size1-1][j+1-size1:j+size1]) == [1]*(2*size1-1):
                            size1 = size1 + 1
                            if size1==q+1:
                                line1=line1+1
                                c.append([(i,j)])
                                break
                        else:
                            break
                    else:
                        break
    if line1 != 0:
        d.append((line1,q))
if len(d)>0:
    print()
    print('For triangles pointing S, we have:')
for i in range(len(d)):
    if d[i][0]>0:
        if d[i][0]>1:
            print('     %d'%d[i][0],'triangles of size %d'%d[i][1])
        elif d[i][0]==1:
            print('     %d'%d[i][0],'triangle of size %d'%d[i][1])
grid = roate(grid)
grid = roate(grid)
grid = roate(grid)

c = []
d = []
for q in range(size,1,-1):
    line1 = 0
    for i in range(len(grid[0])-q+1):
        for j in range(q-1,len(grid)-q+1):
            size1 = 2
            while size1>0:
                if ([(i,j)]) in c:
                    break
                else:
                    if grid[i][j] == 1:
                        if list(grid[i+size1-1][j+1-size1:j+size1]) == [1]*(2*size1-1):
                            size1 = size1 + 1
                            if size1==q+1:
                                line1=line1+1
                                c.append([(i,j)])
                                break
                        else:
                            break
                    else:
                        break
    if line1 != 0:
        d.append((line1,q))
if len(d)>0:
    print()
    print('For triangles pointing W, we have:')
for i in range(len(d)):
    if d[i][0]>0:
        if d[i][0]>1:
            print('     %d'%d[i][0],'triangles of size %d'%d[i][1])
        elif d[i][0]==1:
            print('     %d'%d[i][0],'triangle of size %d'%d[i][1])
