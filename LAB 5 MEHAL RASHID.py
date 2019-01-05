import math
def area(radius,height,decimals):
    _area = (2*math.pi*radius*height) + (2*math.pi*(radius**2))
    print("\n\nArea of the cylinder is {0:.{1}f}cm\u00b2".format(_area,decimals))
          
def volume(radius,height,decimals):
    _volume = math.pi*(radius**2)*height
    print("Volume of the cylinder is {0:.{1}f}cm\u00b3".format(_volume,decimals))

radius = float(input("Please enter the radius of the cylinder      : "))
height = float(input("Please enter the height of the cylinder      : "))
decimals = int(input("Please enter the number of decimals you want : "))

area(radius,height,decimals)
volume(radius,height,decimals)
