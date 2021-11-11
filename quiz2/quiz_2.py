# Written by *** for COMP9021
#
# Implements two functions that both return a string:
# - for line(), the equation of a line that goes through both points
#   provided as arguments;
# - for parabola(), the equation of a parabola that has as roots the
#   values provided as arguments.


def line(point_1, point_2):
    '''It can be assumed that point_1 and point_2 are both
    tuples of 2 integers.
    
    The function is meant to return a string that represents the equation
    of a line that goes through both points, in case they are different;
    otherwise, the function returns None.

    - If the line is vertical, then the function returns a string of the
      form 'x = b', with b the representation of a floating point number
      with 2 digits after the decimal point.
    - If the line is horizontal, then the function returns a string of the
      form 'y = b', with b the representation of a floating point number
      with 2 digits after the decimal point.
    - If the line is neither horizontal nor vertical, then
        - either the intercept is 0, in which case the function returns
          a string of the form 'y = ax', with a the representation of a
          floating point number with 2 digits after the decimal point;
        - or the intercept is not 0, in which case the function returns
          a string of the form 'y = ax ± b' with a and b representations
          of floating point numbers with 2 digits after the decimal point,
          and with b positive. 
    '''
    x1 = point_1[0]
    x2 = point_2[0]
    y1 = point_1[1]
    y2 = point_2[1]
    if x1!=x2 :
      k = (y2-y1)/(x2-x1)
      b = (y1*x2-x1*y2)/(x2-x1)
      if k == 0:
        b = y1
        string=('y =','%.2f'%b)
        return " ".join(string)
      else:
        if b>0:
            string=('y = ','%.2f'%k,'x + ','%.2f'%b)
            return "".join(string)
        elif b<0:
            b = -b
            string=('y = ','%.2f'%k,'x - ','%.2f'%b)
            return "".join(string)
        elif b==0:
            string=('y = ','%.2f'%k,'x')
            return "".join(string)
    elif x1==x2 and y1==y2:
      return
    elif x1==x2 and y1!=y2:
      b = x1
      string = ('x =','%.2f'%b)
      return " ".join(string)
      

    
    ### REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE
        
def parabola(*roots):
    '''It can be assumed that roots consists of nothing but integers.

    The function is supposed to return a string that represents a
    second-order equation with 1 as factor of x^2, such that the roots
    of the equation are precisely the members of the argument root, in
    case such an equation exists; otherwise, the function returns None.

    The returned string should have the form 'x^2 ± bx ± c' with b and
    c positive integers, modulo the following conditions.
    - In case b is 0, ' + bx' is omitted.
    - In case c is 0, '+ c' is omitted.
    - In case b is 1, b is omitted.    
    '''
    new=[]
    for i in roots:
      if i not in new:
        new.append(i)

    if len(new)>2 or len(new)==0:
      return
    elif len(new)==1:
      b=-2*new[0]
      c=new[0]**2
      if c==0:
        result = ('x^2 = 0')
        return "".join(result)
      elif c!=0 and b<0:
        b=abs(b)
        result = ('x^2 - %dx + %d = 0'%(b,c))
        return "".join(result)
      elif c!=0 and b>0 and b!=1:
        result = ('x^2 + %dx + %d = 0'%(b,c))
        return "".join(result)
      elif c!=0 and b==1:
        result = ('x^2 + x + %d = 0'%c)
        return "".join(result)
      elif c!=0 and b==-1:
        result = ('x^2 - x + %d = 0'%c)
        return "".join(result)
    

    elif len(new)==2:
      b = -(new[0]+new[1])
      c = new[0]*new[1]
      if c==0:
        if b<0 and b!=-1:
          b=abs(b)
          result = ('x^2 - %dx = 0'%b)
          return "".join(result)
        elif b>0 and b!=1:
          result = ('x^2 + %dx = 0'%b)
          return "".join(result)
        elif b==1:
          result = ('x^2 + x = 0')
          return "".join(result)
        elif b==-1:
          result = ('x^2 - x = 0')
          return "".join(result)

      elif c>0:
        if b<0 and b!=-1:
          b=abs(b)
          result = ('x^2 - %dx + %d = 0'%(b,c))
          return "".join(result)
        elif b>0 and b!=1:
          result = ('x^2 + %dx + %d = 0'%(b,c))
          return "".join(result)
        elif b==1:
          result = ('x^2 + x + %d = 0'%(c))
          return "".join(result)
        elif b==-1:
          result = ('x^2 - x + %d = 0'%(c))
          return "".join(result)

      elif c<0:
        c = abs(c)
        if b<0 and b!=-1:
          b=abs(b)
          result = ('x^2 - %dx - %d = 0'%(b,c))
          return "".join(result)
        elif b>0 and b!=1:
          result = ('x^2 + %dx - %d = 0'%(b,c))
          return "".join(result)
        elif b==1:
          result = ('x^2 + x - %d = 0'%(c))
          return "".join(result)
        elif b==-1:
          result = ('x^2 - x - %d = 0'%(c))
          return "".join(result)  
        


    
    


    ### REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE

    
    
    
