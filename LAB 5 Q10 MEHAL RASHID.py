print("Sin() Cos() Tan() Table :-")

import math
def table(range1,range2,step):
    sin=[]
    cos=[]
    tan=[]
    degrees_lst=[]
    for degrees in range(range1,range2+1,step):
        sinx = math.sin(math.radians(degrees))
        sinx = float("{0:.2f}".format(sinx))
        sin.append(sinx)
        cosx = math.cos(math.radians(degrees))
        cosx = float("{0:.2f}".format(cosx))
        cos.append(cosx)
        tanx = math.tan(math.radians(degrees))
        tanx = float("{0:.2f}".format(tanx))
        tan.append(tanx)
        degrees_lst.append(degrees)
    print("_"*49)
    print("\n\n| {3:10}| {0:10}| {1:10}| {2:10}|".format("Sin","Cos","Tan","Degrees"))
    for row in range(len(sin)):
        print("\n")
        for col in range(4):
            if col==1:
                print("| {0:10}".format(str(sin[row])),end="")
            elif col==2:
                print("| {0:10}".format(str(cos[row])),end="")
            elif col==3:
                print("| {0:10}|".format(str(sin[row])),end="")
            elif col==0:
                print("| {0:10}".format(str(degrees_lst[row])),end="")
    print("\n")
    print("_"*49)            
                
range1 = int(input("Please enter starting value in degrees    : "))
range2 = int(input("Please enter ending value in degrees      : "))        
step   = int(input("Please enter the step between these values: "))

table(range1,range2,step)
