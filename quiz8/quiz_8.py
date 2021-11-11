# Written by *** for COMP9021

# Defines:
# - a class: DarkCorridor, implementing 2 special methods
# - another class: Pacer, implementing 3 special methods
#   and (at least) 2 extra methods:
#   * pace()
#   * now_here_in_dark_corridor()
# - a function: compare_stress(), that takes two Pacer objects
#   as arguments.

# Uses the Unicode characters of code point 9654, 9664 and 11036.

from itertools import cycle, chain, islice


# INSERT YOUR CODE HERE
blank = chr(11036)
left  = chr(9664)
right = chr(9654)
class DarkCorridorError(Exception):
    pass
 
class DarkCorridor:
    def __init__(self,length):
        if length <= 0:
            raise DarkCorridorError('The length of the corridor should be strictly positive')
        self.length = length
        self.line = []
        self.line = self.length*[0]
    def __repr__(self):
        return f'DarkCorridor({self.length})'
    def __str__(self):
        str1 = len(self.line)*(' %s'%blank)
        return f'{str1}'



    
class Pacer:
    
    def __init__(self,name,D):
        self.name = name
        self.D    = repr(D)
        self.length = D.length
        self.line = self.length*[0]
        self.line[0] = 1
        self.count = 0
    def __repr__(self):
        return f'Pacer(\'{self.name}\', {self.D})'
    def __str__(self):
        str11 = self.length*(' %s'%blank)
        return f'{self.name} in {str11}'
    def now_here_in_dark_corridor(self):
        str1 = ''
        for i in range(len(self.line)):
            if self.line[i] == 0:
                str1 = str1+(' %s'%blank)
            elif self.line[i] == 1:
                str1 = str1+(' %s'%right)
            elif self.line[i] == 2:
                str1 = str1+(' %s'%left)
        print(str1)
    def pace(self,num):
        self.count = self.count + num
        for i in range(num):
            for j in range(len(self.line)):
                if self.line[j] != 0:
                    if j == 0:
                        if self.line[j] == 1:
                            self.line[j] = 0
                            self.line[j+1] = 1
                            break
                        elif self.line[j] == 2:
                            self.line[j] = 1
                            break
                    elif j == len(self.line)-1:
                        if self.line[j] == 1:
                            self.line[j] = 2
                            break
                        elif self.line[j] == 2:
                            self.line[j-1] = 2
                            self.line[j] = 0
                            break
                    elif j!= 0 and j!= len(self.line)-1:
                        if self.line[j] == 1:
                            self.line[j] = 0
                            self.line[j+1] = 1
                            break
                        elif self.line[j] == 2:
                            self.line[j] = 0
                            self.line[j-1] = 2
                            break
    def countsteps(self):
        return self.count


def compare_stress(a,b):
    numa = a.countsteps()
    numb = b.countsteps()
    abs1 = numa - numb
    if (numa == 0 or numa ==1) and (numb == 0 or numb == 1):
        print(1)
        if abs1 == 0:
            print('%s and %s are both as stressed (%d step).'%(a.name,b.name,numa))
        elif abs1 < 0:
            print('%s (%d step) is more stressed than %s (%d step).'%(b.name,numb,a.name,numa))
        elif abs1 > 0:
            print('%s (%d step) is more stressed than %s (%d step).'%(a.name,numa,b.name,numb))
    elif (numa == 0 or numa ==1) and (numb != 0 or numb != 1):
        print(2)
        print('%s (%d steps) is more stressed than %s (%d step).'%(b.name,numb,a.name,numa))
    elif (numb == 0 or numb ==1) and (numa != 0 or numa != 1):
        print(3)
        print('%s (%d steps) is more stressed than %s (%d step).'%(a.name,numa,b.name,numb))
    elif (numb != 0 or numb !=1) and (numa != 0 or numa != 1):
        if abs1 == 0:
            print('%s and %s are both as stressed (%d steps).'%(a.name,b.name,numa))
        elif abs1 < 0:
            print('%s (%d steps) is more stressed than %s (%d steps).'%(b.name,numb,a.name,numa))
        elif abs1 > 0:
            print('%s (%d steps) is more stressed than %s (%d steps).'%(a.name,numa,b.name,numb))
        
