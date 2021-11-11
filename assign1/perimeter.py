# Insert your code here
filename = input('Which data file do you want to use? ')
rec,list_x1, list_y1,list_x2, list_y2 = [],[],[],[],[]
with open(f'{filename}','r') as file:
    for line in file:
        for i in line.strip().split():
            x1,y1,x2,y2 = int(line.strip().split()[0]),int(line.strip().split()[1]),int(line.strip().split()[2]),int(line.strip().split()[3])
            rec.append((x1,y1,x2,y2))

def getNonRepeatList(data):
    new_data = []
    for i in range(len(data)):
        if data[i] not in new_data:
            new_data.append(data[i])
    return new_data

rec = getNonRepeatList(rec)

for i in rec:
    for j in rec:
        if j[0]>i[0] and j[1]>i[1] and j[2]<i[2] and j[3]<i[3]:
            rec.remove(j)

getpoint=[]

for i in range(len(rec)):
    for j in range(rec[i][0],rec[i][2]+1):
        getpoint.append((j,rec[i][1]))
        getpoint.append((j,rec[i][3]))
    for j in range(rec[i][1],rec[i][3]+1):
        getpoint.append((rec[i][0],j))
        getpoint.append((rec[i][2],j))

for i in rec:
    for j in getpoint[:]:
        if j[0]<i[0] or j[0]==i[0]:
            pass
        elif j[0]>i[2] or j[0]==i[2]:
            pass
        elif j[1]<i[1] or j[1]==i[1]:
            pass
        elif j[1]>i[3] or j[1]==i[3]:
            pass
        else:
            getpoint.remove(j)
getpoint = list(set(getpoint))

total=0
for i in range(len(getpoint)):
    if (getpoint[i][0]+1,getpoint[i][1]) in getpoint:
        total =total+1
for i in range(len(getpoint)):
    if (getpoint[i][0],getpoint[i][1]+1) in getpoint:
        total =total+1

print('The perimeter is: %d'%total)
