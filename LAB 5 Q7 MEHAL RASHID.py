import math

def projectile(init_veloc,angle):
    gravity = 9.8
    max_height = (init_veloc**2)*((math.sin(angle))**2) / (2*gravity)
    time_total = 2*init_veloc*math.sin(angle) / gravity
    hor_range  = (init_veloc**2)*math.sin((2*angle)) / gravity

    print("\n\nThe Maximum height reached by the object is : {0:.1f}meters".format(max_height))
    print("The Total time taken by the object is       : {0:.1f}seconds".format(time_total))
    print("The Horizontal Range of the object is       : {0:.1f}meters".format(hor_range))

init_veloc = float(input("Please enter the initial velocity of the object    : "))
angle      = float(input("Please enter the angle of projection of the object : "))
angle = math.radians(angle)
projectile(init_veloc,angle)
