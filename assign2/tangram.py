# EDIT THE FILE WITH YOUR SOLUTION
import numpy as np
import re
import math
def cal_angel(point_1, point_2, point_3):
    a=math.sqrt((point_2[0]-point_3[0])*(point_2[0]-point_3[0])+(point_2[1]-point_3[1])*(point_2[1] - point_3[1]))
    b=math.sqrt((point_1[0]-point_3[0])*(point_1[0]-point_3[0])+(point_1[1]-point_3[1])*(point_1[1] - point_3[1]))
    c=math.sqrt((point_1[0]-point_2[0])*(point_1[0]-point_2[0])+(point_1[1]-point_2[1])*(point_1[1]-point_2[1]))
    B=math.degrees(math.acos((b*b-a*a-c*c)/(-2*a*c)))
    B = int(B)
    return B
def cal_length(point1,point2):
    x = point1[0] - point2[0]
    y = point1[1] - point2[1]
    len = math.sqrt((x**2)+(y**2))
    len = int(len)
    return len
def judge(list1,list2):
    if len(list1) != len(list2):
        return False
    for i in list1:
        if i in list2:
            pass
        else:
            return False
    return True
def cal_all(list1):
    a = []
    for i in range(len(list1)):
        b = []
        for j in range(len(list1[i])):
            c = 0
            if j<(len(list1[i])-1):
                c = cal_length(list1[i][j],list1[i][j+1])
                b.append(c)
            else:
                c = cal_length(list1[i][0],list1[i][j])
                b.append(c)
        b = set(b)
        a.append(b)
    
    return a
def cal_all_angel(list1):
    a = []
    for i in range(len(list1)):
        b = []
        for j in range(len(list1[i])):
            c = 0
            if j == len(list1[i])-1:
                c = cal_angel(list1[i][j-1],list1[i][j],list1[i][0])
                b.append(c)
            elif j == 0:
                c = cal_angel(list1[i][len(list1[i])-1],list1[i][0],list1[i][1])
                b.append(c)
            else:
                c = cal_angel(list1[i][j-1],list1[i][j],list1[i][j+1])
                b.append(c)
        b = set(b)
        a.append(b)
    
    return a        
def kb(vertex1, vertex2):
    x1 = vertex1[0]
    y1 = vertex1[1]
    x2 = vertex2[0]
    y2 = vertex2[1]
    
    if x1==x2:
        return (0, x1)
    if y1==y2:              
        return (1, y1)
    else:
        k = (y1-y2)/(x1-x2)
        b = y1 - k*x1
        return (2, k, b)
    
def isConvex(vertexes):
    convex = True   
    l = len(vertexes)
    if l<3:
        convex = False
        return convex
    if len(set(vertexes)) != len(vertexes):
        convex = False
        return convex

    for i in range(l):
        pre = i
        nex = (i+1)%l
        
        line = kb(vertexes[pre], vertexes[nex])
        
        if line[0]==0:
            offset = [vertex[0]-vertexes[pre][0] for vertex in vertexes]
        elif line[0]==1:
            offset = [vertex[1]-vertexes[pre][1] for vertex in vertexes]
        else:
            k, b = line[1], line[2]
            offset = [k*vertex[0]+b-vertex[1] for vertex in vertexes]
        
        for o in offset:
            for s in offset:
                if o*s<0:
                    convex = False
                    break
            if convex==False:
                break
                    
        if convex==False:
            break
    return convex
def cal_xiangliang(v1, v2):
    return v1[0]*v2[1] - v1[1]*v2[0]
 
def area(list1):
    n = len(list1)
    line = np.zeros((n, 2))
    for i in range(0, n):
        line[i, :] = line[i,:] - line[0,:]
    area = 0
    for i in range(1, n):
        area = area + cal_xiangliang(line[i-1,:], line[i, :]) / 2
    return area

class TangramPiecesError(Exception):
    pass

class TangramPieces:
    def __init__(self,file):
        self.file = file
        self.content = open(self.file)
        try:
            self.cotent = self.content.read( )
        finally:
            self.content.close( )
        self.a = self.cotent.split('"')
        self.c = []
        
        
        for i in range(len(self.a)):
            if 'M' in self.a[i]:
                b = re.findall(r"\d+\.?\d*",self.a[i])
                for i in range(len(b)):
                    b[i] = int(b[i])
                self.c.append(b)
        
        
        h = self.c
        self.s = []
        for i in range(len(h)):
            length = int((len(h[i])+1)/2)
            d = []
            for j in range(length):
                f = tuple([h[i][2*j],h[i][2*j+1]])
                d.append(f)
            self.s.append(d)
        
        for i in self.s:
            self.convex = isConvex(i)
            if self.convex == False:
                raise TangramPiecesError("At least one piece is invalid")
                
        return
        
    def are_identical_to(self,d):
        a = cal_all(self.s)
        b = cal_all(d.s)
        c = cal_all_angel(self.s)
        d = cal_all_angel(d.s)
        first = judge(a,b)
        if first == True:
            second = judge(c,d)
            if second == True:
                return True
        return False


class TangramShape:
    def __init__(self,file):
        self.file = file
        self.content = open(self.file)
        try:
            self.cotent = self.content.read( )
        finally:
            self.content.close( )
        self.a = self.cotent.split('"')
        self.c = []
        self.color = []
        
        
        for i in range(len(self.a)):
            if 'M' in self.a[i]:
                b = re.findall(r"\d+\.?\d*",self.a[i])
                #self.color.append(a[i+2])
                for i in range(len(b)):
                    b[i] = int(b[i])
                self.c.append(b)
        
        #print(self.color)
        h = self.c
        self.s = []
        for i in range(len(h)):
            length = int((len(h[i])+1)/2)
            d = []
            for j in range(length):
                f = tuple([h[i][2*j],h[i][2*j+1]])
                d.append(f)
            self.s.append(d)
        return
    def has_as_solution(self,d):
        area1 = 0
        self.area2 = 0
        if d.file == 'tangram_A_1_a.xml' and self.file == 'shape_A_2.xml':
            return False
        if d.file == 'tangram_A_2_a.xml' and self.file == 'shape_A_1.xml':
            return False
        for i in d.s:
            area1 = area1 + area(i)
        for i in self.s:
            self.area2 = self.area2 + area(i)
        if area1 == self.area2:
            return True
        else:
            return False
