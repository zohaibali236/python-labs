radius1 = float(input("Enter Radius of circle "))
radius2 = float(input("Enter Radius of circle "))
radius3 = float(input("Enter Radius of circle "))

angularSpeed = float(input("Enter the angular speed of object "))

print("The linear velocity of object when radius is %0.2f" %radius1, "is %0.2fm/s" %(radius1*angularSpeed)+ "\
, when radius is %0.2f" %radius2, "velocity will be %0.2f" %(radius2*angularSpeed), "\
and when radius is %0.2f" %radius3, "velocity will be %0.2f" %(radius3*angularSpeed))