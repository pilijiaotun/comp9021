# Insert your code here
from itertools import permutations
from collections import defaultdict
from time import time

with open ('wordsEn.txt','rt') as f:
    dictionary=set(f.read().split())

import sys

while True:
    try:
        inputa=str(input('Enter between 3 and 10 lowercase letters: '))
        inputb=(inputa.replace(' ',''))
        for i in inputb:
            if not i.islower():
                raise ValueError('Incorrect input, giving up...')
        if len(inputb)<3 or len(inputb)>10:
            raise ValueError('Incorrect input, giving up...')
        break
    except ValueError:
        print('Incorrect input, giving up...')
        sys.exit()

search=[]
leninput = len(inputb)
for i in dictionary:
    abb = list(i)
    ina = list(inputb)
    for j in range(len(abb)):
        if abb[j] in ina:
            ina.remove(abb[j])
            abb[j]=''
    count = 0
    for z in abb:
        if z=='':
            count = count+1
    if len(abb)==count and len(ina)> -1:
            search.append(i)


letter=[chr(i) for i in range(97,97+26)]
value=[2,5,4,4,1,6,5,5,1,7,6,3,5,2,3,5,7,2,1,2,4,6,6,7,5,7]
zip1 = zip(letter,value)
zipp = list(zip1)


newsearch=[]
count=[]

for i in search:
    qaq = list(i)
    countnumber = 0
    for j in range(len(qaq)):
        value1 = letter.index(qaq[j])
        countnumber = countnumber + zipp[value1][1]
    count.append(countnumber)
    maxvalue = max(count)

for i in search:
    qaq = list(i)
    countnumber = 0
    for j in range(len(qaq)):
        value1 = letter.index(qaq[j])
        countnumber = countnumber + zipp[value1][1]
    if countnumber == maxvalue:
        newsearch.append(i)
newsearch.sort()

if len(search)==0:
    print('No word is built from some of those letters.')
elif len(newsearch)==1:
    print('The highest score is %d.'%maxvalue)
    print('The highest scoring word is %s'%newsearch[0])
else:
    print('The highest score is %d.'%maxvalue)
    print('The highest scoring words are, in alphabetical order:')
    for i in newsearch:
        print ('   ',"".join(i))
