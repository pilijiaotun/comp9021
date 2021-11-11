# Written by *** for COMP9021
#
# Given a sequence L of numbers, the greedy increasing subsequence of L,
# say G, is inductively defined as follows:
# - If L is of length at most 1 then G is L.
# - If L is of the form (e_0, e_1, ..., e_n) with n >= 1, then:
#   - either e_1 is greater than e_0, in which case G is e_0 followed by the
#     greedy increasing subsequence of (e_1, ..., e_n),
#   - or e_1 is less than or equal to e_0, in which case G is the greedy
#     increasing subsequence of (e_0, e_2,..., e_n).
#
# 1. Generates a random list L of digits whose length is chosen by the user
#    (done).
# 2. Displays L (done),
# 3. Displays the integer made from these digits (without the leading 0s,
#    if any).
# 4. Graphically displays the greedy increasing subsequence of L as
#    horizontal bars.
# 5. Graphically displays the nonzero values in L as steps.


from random import seed, randrange
import sys


try: 
    for_seed, length = (int(x) for x in input('Enter two integers, the second '
                                              'one being strictly positive: '
                                             ).split()
                       )
    if length <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
values = [randrange(10) for _ in range(length)]
print('Here are the generated digits:', values)
print()
# INSERT CODE HERE:

print('The integer made from these digits is: ',end='')
values1 = values.copy()
for j in range(len(values1) - 1, 0, -1):
    if values1[j] == values1[j-1]==0:
        del values1[j]
    elif values1[0]==0:
        del values1[0]                 
for g in values1:
    print(g,end='')

print('\n')
print('Here is the greedy increasing subsequence of values, '
      'horizontally displayed:'
     )
# INSERT CODE HERE:
Max = values[0]
greedy=[values[0]]
for i in values:
    if i > Max:
        Max = i
        greedy.append(i)
if (greedy[0]== 0):
        greedy.remove(greedy[0])
print()
for z in greedy:
    print('   ',z*'-')
print()
print('Here are the nonzero values, displayed as stairs:')
# INSERT CODE HERE:
print()
q = 0
nonezero2 = []
for x in values:
    if x!=0:  
        nonezero2.append(x)
for t in nonezero2:
    print('   ',q*' ',t*'-')
    q = t+q
print()

