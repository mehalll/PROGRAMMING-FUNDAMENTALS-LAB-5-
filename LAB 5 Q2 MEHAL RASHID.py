def area(length,width):
    _area = length * width
    print("\n\nThe area of rectangle is {0}cm\u00b2".format(_area))

def volume(length,widht,height):
    _volume = length * width * height
    print("The volume of cuboid is {0}cm\u00b3".format(_volume))

length = int(input("Please enter the length of the rectangle:"))
width  = int(input("Please enter the width  of the rectangle:"))
height = int(input("Please enter the height of the rectangle:"))

area(length,width)
volume(length,width,height)
    
