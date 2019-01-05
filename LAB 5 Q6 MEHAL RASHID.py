def first_eq():
    print("\nv = u + at")
    u = float(input("\nPlease enter the initial velocity : "))
    a = float(input("PLease enter the acceleration     : "))
    t = float(input("Please enter the time in seconds  : "))
    v= u + (a*t)
    v = float("{0:.2f}".format(v))
    print("\nThe Final velocity is : ",v,"m/s")
    user_input()
def second_eq():
    print("\ns = ut + (1/2)at\u00b2")
    u = float(input("\nPlease enter the initial velocity : "))
    a = float(input("PLease enter the acceleration     : "))
    t = float(input("Please enter the time in seconds  : "))
    s = u*t + (1/2)*a*(t**2)
    s = float("{0:.2f}".format(s))
    print("\nThe Distance is : ",s,"m")
    user_input()
def third_eq():
    u = float(input("\nPlease enter the initial velocity : "))
    a = float(input("PLease enter the acceleration     : "))
    s = float(input("Please enter the distance         : "))
    import math
    v = math.sqrt((u**2)+(2*a*s))
    v = float("{0:.2f}".format(v))
    print("\nThe Final velocity is : ",v,"m/s")
    user_input()
    
print("\n\nNEWTONS 3 Laws of Motion")
def user_input():
    user = input("\n\nWhich Equation of motion do you want to use? (enter only 'first','second','third' or 'end') : ")
    user = user.casefold()
    while user!='first' and user!='second' and user!='third' and user!='end':
        print("\nPlease only enter 'first','second','third' or 'end'!")
        user = input("Which law do you want to learn? (enter only 'first','second','third' or 'end') : ")
    else:
        if user=='first':
            first_eq()
        elif user=='second':
            second_eq()
        elif user=='third':
            third_eq()
        else:
            print("Thank you")

user_input()
