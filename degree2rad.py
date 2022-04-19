import math
val =input("Enter the radians value: ")
print("you have entered "+val+" radians")
rad = float(val)
def degreeConvert(rad):
    degree = rad*180/math.pi
    return degree
    
print("value in degree is ",degreeConvert(rad))