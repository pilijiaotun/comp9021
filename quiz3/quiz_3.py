# Written by *** for COMP9021

# Prompts the user for two integers.
# - The first one should be between 1 and 4, with
#   * 1 meaning initially looking North,
#   * 2 meaning initially looking East,
#   * 3 meaning initially looking South,
#   * 4 meaning initially looking West.
# - The second one should be positive. When written in base 3, its consecutive
#   digits read from left to right represent the directions to take, with
#   * 0 meaning going in the direction one is initially looking at,
#   * 1 meaning 45 degrees left of the direction one is initially looking at,
#   * 2 meaning 45 degrees right of the direction one is initially looking at.
#
# Prints out:
# - the direction one is originally looking at, as an arrow,
# - the representation of the second digit in base 3,
# - the corresponding sequence of directions to take, as arrows,
# - in case one is originally looking North or South, the path,
#   so the sequence of arrows again, but nicely displayed.


import sys

try:
    initial_direction, directions = input('Enter an integer between 1 and 4 '
                                          'and a positive integer: '
                                         ).split()
    if len(initial_direction) != 1\
       or len(directions) > 1 and directions[0] == '0':
        raise ValueError
    initial_direction = int(initial_direction)
    directions = int(directions)
    if initial_direction not in {1, 2, 3, 4} or directions < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

# INSERT YOUR CODE HERE
print()
up = chr(8679)
down = chr(8681)
left = chr(8678)
right = chr(8680)
left_up = chr(11009)
left_down = chr(11011)
right_up = chr(11008)
right_down = chr(11010)

first_look = list([up, right, down, left])
print('Ok, you want to first look this way:',first_look[initial_direction-1])
print()

x = 3
b = []
while True:
    s=directions//x
    y=directions%x
    b=b+[y]
    if s == 0:
            break
    directions=s
b.reverse()
print('In base 3, the second input reads as:', ''.join(map(str, b)))

if initial_direction == 1:
    list1 = [up, left_up, right_up]
elif initial_direction == 2:
    list1 = [right, right_up, right_down]
elif initial_direction == 3:
    list1 = [down, right_down, left_down]
elif initial_direction == 4:
    list1 = [left, left_down, left_up]
c = []
num_left = 0
num_right = 0
for i in range(len(b)):
    c.append(list1[b[i]])
print("So that's how you want to go: ", ''.join(map(str, c)))
print()

for j in range(len(c)):
    if c[j] == left_up or c[j] == left_down:
        num_left = num_left + 1
    elif c[j] == right_up or c[j] == right_down:
        num_right = num_right + 1


if initial_direction == 4 or initial_direction == 2:
    print("I don't want to have the sun in my eyes, but by all means have a go at it!")
elif initial_direction == 3:
    print("Let's go then!")
    blank= 0
    number = 0

    for q in range(1,len(c)):
        if c[q] == left_up or c[q] == left_down:
            blank = blank - 1
            if blank == -1:
                number = number+1
                blank = 0
        elif c[q] == right_up or c[q] == right_down:
            blank = blank + 1

    blank_g = [' '*number]
    print(blank_g[0]+c[0])
    for q in range(1,len(c)):
        if c[q] == left_down:
            number = number - 1
            blank_g = [' '*number]
            print(blank_g[0]+c[q]) 
        elif c[q] == right_down:
            number = number + 1
            blank_g = [' '*number]
            print(blank_g[0]+c[q])
        elif c[q] == down:
            blank_g = [' '*number]
            print(blank_g[0]+c[q])

elif initial_direction == 1:
    
    print("Let's go then!")
    blank= 0
    number = 0
    double_count = 0
    for q in range(1,len(c)):
        if c[q] == left_up :
            blank = blank - 1
            double_count = double_count - 1
            if blank == -1:
                number = number+1
                blank = 0
        elif c[q] == right_up:
            blank = blank + 1
            double_count = double_count + 1
            
    count = abs(number-abs(double_count))       
    blank_g = [' '*count]
    c.reverse()
    

    for s in range(0,len(c)):
        if c[s] == left_up:
            blank_g = [' '*count]
            print(blank_g[0]+c[s]) 
            count = count + 1
        elif c[s] == right_up:
            blank_g = [' '*count]
            print(blank_g[0]+c[s])
            count = count - 1
        elif c[s] == up:
            blank_g = [' '*count]
            print(blank_g[0]+c[s])
                                           


