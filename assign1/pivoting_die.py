# Insert your code here
while True:
    try:
        N = int(input('Enter the desired goal cell number: '))
        if N <= 0 :
            raise ValueError('Incorrect value, try again')
        break
    except ValueError:
        print('Incorrect value, try again')
l=[3,1,4,6]
r=[2,3,5,4]
d = 0
sum1 = 0
sum2 = 0
sumsum1 = 0
sumsum2 = 0
N=N-1
while True:
    if d == 0:
        sum1 = sum1 + 1
        if N - sumsum1 - sumsum2 > sum1:
            for j in range(sum1%4):
                r = (r[0], l[3], r[2], l[1])
                l = (l[3], l[0], l[1], l[2])
            d = 1
        else:
            for j in range(N - sumsum1 - sumsum2):
                r = (r[0], l[3], r[2], l[1])
                l = (l[3], l[0], l[1], l[2])
            d = 1
            break
        sumsum1 = sumsum1+sum1
        
    elif d == 1:
        sum2 = sum2 + 1
        if N - sumsum1 - sumsum2 > sum2:
            for j in range(sum2%4):
                l = (r[2], l[1], r[0], l[3])
                r = (r[1], r[2], r[3], r[0])
            d = 2
        else:
            for j in range(N - sumsum1 - sumsum2):
                l = (r[2], l[1], r[0], l[3])
                r = (r[1], r[2], r[3], r[0])
            d = 2
            break
        sumsum2 = sumsum2+sum2
        
    elif d == 2:
        sum1 = sum1 + 1
        if N - sumsum1 - sumsum2 > sum1:
            for j in range(sum1%4):
                r = (r[0], l[1], r[2], l[3])
                l = (l[1], l[2], l[3], l[0])
            d = 3
        else:
            for j in range(N - sumsum1 - sumsum2):
                r = (r[0], l[1], r[2], l[3])
                l = (l[1], l[2], l[3], l[0])
            d = 3
            break
        sumsum1 = sumsum1+sum1
        
    elif d == 3:
        sum2 = sum2 + 1
        if N - sumsum1 - sumsum2 > sum2:
            for j in range(sum2%4):
                l = (r[0], l[1], r[2], l[3])
                r = (r[3], r[0], r[1], r[2])
            d = 0
        else:
            for j in range(N - sumsum1 - sumsum2):
                l = (r[0], l[1], r[2], l[3])
                r = (r[3], r[0], r[1], r[2])
            d = 0
            break
        sumsum2 = sumsum2+sum2
print('On cell %d, %d is at the top, %d at the front, and %d on the right.'%(N+1,l[0],r[0],l[1]))
