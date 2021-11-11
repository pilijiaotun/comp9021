 # Written by *** for COMP9021

# Prompts the user for 4 positive integers, the last three of which
# represent a number of points (nothing will need to be done if it is 0),
# an integer max_coordinate such that all coordinates to be generated
# will be between -max_coordinate and max_coordinate included, and a
# square window size (width and height).
#
# Generates a list of x coordinates and a list of y coordinates of common
# length the number of points requested. Shows these lists, possibly truncated.
#
# x-coordinates increase from left to right,
# y-coordinates increase from bottom to top.
#
# 1. Displays the points, without duplicates, from highest to lowest,
#    and from left to right for a given height.
#
# 2. Displays the size of the smallest rectangle, as well as its top left
#    and bottom right corners, in which all points fit.
#
# 3. Displays the maximum number of points that can fit in a square window
#    with the provided size. The window has to be fully included in the
#    enclosing rectangle. In case such a window exists, then displays the
#    top left and bottom right corners of the leftmost, topmost such window.


from random import seed, randrange
import sys

try:
    for_seed, nb_of_points, max_coordinate, window_size =\
            (int(e) for e in input('Enter four positive integers: ').split())
    if for_seed < 0 or nb_of_points < 0 or max_coordinate < 0\
       or window_size < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
if not nb_of_points:
    print('No point to play with, see you later!')
    sys.exit()
seed(for_seed)
x_coordinates = [randrange(-max_coordinate, max_coordinate + 1)
                     for _ in range(nb_of_points)
                ]
y_coordinates = [randrange(-max_coordinate, max_coordinate + 1)
                     for _ in range(nb_of_points)
                ]
field_width = max(max(len(str(e)) for e in x_coordinates),
                  max(len(str(e)) for e in y_coordinates)
                 )
print('Here is how the x-coordinates of your points start:')
print('  ', ' '.join(f'{e:{field_width}}' for e in x_coordinates)
                [: 80 // (field_width + 1) * (field_width + 1)]
     )
print('Here is how the y-coordinates of your points start:')
print('  ', ' '.join(f'{e:{field_width}}' for e in y_coordinates)
                [: 80 // (field_width + 1) * (field_width + 1)]
     )

# INSERT CODE HERE
zip1 = zip(x_coordinates,y_coordinates)
zipp = list(zip1)
print()
print('Here are the points, without duplicates, from highest to lowest,')
print(' and from left to right for a given height:')

new = []
for j in zipp:
    if j not in new: 
        new.append(j)
for i in range(len(new)):
    j=i
    for j in range(len(new)):
        if (new[i][0]<new[j][0]):
            new[i],new[j]=new[j],new[i]
        if (new[i][1]>new[j][1]):
            new[i],new[j]=new[j],new[i]
for i in range(len(new)):
    print(' ',new[i])

x = x_coordinates
y = y_coordinates
maxx = x_coordinates[0]
minx = x_coordinates[0]
maxy = y_coordinates[0]
miny = y_coordinates[0]

for i in x_coordinates:
    if i>maxx:
        maxx = i
    elif i<minx:
        minx = i
for i in y_coordinates:
    if i>maxy:
        maxy = i
    elif i<miny:
        miny = i
size = abs(maxx-minx)*abs(maxy-miny)
print()
print('All points fit in a rectangle of size %d,'%size)
print(' with (%d, %d) as top left corner, and'%(minx,maxy))
print(' with (%d, %d) as bottom right corner.'%(maxx,miny))
print()

if window_size>abs(maxx-minx) or window_size>abs(maxy-miny):
   print('The maximum number of points that fit in a square window of size %d'%(window_size))
   print(' enclosed within the rectangle is 0.')
else:
    countx=minx
    county=maxy
    count = 0
    democount = 0
    for j in range(maxy,miny-1+window_size,-1):
        for i in range(minx,maxx+1-window_size,1):
            democount = 0
            for s in range(len(new)):
                if new[s][0]>=i and new[s][0]<=i+window_size and new[s][1]<=j and new[s][1]>=j-window_size:
                    democount = democount+1
                if democount>count:
                    count = democount
                    countx = i
                    county = j
    print('The maximum number of points that fit in a square window of size %d'%(window_size))
    print(' enclosed within the rectangle is %d.'%(count))
    print('The leftmost, topmost such window has (%d, %d) as top left corner,'%(countx,county))
    print(' and (%d, %d) as bottom right corner.'%(countx+window_size,county-window_size))














