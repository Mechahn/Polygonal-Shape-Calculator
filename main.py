import math

print("\nEnter the 4 coordinates below:")

#Below is the collection of the data for coordinate locations

p1x = float(input("\nX of Coord. 1: "))
p1y = float(input("Y of Coord. 1: "))

p2x = float(input("\nX of Coord. 2: "))
p2y = float(input("Y of Coord. 2: "))


p3x = float(input("\nX of Coord. 3: "))
p3y = float(input("Y of Coord. 3: "))


p4x = float(input("\nX of Coord. 4: "))
p4y = float(input("Y of Coord. 4: "))

#Below is the measurements of the distances between said coordinates.
#Labeled as "Dist (distance)_ [first coordinate number] to [second coordinate number]"

def dist_1to2():
    xes = p2x - p1x
    xes_squared = math.pow(xes, 2)
    yes = p2y - p1y
    yes_squared = math.pow(yes, 2)
    added = xes_squared + yes_squared
    return added

def dist_2to3():
    xes = p3x - p2x
    xes_squared = math.pow(xes, 2)
    yes = p3y - p2y
    yes_squared = math.pow(yes, 2)
    added = xes_squared + yes_squared
    return added

def dist_3to4():
    xes = p4x - p3x
    xes_squared = math.pow(xes, 2)
    yes = p4y - p3y
    yes_squared = math.pow(yes, 2)
    added = xes_squared + yes_squared
    return added

def dist_4to1():
    xes = p1x - p4x
    xes_squared = math.pow(xes, 2)
    yes = p1y - p4y
    yes_squared = math.pow(yes, 2)
    added = xes_squared + yes_squared
    return added

# Below is the calling of the distance measurement functions

dist_1to2()
dist_2to3()
dist_3to4()
dist_4to1()

#Below is the complete coordinate of each coord.
# "C" and number for which "coordinate" it is.
C1 = (p1x, p1y)
C2 = (p2x, p2y)
C3 = (p3x, p3y)
C4 = (p4x, p4y)

#Below is the measurement of each sequence of 3 coordinates. Named as "angle, [first coord, second, third]"

def angle123():

    def getAngle(a, b, c):
        ang = math.degrees(math.atan2(c[1] - b[1], c[0] - b[0]) - math.atan2(a[1] - b[1], a[0] - b[0]))
        return ang + 360 if ang < 0 else ang

    angle = getAngle(C1, C2, C3)
    return angle

def angle234():

    def getAngle(a, b, c):
        ang = math.degrees(math.atan2(c[1] - b[1], c[0] - b[0]) - math.atan2(a[1] - b[1], a[0] - b[0]))
        return ang + 360 if ang < 0 else ang

    angle = getAngle(C2, C3, C4)
    return angle

def angle341():

    def getAngle(a, b, c):
        ang = math.degrees(math.atan2(c[1] - b[1], c[0] - b[0]) - math.atan2(a[1] - b[1], a[0] - b[0]))
        return ang + 360 if ang < 0 else ang

    angle = getAngle(C3, C4, C1)
    return angle

def angle412():

    def getAngle(a, b, c):
        ang = math.degrees(math.atan2(c[1] - b[1], c[0] - b[0]) - math.atan2(a[1] - b[1], a[0] - b[0]))
        return ang + 360 if ang < 0 else ang

    angle = getAngle(C4, C1, C2)
    return angle

#Below is calling of the angle measurement functions

angle123()
angle234()
angle341()
angle412()

#Below changes the angle functions into variables so to make the readability of which angle is which easier

angle1 = angle412()
angle2 = angle123()
angle3 = angle234()
angle4 = angle341()

#Below prints out the calculated distances and angles between stated coordinates

print("\n")
print("Angle 1: {}".format(angle1))
print("Angle 2: {}".format(angle2))
print("Angle 3: {}".format(angle3))
print("Angle 4: {}".format(angle4))

print("\n")
print("Distance 1: {}".format(dist_1to2()))
print("Distance 2: {}".format(dist_2to3()))
print("Distance 3: {}".format(dist_3to4()))
print("Distance 4: {}".format(dist_4to1()))

#below is the printing for if the shape formed is a square
# Properties of square-
#       1) Has 4 congruent sides
#       2) Has 4 congruent angles

if dist_1to2() == dist_2to3() and dist_1to2() == dist_3to4() and dist_1to2() == dist_4to1() and angle123() == angle234() and angle123() == angle341() and angle123() == angle412():
    print("\nThe shape is a square")
else:
    print("\nThe shape is not a square")